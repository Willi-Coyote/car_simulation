from typing import List

from move.movement import Movement


class Car:
    directions = ['N', 'E', 'S', 'W']

    def __init__(self, name, x, y, direction):
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.movements: List[Movement] = []

    def __str__(self):
        return f"{self.name}, ({self.x},{self.y}) {self.direction}"
