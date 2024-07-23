class CarPosition:
    def __init__(self, name, x, y, direction):
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction

    def __repr__(self):
        return f"- {self.name}, ({self.x},{self.y}) {self.direction}"


class SimulationResult:
    def __init__(self):
        self.events = []
        self.final_positions = []

    def add_event(self, event):
        self.events.append(event)

    def add_final_position(self, car_position):
        self.final_positions.append(car_position)

    def get_events(self):
        return self.events

    def get_final_positions(self):
        return self.final_positions
