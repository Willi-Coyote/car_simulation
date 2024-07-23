import pytest

from reader.console_reader import ConsoleReader
from field import Field


def test_given_valid_input_when_parse_field_dimensions_then_correct_values_returned():
    reader = ConsoleReader()

    result = reader._parse_field_dimensions("10 5")

    assert result == (10, 5)


def test_given_negative_width_when_parse_field_dimensions_then_value_error_raised():
    reader = ConsoleReader()

    with pytest.raises(ValueError):
        reader._parse_field_dimensions("-1 5")


def test_given_negative_height_when_parse_field_dimensions_then_value_error_raised():
    reader = ConsoleReader()

    with pytest.raises(ValueError):
        reader._parse_field_dimensions("10 -5")


def test_given_incorrect_format_when_parse_field_dimensions_then_value_error_raised():
    reader = ConsoleReader()

    with pytest.raises(ValueError):
        reader._parse_field_dimensions("10")


def test_given_valid_input_when_parse_car_initial_position_then_correct_values_returned():
    field = Field(10, 10)
    reader = ConsoleReader()

    result = reader._parse_car_initial_position("2 3 N", field)

    assert result == (2, 3, 'N')


def test_given_out_of_bounds_position_when_parse_car_initial_position_then_value_error_raised():
    field = Field(10, 10)
    reader = ConsoleReader()

    with pytest.raises(ValueError):
        reader._parse_car_initial_position("11 3 N", field)


def test_given_invalid_direction_when_parse_car_initial_position_then_value_error_raised():
    field = Field(10, 10)
    reader = ConsoleReader()

    with pytest.raises(ValueError):
        reader._parse_car_initial_position("2 3 X", field)


def test_given_incorrect_format_when_parse_car_initial_position_then_value_error_raised():
    field = Field(10, 10)
    reader = ConsoleReader()

    with pytest.raises(ValueError):
        reader._parse_car_initial_position("2 3", field)


def test_given_valid_movements_when_validate_movements_then_no_error():
    reader = ConsoleReader()

    reader._validate_movements("LRF")


def test_given_invalid_movements_when_validate_movements_then_value_error_raised():
    reader = ConsoleReader()

    with pytest.raises(ValueError):
        reader._validate_movements("LRX")
