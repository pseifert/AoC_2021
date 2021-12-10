def get_example_input():
    with open("example.txt", "r") as example_file:
        return [line.strip('\n') for line in example_file.readlines()]


def get_task_input():
    with open("chunks.txt", "r") as task_file:
        return [line.strip('\n') for line in task_file.readlines()]


def find_wrong_brackets(chunk_list):
    opening_brackets = ["<", "(", "[", "{"]
    bracket_matching = {">": "<", ")": "(", "]": "[", "}": "{"}
    bracket_points = {">": 25137, ")": 3, "]": 57, "}": 1197}

    points = 0
    completion_scores = list()

    for chunks in chunk_list:
        open_brackets = list()
        brackets = list(chunks)
        for bracket in brackets:
            if bracket in opening_brackets:
                open_brackets.append(bracket)
            else:
                if bracket_matching.get(bracket) == open_brackets[-1]:
                    open_brackets = open_brackets[:-1]
                else:
                    points += bracket_points.get(bracket)
                    open_brackets = list()
                    break
        if open_brackets:
            completion_scores.append(append_missing_brackets(open_brackets, bracket_matching))
    print(points)
    middle_score = sorted(completion_scores)[int(len(completion_scores) / 2)]
    print(middle_score)


def append_missing_brackets(open_brackets):
    bracket_scores = {"<": 4, "(": 1, "[": 2, "{": 3}
    score = 0
    open_brackets.reverse()
    for bracket in open_brackets:
        score = (score * 5) + bracket_scores.get(bracket)
    return score


find_wrong_brackets(get_task_input())
