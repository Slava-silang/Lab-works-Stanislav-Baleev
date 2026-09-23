import pytest
from toolkit import converter


def test_under_absolute_zero_C():
    with pytest.raises(ValueError):
        converter.converter(-290, "C", "k")


def test_under_absolute_zero_K():
    with pytest.raises(ValueError):
        converter.converter(-10, "K", "C")


def test_under_absolute_zero_F():
    with pytest.raises(ValueError):
        converter.converter(-460, "F", "f")


def test_unmatched_units():
    with pytest.raises(ValueError):
        converter.converter(15, "km", "kg")


def test_unknown_unit():
    with pytest.raises(SyntaxError):
        converter.converter(21, "km", "miles")


def test_convert_to_the_same_unit():
    assert converter.converter(10, "f", "f") == 10.0


def test_float_unit():
    assert abs(converter.converter(3.87, "f", "k") - 257.5222222) < 0.0001
