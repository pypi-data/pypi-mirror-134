from functools import lru_cache
from glob import glob
from pathlib import Path
from typing import Dict, List, Text, Tuple

import aep.tools.libs.data


def get_bundles(args) -> List[Text]:
    bundle_list = []
    for bundle_type in ("incident", "threatactors"):
        for bundle in glob(f"{args.data_dir}/{bundle_type}/*"):
            bundle_list.append(Path(bundle_type) / Path(bundle).name)

    return sorted(bundle_list)


@lru_cache()
def read_promise_description_file(filename: Path) -> List:
    return aep.tools.libs.data.read_promise_description_file(open(Path(filename)))


@lru_cache()
def read_technique_promises(
    tech_promises_file: Path, promise_descriptions_file: Path, conditions_file: Path
) -> Tuple[Dict, Dict, bool]:

    return aep.tools.libs.data.read_technique_promises(
        tech_promises_file, promise_descriptions_file, conditions_file
    )
