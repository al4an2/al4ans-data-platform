import random
from datetime import UTC, date, datetime, time, timedelta
from decimal import Decimal
from typing import get_args
from uuid import UUID

from datagen.models import Currency, Transaction

CURRENCIES: tuple[Currency, ...] = get_args(Currency)

ACCOUNTS = [f"acc-{i:04d}" for i in range(30)]
MERCHANTS = [
    "Starbucks",
    "Amazon",
    "Uber",
    "Netflix",
    "Lidl",
    "Shell",
    "IKEA",
    "Spotify",
]


def generate(count: int, seed: int, day: date) -> list[Transaction]:
    """Generate `count` deterministic transactions from `seed`."""
    day_start = datetime.combine(day, time.min, tzinfo=UTC)  # 00:00:00 UTC

    rng = random.Random(seed)

    transactions = []
    for _ in range(count):
        transactions.append(
            Transaction(
                tx_id=UUID(int=rng.getrandbits(128), version=4),
                account_id=rng.choice(ACCOUNTS),
                amount=Decimal(rng.randint(1, 100_000)) / 100,
                currency=rng.choice(CURRENCIES),
                merchant=rng.choice(MERCHANTS),
                created_at=day_start + timedelta(seconds=rng.randint(0, 86_399)),
            )
        )

    return sorted(transactions, key=lambda x: x.created_at)
