"""Test abbreviations"""
import pytest

from address_standardizer.abbreviator import abbreviate, abbreviate_business, abbreviate_state


@pytest.mark.parametrize(
    "input_string,expected",
    [
        ("alley", "ALY"),
        ("aParTment", "APT"),
        ("space", "SPC"),
        ("front", "FRNT"),
        ("street", "ST"),
        ("north", "N"),
        ("East", "E"),
        ("northeast", "NE"),
        ("Not found", None),
        ("", None),
        (None, None),
    ],
)
def test_abbreviate(input_string, expected):
    assert abbreviate(input_string) == expected


@pytest.mark.parametrize(
    "input_string,expected",
    [
        ("atlantic", "ATL"),
        ("flower", "FLWR"),
        ("gallery", "GLLRY"),
        ("lmao no", None),
        ("", None),
        (None, None),
    ],
)
def test_abbreviate_business(input_string, expected):
    assert abbreviate_business(input_string) == expected


@pytest.mark.parametrize(
    "input_string,expected",
    [
        ("california", "CA"),
        ("illinois", "IL"),
        ("lmao no", None),
        ("", None),
        (None, None),
    ],
)
def test_abbreviate_state(input_string, expected):
    assert abbreviate_state(input_string) == expected
