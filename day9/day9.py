example = [list("2199943210"), list("3987894921"), list("9856789892"), list("8767896789"), list("9899965678")]

example = [[int(x) for x in inner] for inner in example]


def get_task_input():
    with open("matrix.txt", "r") as task_file:
        list_string = [list(str(numbers))[:-1] for numbers in task_file.readlines()]
        return [[int(x) for x in inner] for inner in list_string]


def get_local_mins(matrix):
    local_mins = list()
    for row_index, row in enumerate(matrix):
        for index, number in enumerate(row):
            adjasent_list = list()
            if number == 9: continue
            if row_index != 0:
                adjasent_list.append(matrix[row_index - 1][index])
            if index != 0:
                adjasent_list.append(row[index - 1])
            if index != len(row) - 1:
                adjasent_list.append(row[index + 1])
            if row_index != len(matrix) - 1:
                adjasent_list.append(matrix[row_index + 1][index])
            if min(adjasent_list) > number:
                local_mins.append(number)
    return local_mins


mins = get_local_mins(get_task_input())
print(sum([x + 1 for x in mins]))
