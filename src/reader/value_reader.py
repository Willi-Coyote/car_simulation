from enum import Enum
from typing import Protocol

from car import Car
from field import Field


class UserChoice(Enum):
    ADD_CAR = 1
    RUN_SIMULATION = 2


class FinalChoice(Enum):
    START_OVER = 1
    EXIT = 2


class ValueReader(Protocol):
    def read_field(self) -> Field:
        pass

    def read_car(self, field: Field) -> Car:
        pass

    def read_car_movements(self, car: Car) -> Car:
        pass

    def read_user_choice(self) -> UserChoice:
        pass

    def read_user_final_choice(self) -> FinalChoice:
        pass
