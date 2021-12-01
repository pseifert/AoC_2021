import itertools


def get_example_input():
    with open("example.txt", "r") as example_file:
        return [int(depth) for depth in example_file.readlines()]


def get_task_input():
    with open("depth.txt", "r") as task_file:
        return [int(depth) for depth in task_file.readlines()]


def get_depth_increase():
    print("Task 1")
    input_task_1 = get_task_input()
    print([y > x for x, y in create_comparison_pairs(input_task_1)].count(True))


def get_depth_window_increase():
    print("Task 2")
    input_task_1 = get_task_input()
    window_list = create_window(input_task_1)
    window_sum = [x+y+z for x, y, z in window_list]
    print([y > x for x, y in create_comparison_pairs(window_sum)].count(True))


def create_comparison_pairs(input_list):
    x, y = itertools.tee(input_list)
    next(y, None)
    return zip(x, y)


def create_window(input_list):
    x, y, z = itertools.tee(input_list, 3)
    next(y, None)
    next(z, None)
    next(z, None)
    return zip(x, y, z)


get_depth_increase()
get_depth_window_increase()
