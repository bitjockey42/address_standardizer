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
        ("street", "ST"),
        ("CALIFORNIA", "CA"),
        ("iLLinOis", "IL"),
        ("north", "N"),
        ("East", "E"),
        ("northeast", "NE"),
        ("Not found", None),
        ("", None),
        (None, None),
        ("academic", "ACDMC"),
        ("Atlantic", "ATL"),
        ("ALARM", "ALRM"),
    ],
)
def test_abbreviate(input_string, expected):
    assert abbreviate(input_string) == expected
