def get_example_input():
    with open("example.txt", "r") as example_file:
        return [str(depth) for depth in example_file.readlines()]


def get_task_input():
    with open("binaries.txt", "r") as task_file:
        return [str(depth) for depth in task_file.readlines()]


def get_codes(codes):
    gamma_code = list()
    epsilon_code = list()
    for i in range(len(codes[0])-1):
        bits = [bit[i] for bit in codes]
        gamma_code.append("1" if bits.count("1") > bits.count("0") else "0")
        epsilon_code.append("1" if bits.count("0") > bits.count("1") else "0")
    gamma = int("".join(gamma_code), 2)
    epsilon = int("".join(epsilon_code), 2)
    print(f"Gamma: {gamma}")
    print(f"Epsilon: {epsilon}")
    print(f"Result = {gamma*epsilon}")


def get_oxygen_generator_rating(codes):
    final_code = codes
    for i in range(len(final_code[0])-1):
        if len(final_code) == 1:
            break
        bits = [bit[i] for bit in final_code]
        if bits.count("1") >= bits.count("0"):
            indices = [index for index, bit in enumerate(bits) if bit == "1"]
            final_code = [final_code[index] for index in indices]
        else:
            indices = [index for index, bit in enumerate(bits) if bit == "0"]
            final_code = [final_code[index] for index in indices]
    final_code = final_code[0][:-1]
    oxygen = int("".join(final_code), 2)
    print(f"oxygen: {final_code} = {oxygen}")
    return oxygen


def get_co2_generator_rating(codes):
    final_code = codes
    for i in range(len(final_code[0])-1):
        if len(final_code) == 1:
            break
        bits = [bit[i] for bit in final_code]
        if bits.count("0") <= bits.count("1"):
            indices = [index for index, bit in enumerate(bits) if bit == "0"]
            final_code = [final_code[index] for index in indices]
        else:
            indices = [index for index, bit in enumerate(bits) if bit == "1"]
            final_code = [final_code[index] for index in indices]
    final_code = final_code[0]
    co2 = int("".join(final_code), 2)
    print(f"co2: {final_code} = {co2}")
    return co2


def split_code(input_list):
    return [list(code) for code in input_list]


splitted_code_list = split_code(get_task_input())
get_codes(splitted_code_list)
oxygen_value = get_oxygen_generator_rating(splitted_code_list)
co2_value = get_co2_generator_rating(splitted_code_list)
print(f"result: {oxygen_value*co2_value}")