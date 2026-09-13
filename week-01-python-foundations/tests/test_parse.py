from pathlib import Path

import pytest

from ops_ingest.models import OpsTicket, TicketStatus
from ops_ingest.parse import IngestError, load_records

FIXTURES = Path(__file__).resolve().parents[1] / "data"


def test_json_ingest_validates_two_tickets() -> None:
    tickets = load_records(FIXTURES / "tickets.json")
    assert len(tickets) == 2
    assert tickets[0].ticket_id == "OPS-1042"
    assert tickets[0].status is TicketStatus.open


def test_csv_ingest_allows_blank_owner() -> None:
    tickets = load_records(FIXTURES / "tickets.csv")
    assert tickets[1].owner is None
    assert tickets[1].hours == 0


def test_rejects_unknown_status(tmp_path: Path) -> None:
    path = tmp_path / "bad.json"
    path.write_text('[{"ticket_id":"x","customer":"a","hours":1,"status":"nope","opened_on":"2026-01-01"}]')
    with pytest.raises(IngestError):
        load_records(path)


def test_rejects_negative_hours() -> None:
    with pytest.raises(Exception):
        OpsTicket(
            ticket_id="ops-1",
            customer="a",
            hours=-1,
            status="open",
            opened_on="2026-01-01",
        )


def test_ticket_id_cannot_contain_spaces() -> None:
    with pytest.raises(Exception):
        OpsTicket(
            ticket_id="ops 1",
            customer="a",
            hours=1,
            status="open",
            opened_on="2026-01-01",
        )
