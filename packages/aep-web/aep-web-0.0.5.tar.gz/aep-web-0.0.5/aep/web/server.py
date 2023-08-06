import argparse
import json
import logging
import re
from pathlib import Path
from typing import Any, List, Text

import aep.tools.libs.data
import uvicorn
from aep.tools.generate import stages_table
from aep.tools.libs.libgenerate import simulate
from fastapi import (Depends, FastAPI, File, Query, Request, Response,
                     UploadFile)
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pkg_resources import resource_filename, resource_string

import aep.web.data
from aep.web.arguments import parse_args

templates = Jinja2Templates(directory=resource_filename(__name__, "templates"))


app = FastAPI()


@app.get("/static/bulma.css")
async def bulma_static() -> Response:
    return Response(resource_string("aep.web", "static/bulma.css"))


def error(
    request: Request, message: Text, web_root: Text
) -> templates.TemplateResponse:

    # request must be included in TemplateResponse
    return templates.TemplateResponse(
        "error.html", {"error": message, "request": request, "web_root": web_root}
    )


def islist(item: Any) -> bool:
    """Return true if item is list/tuple"""
    return isinstance(item, (list, tuple))


def generate(
    technique_promises,
    techniques,
    seeds: List[Text],
    system_conditions: List[Text],
    include_techniques: List[Text],
    exclude_techniques: List[Text],
    show_promises: bool,
    show_tactics: bool,
    nop_empty_provides: bool,
):

    nops = aep.tools.libs.data.nop_techniques(
        technique_promises, ["defense_evasion"], nop_empty_provides
    )
    removed = []
    for tat in techniques[:]:
        if tat in nops:
            removed.append(tat)
            techniques.remove(tat)

    if include_techniques:
        techniques.extend(include_techniques)
    if exclude_techniques:
        for exclude in exclude_techniques:
            try:
                techniques.remove(exclude)
            except ValueError:
                print(f"{sorted(exclude)} is not in the list of techniques used")

    sim = simulate(seeds, techniques, technique_promises, system_conditions)

    table = stages_table(
        sim,
        technique_promises,
        show_promises,
        show_tactics,
        join_text=None,
    )

    return table, sim, removed


@app.post("/upload_navigator_submit", response_class=HTMLResponse)
async def upload_navigator_submit(
    request: Request,
    navigator: UploadFile = File(...),
    args: argparse.Namespace = Depends(parse_args),
):

    try:
        layer = json.loads(await navigator.read())
    except json.decoder.JSONDecodeError:
        return error(request, "Unable to parse uploaded file as json", args.web_root)
    except Exception as e:
        logging.error(
            f"Error in aep-wep, server.py/upload_navigator_submit: {e}", args.web_root
        )
        return error(request, "Unknown server error", args.web_root)

    if "techniques" not in layer:
        return error(
            request, "Unable to find techniques in navigator layer", args.web_root
        )

    # Get unique technique IDs
    techniques = " ".join(list({tech["techniqueID"] for tech in layer["techniques"]}))

    # Redirect with technique IDs as argument
    return RedirectResponse(
        f"{args.web_root}/?technique_list={techniques}&navigator_info={navigator.filename}"
        + f" ({len(layer['techniques'])} techniques)",
        status_code=302,
    )


@app.get("/upload_navigator_form", response_class=HTMLResponse)
async def upload(request: Request, args: argparse.Namespace = Depends(parse_args)):
    return templates.TemplateResponse(
        "upload_navigator_form.html",
        {
            "request": request,
            "web_root": args.web_root,
        },
    )


@app.get("/", response_class=HTMLResponse)
async def index(
    request: Request,
    technique_list: Text = Query(""),
    seeds: List[Text] = Query([]),
    end_condition: Text = Query(None),
    include_techniques: List[Text] = Query([]),
    exclude_techniques: List[Text] = Query([]),
    show_promises: bool = Query(False),
    show_tactics: bool = Query(False),
    navigator_info: Text = None,
    nop_empty_provides: bool = Query(False),
    bundle_file: Path = Path(),
    args: argparse.Namespace = Depends(parse_args),
):

    include_tools = False
    system_conditions: List[Text] = []
    table = ""
    sim = None
    removed = []
    techniques: List[Text] = []
    all_sim_techniques = set()
    try:

        promises = aep.web.data.read_promise_description_file(
            Path(args.data_dir) / Path(args.promise_descriptions)
        )

        technique_promises, expand_map, _ = aep.web.data.read_technique_promises(
            Path(args.data_dir) / Path(args.technique_promises),
            Path(args.data_dir) / Path(args.promise_descriptions),
            Path(args.data_dir) / Path(args.conditions),
        )

    except FileNotFoundError:
        return error(
            request,
            "Unable to read config files. "
            + "Make sure --data-dir points to data directory in aep-data repository",
            args.web_root,
        )

    # Test for empty (default) Path
    if bundle_file != Path():
        techniques = aep.tools.libs.data.read_tech_bundle(
            args.data_dir / bundle_file,
            include_tool_techniques=include_tools,
        )

    if technique_list:
        techniques += [tech for tech in re.split(r"[, ]+", technique_list) if tech]

    if techniques:
        techniques = aep.tools.libs.data.preprocess_techniques(
            technique_promises, expand_map, techniques
        )

        table, sim, removed = generate(
            technique_promises,
            techniques,
            seeds,
            system_conditions,
            include_techniques,
            exclude_techniques,
            show_promises,
            show_tactics,
            nop_empty_provides,
        )

        for stage in sim.stages:
            all_sim_techniques.update(stage.techniques)

    all_techniques = sorted(
        (technique_promises[tech]["name"], tech) for tech in technique_promises
    )

    return templates.TemplateResponse(
        "generate.html",
        {
            "request": request,
            "seeds": seeds,
            "show_promises": show_promises,
            "navigator_info": navigator_info,
            "technique_list": technique_list.strip(),
            "show_tactics": show_tactics,
            "nop_empty_provides": nop_empty_provides,
            "end_condition": end_condition,
            "include_techniques": include_techniques,
            "exclude_techniques": exclude_techniques,
            "bundles": aep.web.data.get_bundles(args),
            "bundle_file": bundle_file,
            "technique_promises": technique_promises,
            "techniques": set(techniques),
            "all_sim_techniques": sorted(list(all_sim_techniques)),
            "all_techniques": all_techniques,
            "promises": sorted(list(promises)),
            "table": table,
            "removed": ", ".join(removed),
            "sim": sim,
            "web_root": args.web_root,
            "islist": islist,
        },
    )


def main() -> None:
    """Main API loop"""
    args = parse_args()

    uvicorn.run(
        "aep.web.server:app",
        host=args.host,
        port=args.port,
        log_level="info",
        reload=args.reload,
    )


if __name__ == "__main__":
    main()
