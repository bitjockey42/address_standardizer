"""Test utils"""
from address_standardizer import utils


def test_process_csv(mocker):
    mocker.patch(
        "address_standardizer.utils.read_csv",
        return_value=[
            {"primary": "ALLEY", "standard": "ALY", "common": "ALLEY"},
            {"primary": "", "standard": "", "common": "ALLY"},
            {"primary": "ANEX", "standard": "ANX", "common": "ANNEX"},
        ],
    )
    assert utils.process_csv("test.csv") == [
        {"primary": "ALLEY", "standard": "ALY", "common": "ALLEY"},
        {"primary": "ALLEY", "standard": "ALY", "common": "ALLY"},
        {"primary": "ANEX", "standard": "ANX", "common": "ANNEX"},
    ]


def test_generate_standards_map(mocker):
    mocker.patch(
        "address_standardizer.utils.process_csv",
        return_value=[
            {"primary": "ALLEY", "standard": "ALY", "common": "ALLEY"},
            {"primary": "ALLEY", "standard": "ALY", "common": "ALLY"},
            {"primary": "ANEX", "standard": "ANX", "common": "ANNEX"},
        ]
    )
    assert utils.generate_standards_map("test.csv") == {
        "ALY": ["ALLEY", "ALLY"],
        "ANX": ["ANNEX"],
    }
