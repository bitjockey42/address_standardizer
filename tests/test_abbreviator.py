"""Test abbreviations"""
from address_standardizer.abbreviator import abbreviate


def test_abbreviate():
    assert abbreviate("alley") == "ALY"
    assert abbreviate("aPartMent") == "APT"
    assert abbreviate("SPACE") == "SPC"
    assert abbreviate("front") == "FRNT"
