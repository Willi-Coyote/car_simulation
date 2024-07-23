from car import Car
from field import Field
from move.movement import Movement


class MoveForward(Movement):
    def execute(self, car: Car, field: Field):
        old_x, old_y = car.x, car.y
        if car.direction == 'N':
            car.y += 1
        elif car.direction == 'E':
            car.x += 1
        elif car.direction == 'S':
            car.y -= 1
        elif car.direction == 'W':
            car.x -= 1
        if field.is_outside(car.x, car.y):
            car.x, car.y = old_x, old_y

    def __str__(self):
        return "F"
