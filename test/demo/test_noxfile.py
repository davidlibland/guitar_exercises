"""
Tests that noxfile requirements are actually honored.
"""
import pydantic
from packaging.version import Version

# avoid annoying error
import guitar_exercises  # pylint: disable=unused-import


def test_pydantic_version():
    """Ensure that composite constraint on pydantic is satisfied."""
    assert Version(pydantic.version.VERSION) < Version(
        "2.5.0"
    ), "pydantic version constraint failed"
