from car import Car
from move.movement import Movement


class RotateRight(Movement):
    def execute(self, car, field):
        current_index = Car.directions.index(car.direction)
        car.direction = Car.directions[(current_index + 1) % 4]

    def __str__(self):
        return "R"
