import pytest

from toolkit import calculator


def test_addition():
    assert calculator.polish_calc("2 + 3") == 5

def test_operator_precedence():
    assert calculator.polish_calc("2 - 3 * 7") == -19

def test_division():
    assert calculator.polish_calc("5 / 2") == 2.5

def test_branches():
    assert calculator.polish_calc("(3 + 4) * 5") == 35

def test_division_by_zero():
    with pytest.raises(Exception):
        calculator.polish_calc("10 / 0.000")

def test_invalid_expression():
    with pytest.raises(Exception):
        calculator.polish_calc("2 +")

def test_invalid_symbol():
    with pytest.raises(Exception):
        calculator.polish_calc("2 + a")

def test_two_operators_in_row():
    with pytest.raises(Exception):
        calculator.polish_calc("2 + * 3")

def test_unclosed_branch():
    with pytest.raises(Exception):
        calculator.polish_calc("( 2 * 3")

def test_unmatched_branch():
    with pytest.raises(Exception):
        calculator.polish_calc("8 * 6 - 3) % 2")

def test_precedence_with_multiply_operations():
    assert calculator.polish_calc("10 + 20 / 5 * 2 - 3") == 15

def test_complex_branches():
    assert calculator.polish_calc("(10 + 5) * (8 - 3) / 5") == 15

def test_decimal_numbers():
    assert calculator.polish_calc("2.5 + 3.5") == 6.0

def test_negative_number():
    assert calculator.polish_calc("-5 + 10") == 5

def test_negative_numbers_multiplication():
    assert calculator.polish_calc("-5 * -4") == 20

def test_negative_number_in_parentheses():
    assert calculator.polish_calc("(-5 + 8) * 3") == 9

def test_complex_expression():
    expression = "(-10 + 4) * (3 + 2) / 5 + 17 % 4"
    assert calculator.polish_calc(expression) == -5
