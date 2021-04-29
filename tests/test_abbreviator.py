"""Test abbreviations"""
import pytest

from address_standardizer.abbreviator import abbreviate


@pytest.mark.parametrize(
    "input_string,expected",
    [
        ("alley", "ALY"),
        ("aParTment", "APT"),
        ("space", "SPC"),
        ("front", "FRNT"),
        ("CALIFORNIA", "CA"),
        ("iLLinOis", "IL"),
        ("north", "N"),
        ("East", "E"),
        ("northeast", "NE"),
    ],
)
def test_abbreviate(input_string, expected):
    assert abbreviate(input_string) == expected


def test_abbreviate_error():
    with pytest.raises(ValueError):
        abbreviate("")
