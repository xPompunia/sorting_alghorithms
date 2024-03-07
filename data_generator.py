from random import randint


def generate_random_data(length):
    if length < 1:
        raise ValueError("Length of the list must be at least 1")
    random_list = [randint(1, 100) for _ in range(length)]
    return random_list


def generate_A_shaped_array(length):
    if length < 3:
        raise ValueError("Length of the array must be at least 3")
    pivot = length // 2
    data = [randint(1, 100)]
    for i in range(1, pivot):
        data.append(data[-1] + randint(1, 10))
    for i in range(pivot, length):
        data.append(data[-1] - randint(1, 10))
    return data


def generate_constant_data(length):
    return length * [randint(1, 100)]


def generate_ascending_data(length):
    if length < 1:
        raise ValueError("Length of the list must be at least 1")

    random_list = [randint(1, 100) for _ in range(length)]
    sorted_list = sorted(random_list)
    return sorted_list


def generate_descending_data(length):
    if length < 1:
        raise ValueError("Length of the list must be at least 1")

    random_list = [randint(1, 100) for _ in range(length)]
    sorted_list = sorted(random_list, reverse=True)
    return sorted_list
