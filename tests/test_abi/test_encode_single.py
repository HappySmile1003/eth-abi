import pytest

from eth_abi.abi import encode_single

from ..common.unit import CORRECT_SINGLE_ENCODINGS


@pytest.mark.parametrize('typ,python_value,expected', CORRECT_SINGLE_ENCODINGS)
def test_encode_single(typ, python_value, expected):
    actual = encode_single(typ, python_value)
    assert actual == expected
