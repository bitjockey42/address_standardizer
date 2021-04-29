"""Test abbreviations"""
import pytest

from address_standardizer.abbreviator import abbreviate


def test_abbreviate():
    assert abbreviate("alley") == "ALY"
    assert abbreviate("aPartMent") == "APT"
    assert abbreviate("SPACE") == "SPC"
    assert abbreviate("front") == "FRNT"


def test_abbreviate_error():
    with pytest.raises(ValueError):
        abbreviate("")
