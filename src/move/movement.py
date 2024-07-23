from typing import Protocol


class Movement(Protocol):
    def execute(self, car, field):
        pass

    def __str__(self):
        pass
