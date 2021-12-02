def get_example_input():
    with open("example.txt", "r") as example_file:
        return [str(depth) for depth in example_file.readlines()]


def get_task_input():
    with open("movement.txt", "r") as task_file:
        return [str(depth) for depth in task_file.readlines()]


def get_combination(combination_input):
    movement_list = list()
    for movement in combination_input:
        movement_data = movement.split(" ")
        movement_list.append((movement_data[0], int(movement_data[1])))
    return movement_list


def calculate_movement(combined_input):
    horizontal = 0
    depth = 0
    for action, points in combined_input:
        if action == "forward":
            horizontal += points
        elif action == "down":
            depth += points
        elif action == "up":
            depth -= points
    print(f"horizontal={horizontal}")
    print(f"depth={depth}")
    result = horizontal * depth
    print(f"result={result}")


def calculate_movement_with_aim(combined_input):
    horizontal = 0
    depth = 0
    aim = 0
    for action, points in combined_input:
        if action == "forward":
            horizontal += points
            depth += (aim*points)
        elif action == "down":
            aim += points
        elif action == "up":
            aim -= points
    print(f"horizontal={horizontal}")
    print(f"depth={depth}")
    result = horizontal * depth
    print(f"result={result}")

movement = get_combination(get_task_input())
calculate_movement(movement)
calculate_movement_with_aim(movement)
