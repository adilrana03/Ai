from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from ops_ingest.parse import IngestError, load_records


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Ingest JSON/CSV operations files into validated tickets."
    )
    parser.add_argument("path", type=Path, help="Path to a .json or .csv file")
    args = parser.parse_args(argv)

    try:
        tickets = load_records(args.path)
    except FileNotFoundError:
        print(f"error: file not found: {args.path}", file=sys.stderr)
        return 2
    except IngestError as exc:
        print(f"error: {exc}", file=sys.stderr)
        for failure in exc.failures:
            print(f"  - {failure}", file=sys.stderr)
        return 1

    print(json.dumps([ticket.model_dump(mode="json") for ticket in tickets], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
