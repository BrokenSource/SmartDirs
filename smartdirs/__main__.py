import argparse
import json
from pathlib import Path

from smartdirs import SmartDirs


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--pkg",
        type=Path,
        default=Path(__file__).parent,
        help="Package source directory",
    )

    parser.add_argument(
        "--app",
        default=str(__package__),
        help="Application name",
    )

    parser.add_argument(
        "--org",
        default="tremeschin",
        help="Organization name",
    )

    parser.add_argument(
        "--url",
        default="com",
        help="Top level domain",
    )

    parser.add_argument(
        "--schema",
        action="store_true",
        help="Print the schema"
    )

    args = parser.parse_args()

    dirs = SmartDirs(
        pkg=args.pkg,
        app=args.app,
        org=args.org,
        url=args.url,
    )

    if args.schema:
        print(json.dumps(
            dirs.model_json_schema(mode="serialization"),
            separators=(',', ':'),
            ensure_ascii=False,
            indent=None,
        ))
    else:
        print(dirs.model_dump_json())


if __name__ == "__main__":
    main()
