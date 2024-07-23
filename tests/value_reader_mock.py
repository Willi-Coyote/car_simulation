from car import Car
from field import Field
from move.move_forward import MoveForward
from move.rotate_left import RotateLeft
from move.rotate_right import RotateRight
from reader.value_reader import ValueReader, UserChoice, FinalChoice


class ScenarioOne(ValueReader):

    def __init__(self):
        self.call_count = 0

    def read_field(self) -> Field:
        return Field(10, 10)

    def read_car(self, field: Field) -> Car:
        return Car('A', 1, 2, 'N')

    def read_car_movements(self, car: Car) -> Car:
        car.movements = [MoveForward(), MoveForward(), RotateRight(), MoveForward(), MoveForward(),
                         MoveForward(), MoveForward(), RotateRight(), RotateRight(), RotateLeft()]
        return car

    def read_user_choice(self) -> UserChoice:
        if self.call_count == 0:
            self.call_count += 1
            return UserChoice.ADD_CAR
        elif self.call_count == 1:
            return UserChoice.RUN_SIMULATION

    def read_user_final_choice(self) -> FinalChoice:
        return FinalChoice.EXIT


class ScenarioTwo(ValueReader):

    def __init__(self):
        self.call_count = 0
        self.car_count = 0
        self.movement_count = 0

    def read_field(self) -> Field:
        return Field(10, 10)

    def read_car(self, field: Field) -> Car:
        if self.car_count == 0:
            self.car_count += 1
            return Car('A', 1, 2, 'N')
        elif self.car_count == 1:
            return Car('B', 7, 8, 'W')

    def read_car_movements(self, car: Car) -> Car:
        if self.movement_count == 0:
            self.movement_count += 1
            car.movements = [MoveForward(), MoveForward(), RotateRight(), MoveForward(),
                             MoveForward(), MoveForward(), MoveForward(), RotateRight(),
                             RotateRight(),
                             RotateLeft()]
        elif self.movement_count == 1:
            car.movements = [MoveForward(), MoveForward(), RotateLeft(), MoveForward(),
                             MoveForward(), MoveForward(), MoveForward(), MoveForward(),
                             MoveForward(), MoveForward()]
        return car

    def read_user_choice(self) -> UserChoice:
        if self.call_count < 2:
            self.call_count += 1
            return UserChoice.ADD_CAR
        elif self.call_count == 2:
            return UserChoice.RUN_SIMULATION

    def read_user_final_choice(self) -> FinalChoice:
        return FinalChoice.EXIT
