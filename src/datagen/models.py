from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, Field
from pydantic.types import UUID4, AwareDatetime

Currency = Literal[
    "USD",
    "EUR",
]


class Transaction(BaseModel):
    tx_id: UUID4
    account_id: str = Field(min_length=1)
    amount: Decimal = Field(gt=0, decimal_places=2)
    currency: Currency
    merchant: str = Field(min_length=1)
    created_at: AwareDatetime
