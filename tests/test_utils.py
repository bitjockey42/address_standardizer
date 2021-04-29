"""Test utils"""
from address_standardizer import utils


def test_process_csv(mocker):
    mocker.patch(
        "address_standardizer.utils.read_csv",
        return_value=[
            {"primary": "ALLEY", "standard": "ALY", "common": "ALLEY"},
            {"primary": "", "standard": "", "common": "ally"},
            {"primary": "ANEX", "standard": "ANX", "common": "ANNEX"},
        ],
    )
    assert utils.process_csv("test.csv") == [
        {"primary": "ALLEY", "standard": "ALY", "common": "ALLEY"},
        {"primary": "ALLEY", "standard": "ALY", "common": "ALLY"},
        {"primary": "ANEX", "standard": "ANX", "common": "ANNEX"},
    ]


def test_process_csv_alt(mocker):
    mocker.patch(
        "address_standardizer.utils.read_csv",
        return_value=[
            {"common": "EXTENSION\n EXT\n EXTNSN", "standard": "EXT"},
            {"common": "ABACUS\n ABCS", "standard": "ABCS"},
        ],
    )
    assert utils.process_csv_alt("test.csv") == [
        {"common": "EXTENSION", "standard": "EXT"},
        {"common": "EXT", "standard": "EXT"},
        {"common": "EXTNSN", "standard": "EXT"},
        {"common": "ABACUS", "standard": "ABCS"},
        {"common": "ABCS", "standard": "ABCS"},
    ]


def test_generate_standards_map(mocker):
    mocker.patch(
        "address_standardizer.utils.process_csv",
        return_value=[
            {"primary": "ALLEY", "standard": "ALY", "common": "ALLEY"},
            {"primary": "ALLEY", "standard": "ALY", "common": "ALLY"},
            {"primary": "ANEX", "standard": "ANX", "common": "ANNEX"},
        ],
    )
    assert utils.generate_standards_map("test.csv") == {
        "ALY": ["ALLEY", "ALLY"],
        "ANX": ["ANNEX"],
    }


def test_generate_lookup_map(mocker):
    mocker.patch(
        "address_standardizer.utils.process_csv",
        return_value=[
            {"primary": "ALLEY", "standard": "ALY", "common": "ALLEY"},
            {"primary": "ALLEY", "standard": "ALY", "common": "ALLY"},
            {"primary": "ANEX", "standard": "ANX", "common": "ANNEX"},
        ],
    )
    assert utils.generate_lookup_map("test.csv") == {
        "ALLEY": "ALY",
        "ALLY": "ALY",
        "ANNEX": "ANX",
    }
