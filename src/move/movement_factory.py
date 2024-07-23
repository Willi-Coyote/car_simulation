from move.move_forward import MoveForward
from move.movement import Movement
from move.rotate_left import RotateLeft
from move.rotate_right import RotateRight


def parse_movement(movement_str) -> Movement:
    movement_map = {
        'L': RotateLeft(),
        'R': RotateRight(),
        'F': MoveForward()
    }
    return movement_map.get(movement_str, None)
