"""Test standardizer"""
import pytest

from address_standardizer.standardizer import standardize


@pytest.mark.parametrize(
    "address,expected",
    [
        ("1234 Main Street", "1234 MAIN ST"),
        ("1234 Main St.", "1234 MAIN ST"),
    ],
)
def test_standardize(address, expected):
    assert standardize(address) == expected
