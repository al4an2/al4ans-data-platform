"""CLI entry point: generate a batch of synthetic transactions as JSONL.

Usage:
    uv run python -m datagen --count 1000 --seed 42 --date 2026-08-15
"""

import argparse
from datetime import UTC, date, datetime
from pathlib import Path

from datagen.generator import generate


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="datagen",
        description="Generate deterministic synthetic fintech transactions (JSONL).",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=1000,
        help="number of transactions (default: %(default)s)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="RNG seed; same seed = same data (default: %(default)s)",
    )
    parser.add_argument(
        "--date",
        dest="day",
        type=date.fromisoformat,
        default=None,
        help="business date YYYY-MM-DD (default: today, UTC)",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="output file (default: data/date=<date>/batch-<seed>.jsonl)",
    )
    args = parser.parse_args()

    day: date = args.day if args.day is not None else datetime.now(UTC).date()
    out: Path = (
        args.out
        if args.out is not None
        else Path("data") / f"date={day.isoformat()}" / f"batch-{args.seed}.jsonl"
    )

    transactions = generate(args.count, args.seed, day)

    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        for tx in transactions:
            f.write(tx.model_dump_json())
            f.write("\n")

    print(f"Wrote {len(transactions)} transactions for {day.isoformat()} to {out}")


if __name__ == "__main__":
    main()
