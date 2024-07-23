from car import Car
from field import Field
from move.movement_factory import parse_movement
from reader.value_reader import ValueReader, UserChoice, FinalChoice


class ConsoleReader(ValueReader):
    def __init__(self, input_func=input):
        self.input = input_func

    def read_field(self) -> Field:
        while True:
            try:
                user_input = self.input("Please enter the width and height of the simulation field in x y format: ")
                width, height = self._parse_field_dimensions(user_input)
                print(f"You have created a field of {width} x {height}.")
                return Field(width, height)
            except ValueError:
                print("Please enter positive integers for width and height.")

    def read_car(self, field: Field) -> Car:
        car_name = self.input("Please enter the name of the car: ").strip()
        while True:
            try:
                user_input = self.input(f"Please enter initial position of car {car_name} in 'x y direction' format: ")
                x, y, direction = self._parse_car_initial_position(user_input, field)
                return Car(car_name, x, y, direction)
            except ValueError:
                print(f"Invalid position or direction. Position must be within the field '{field}' and direction 'N' (north), 'S' (south), 'W' (west) or 'E' (east).")

    def read_car_movements(self, car: Car) -> Car:
        while True:
            try:
                movement_str = self.input(f"Please enter the movements for car {car.name}: ").strip().upper()
                self._validate_movements(movement_str)
                car.movements = [parse_movement(m) for m in movement_str]
                return car
            except ValueError:
                print("Invalid movement commands. Please enter a string containing only 'L', 'R', or 'F'.")

    def read_user_choice(self) -> UserChoice:
        while True:
            try:
                print("Please choose from the following options:")
                print("[1] Add a car to field")
                print("[2] Run simulation")
                choice_str = self.input().strip()
                choice = int(choice_str)
                return UserChoice(choice)
            except (ValueError, KeyError):
                print("Oops, the option you selected is not available. Please enter 1 or 2.")

    def read_user_final_choice(self) -> FinalChoice:
        while True:
            try:
                print("Please choose from the following options:")
                print("[1] Start over")
                print("[2] Exit")
                choice_str = self.input().strip()
                choice = int(choice_str)
                return FinalChoice(choice)
            except (ValueError, KeyError):
                print("Oops, the option you selected is not available. Please enter 1 or 2.")

    def _parse_field_dimensions(self, input_str: str):
        parts = input_str.split()
        if len(parts) != 2:
            raise ValueError("Input must be in 'x y' format.")
        width, height = map(int, parts)
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        return width, height

    def _parse_car_initial_position(self, input_str: str, field: Field):
        parts = input_str.split()
        if len(parts) != 3:
            raise ValueError("Input must be in 'x y direction' format.")
        x, y = int(parts[0]), int(parts[1])
        direction = parts[2]
        if direction not in 'NSWE' or field.is_outside(x, y):
            raise ValueError("Invalid position or direction.")
        return x, y, direction

    def _validate_movements(self, movement_str: str):
        if not all(m in 'LRF' for m in movement_str):
            raise ValueError("Movement commands must contain only 'L', 'R', or 'F'.")
