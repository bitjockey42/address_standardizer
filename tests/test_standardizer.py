"""Test standardizer"""
import pytest

from address_standardizer.standardizer import standardize, standardize_business


@pytest.mark.parametrize(
    "address,expected",
    [
        ("1234 Main Street", "1234 MAIN ST"),
        ("1234 Main St.", "1234 MAIN ST"),
        ("N. Glenview Road", "N GLENVIEW RD"),
        ("room 1", "RM 1"),
        ("42 1/2 Main Street", "42 1/2 MAIN ST"),
        ("", ""),
        (None, ""),
    ],
)
def test_standardize(address, expected):
    assert standardize(address) == expected


@pytest.mark.parametrize(
    "business,expected",
    [
        ("atlantic media", "ATL MEDIA"),
        ("", ""),
        (None, ""),
    ],
)
def test_standardize_business(business, expected):
    assert standardize_business(business) == expected
