from __future__ import annotations

import csv
import json
from pathlib import Path

from pydantic import ValidationError

from ops_ingest.models import OpsTicket


class IngestError(Exception):
    def __init__(self, path: Path, failures: list[str]) -> None:
        self.path = path
        self.failures = failures
        super().__init__(f"{len(failures)} invalid row(s) in {path}")


def load_records(path: Path) -> list[OpsTicket]:
    suffix = path.suffix.lower()
    if suffix == ".json":
        raw_rows = _load_json(path)
    elif suffix == ".csv":
        raw_rows = _load_csv(path)
    else:
        raise IngestError(path, [f"unsupported file type: {suffix}"])

    tickets: list[OpsTicket] = []
    failures: list[str] = []
    for index, row in enumerate(raw_rows, start=1):
        try:
            tickets.append(OpsTicket.model_validate(row))
        except ValidationError as exc:
            failures.append(f"row {index}: {exc.errors()[0]['msg']}")

    if failures:
        raise IngestError(path, failures)
    return tickets


def _load_json(path: Path) -> list[dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, dict):
        payload = payload.get("tickets", payload)
    if not isinstance(payload, list):
        raise IngestError(path, ["JSON must be a list or an object with tickets[]"])
    return payload


def _load_csv(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))
