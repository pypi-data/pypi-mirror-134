import argparse
from functools import lru_cache

from aep.tools import config

# parse_args() is executed the first time and later the cached result
# is used. In this way, we use to configure settings in API endpoints


@lru_cache()
def parse_args() -> argparse.Namespace:
    """Parse the command line arguments"""

    parser = config.common_args("AEP WEB")

    parser.add_argument(
        "--port", type=int, default=3000, help="API port to listen on (default=3000)"
    )
    parser.add_argument(
        "--reload",
        action="store_true",
        help="Reload web server on file change (dev mode)",
    )

    parser.add_argument(
        "--web-root",
        default="",
        help="Web root (default='/'). Change if you have a reverse proxy and serve under another path",
    )
    parser.add_argument(
        "--host",
        dest="host",
        default="127.0.0.1",
        help="Host interface (default=127.0.0.1)",
    )

    return config.handle_args(parser, "web")
