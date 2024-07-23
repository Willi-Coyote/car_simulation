from car import Car
from field import Field
from move.move_forward import MoveForward
from move.movement_factory import parse_movement
from move.rotate_left import RotateLeft
from move.rotate_right import RotateRight


def test_given_north_when_rotating_left_should_be_west():
    car = Car("A", 1, 1, "N")

    RotateLeft().execute(car, Field(10, 10))

    assert car.direction == "W"


def test_given_north_when_rotating_right_should_be_east():
    car = Car("A", 1, 1, "N")

    RotateRight().execute(car, Field(10, 10))

    assert car.direction == "E"


def test_given_north_when_moving_should_be_moved():
    car = Car("A", 1, 1, "N")

    MoveForward().execute(car, Field(10, 10))

    assert car.y == 2


def test_given_north_when_moving_should_not_be_moved_out_of_field():
    car = Car("A", 1, 10, "N")

    MoveForward().execute(car, Field(10, 10))

    assert car.y == 10


def test_parse_movement_left():
    movement = parse_movement("L")

    assert isinstance(movement, RotateLeft), "Expected RotateLeft instance"


def test_parse_movement_right():
    movement = parse_movement("R")

    assert isinstance(movement, RotateRight), "Expected RotateRight instance"


def test_parse_movement_forward():
    movement = parse_movement("F")

    assert isinstance(movement, MoveForward), "Expected MoveForward instance"


def test_parse_movement_invalid():
    movement = parse_movement("X")

    assert movement is None, "Expected None for invalid movement"
