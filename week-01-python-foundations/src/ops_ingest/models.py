from datetime import date
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field, field_validator


class TicketStatus(str, Enum):
    open = "open"
    in_progress = "in_progress"
    blocked = "blocked"
    done = "done"


class OpsTicket(BaseModel):
    """One operations ticket after validation.

    Real FDE work starts here: refuse garbage data before any model sees it.
    """

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    ticket_id: str = Field(min_length=1, max_length=64)
    customer: str = Field(min_length=1, max_length=120)
    hours: float = Field(ge=0, le=1000)
    status: TicketStatus
    opened_on: date
    owner: str | None = None

    @field_validator("ticket_id")
    @classmethod
    def ticket_id_is_stable(cls, value: str) -> str:
        if " " in value:
            raise ValueError("ticket_id cannot contain spaces")
        return value.upper()
