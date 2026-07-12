"""Smoke test proving the toolchain (uv + pytest + src layout) is wired up."""

from datagen import __version__


def test_package_is_importable() -> None:
    assert __version__ == "0.1.0"
