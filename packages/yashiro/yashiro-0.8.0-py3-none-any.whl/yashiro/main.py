import argparse
import json
import os
from typing import Any, Dict, cast

import jinja2
import tomlkit

from yashiro import __version__


class Parser:
    __slots__ = ["template", "mapping"]

    def __init__(self, args: argparse.Namespace):
        extra: Dict[str, Any] = {}
        if args.strict:
            extra["undefined"] = jinja2.StrictUndefined
        with open(args.template) as file:
            self.template = jinja2.Template(file.read(), **extra)
        self.mapping = dict(os.environ)
        json_path = args.json
        if json_path is not None:
            with open(json_path) as file:
                self.mapping.update(json.load(file))
        toml_path = args.toml
        if toml_path is not None:
            with open(toml_path) as file:
                info = cast(Dict[str, Any], tomlkit.parse(file.read()))
                payload = info["tool"]["yashiro"]
                self.mapping.update(payload)

    def __call__(self) -> str:
        return self.template.render(self.mapping)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="yashiro",
        description="A utility to manage testing and migrating a database",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
        help="Print the version and exit",
    )
    parser.add_argument("-j", "--json", help="The path to the json file")
    parser.add_argument("-o", "--toml", help="The path to the toml file")
    parser.add_argument(
        "-s", "--strict", action="store_true", help="Disallow missing arguments"
    )
    parser.add_argument(
        "-t", "--template", required=True, help="The path to the template"
    )

    return parser.parse_args()


def get_output() -> str:
    args = parse_args()
    parser = Parser(args)
    return parser()


def write_output() -> None:
    print(get_output())
