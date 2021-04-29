"""Test utils"""
from address_standardizer import utils


def test_process_csv(mocker):
    mocker.patch("address_standardizer.utils.read_csv", return_value=[{"primary": "ALLEY", "standard": "ALY"}])
    assert utils.process_csv("test.csv") == [{"primary": "ALLEY", "standard": "ALY"}]
