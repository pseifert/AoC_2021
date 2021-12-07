def get_task_input():
    with open("fish.txt", "r") as task_file:
        list_string = [str(fish) for fish in task_file.readlines()][0].split(",")
        return [int(fish) for fish in list_string]


def get_fish_count_list(fish_list):
    fish = list()
    for index in range(9):
        fish.append(fish_list.count(index))
    return fish


def calculate_growth(fish):
    for index, group in enumerate(fish):
        if index == 0:
            ready_fish = fish[0]
        else:
            fish[index-1] = fish[index]
    fish[6] = fish[6] + ready_fish
    fish[8] = ready_fish

    return sum(fish_count)


lantern_fish_example = [3, 4, 3, 1, 2]
lantern_fish = get_task_input()
fish_count = get_fish_count_list(lantern_fish)
for i in range(0, 256, 1):
    if i == 80:
        print(f"after 80 days: {lantern_fish}")
    lantern_fish = calculate_growth(fish_count)
print(f"after 256 days: {lantern_fish}")
