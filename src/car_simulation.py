from reader.console_reader import ConsoleReader
from simulation_result import SimulationResult, CarPosition
from reader.value_reader import ValueReader, UserChoice, FinalChoice


class CarSimulation:
    def __init__(self, value_reader: ValueReader = ConsoleReader()):
        self._value_reader = value_reader
        self._field = None
        self.cars = []
        self.simulation_result = SimulationResult()

    def start(self):
        print("Welcome to Auto Driving Car Simulation!")
        self._field = self._value_reader.read_field()
        while True:
            choice = self._value_reader.read_user_choice()
            if choice == UserChoice.ADD_CAR:
                self.add_car()
            elif choice == UserChoice.RUN_SIMULATION:
                self.run_simulation()
                final_choice = self._value_reader.read_user_final_choice()
                if final_choice == FinalChoice.START_OVER:
                    self.__init__()
                    self.start()
                elif final_choice == FinalChoice.EXIT:
                    print("Thank you for running the simulation. Goodbye!")
                    break

    def add_car(self):
        car = self._value_reader.read_car(self._field)
        self.cars.append(self._value_reader.read_car_movements(car))
        self.display_cars()

    def display_cars(self):
        print("Your current list of cars are:")
        for car in self.cars:
            movement_str = ''.join([str(m) for m in car.movements])
            print(f"{car}, {movement_str}")

    def run_simulation(self):
        steps = max(len(car.movements) for car in self.cars)
        for step in range(steps):
            positions = {}
            for car in self.cars:
                if step < len(car.movements) and car.movements[step]:
                    car.movements[step].execute(car, self._field)
                    if self.check_collision(car, positions, step):
                        return

        self.record_final_positions()

    def check_collision(self, car, positions, step):
        if (car.x, car.y) in positions:
            collision_event = f"- {positions[(car.x, car.y)]} collides with {car.name} at ({car.x},{car.y}) at step {step + 1}"
            self.simulation_result.add_event(collision_event)
            print(collision_event)
            collision_event = f"- {car.name} collides with {positions[(car.x, car.y)]} at ({car.x},{car.y}) at step {step + 1}"
            self.simulation_result.add_event(collision_event)
            print(collision_event)
            return True
        else:
            positions[(car.x, car.y)] = car.name
            return False

    def record_final_positions(self):
        result_event = "After simulation, the result is:\n"
        for car in self.cars:
            final_position = CarPosition(car.name, car.x, car.y, car.direction)
            result_event += f"- {final_position}\n"
            self.simulation_result.add_final_position(final_position)
        self.simulation_result.add_event(result_event)
        print(result_event)
