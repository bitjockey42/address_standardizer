"""Test abbreviations"""
from address_standardizer.abbreviator import abbreviate


def test_abbreviate():
    assert abbreviate("alley") == "ALY"