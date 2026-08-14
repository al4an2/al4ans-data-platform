from datetime import date

from datagen.generator import generate

DAY = date(2026, 1, 15)


def test_same_seed_same_output() -> None:
    assert generate(100, seed=42, day=DAY) == generate(100, seed=42, day=DAY)


def test_different_seed_different_output() -> None:
    assert generate(100, seed=42, day=DAY) != generate(100, seed=43, day=DAY)


def test_count() -> None:
    assert len(generate(7, seed=1, day=DAY)) == 7
