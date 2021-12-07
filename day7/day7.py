import numpy as np

example = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def get_task_input():
    with open("positions.txt", "r") as task_file:
        list_string = [str(position) for position in task_file.readlines()][0].split(",")
        return [int(position) for position in list_string]


def get_lowest_fuel_consumption_1(submarine_list):
    movement_consumption = {}
    for horizontal_position in range(0, max(submarine_list), 1):
        fuel = 0
        for submarine in submarine_list:
            fuel = fuel + abs(submarine-horizontal_position)
        movement_consumption[horizontal_position] = fuel
    best_position = min(movement_consumption, key=movement_consumption.get)
    return movement_consumption[best_position]


def get_lowest_fuel_consumption_2(submarine_list):
    movement_consumption = {}
    for horizontal_position in range(0, max(submarine_list), 1):
        fuel = 0
        for submarine in submarine_list:
            consumption = list(np.arange(1, abs(submarine-horizontal_position)+1, 1))
            fuel = fuel + sum(consumption)
        movement_consumption[horizontal_position] = fuel
    best_position = min(movement_consumption, key=movement_consumption.get)
    return movement_consumption[best_position]


print(f"Task 1: {get_lowest_fuel_consumption_1(get_task_input())}")
print(f"Task 2: {get_lowest_fuel_consumption_2(get_task_input())}")
