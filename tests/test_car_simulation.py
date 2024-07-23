from car_simulation import CarSimulation
from value_reader_mock import ScenarioOne, ScenarioTwo


def test_simulation_scenario_one():
    simulation = CarSimulation(ScenarioOne())

    simulation.start()

    events = simulation.simulation_result.get_events()
    final_positions = simulation.simulation_result.get_final_positions()
    assert simulation.cars.__len__() == 1
    assert simulation._field.width == 10
    assert simulation._field.height == 10
    assert len(events) > 0
    assert len(final_positions) == 1
    assert final_positions[0].name == "A"
    assert final_positions[0].x == 5
    assert final_positions[0].y == 4
    assert final_positions[0].direction == "S"


def test_simulation_scenario_two():
    simulation = CarSimulation(ScenarioTwo())

    simulation.start()

    events = simulation.simulation_result.get_events()
    assert simulation.cars.__len__() == 2
    assert simulation._field.width == 10
    assert simulation._field.height == 10
    assert len(events) > 0
    assert events[0] == "- A collides with B at (5,4) at step 7"
    assert events[1] == "- B collides with A at (5,4) at step 7"
