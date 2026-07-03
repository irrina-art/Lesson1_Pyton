
import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    (" Skypro", "Skypro"),
    ("  Hello world", "Hello world"),
    (" Python", "Python"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize("input_str, symbol, expected", [
  ("SkyPro", "k", True),
  ("Hello world", "w", True)
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.parametrize("input_str, symbol, expected", [
  ("SkyPro", "r", "SkyPo"),
  ("Pyton", "y", "Pton")
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    (None, TypeError)
])
def test_trim_negative(input_str, expected):
    with pytest.raises(expected):
        None(TypeError)


@pytest.mark.parametrize("input_str, symbol, expected", [
  (" ", "k", False),
  ("SkyPro", "@", False),
  ("SkyPro", "l", False)
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.parametrize("input_str, symbol, expected", [
  ("SkyPro", "", "SkyPro"),
  ("Pyton", "b", "Pyton")
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
