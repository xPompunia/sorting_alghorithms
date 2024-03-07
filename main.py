from time import time
from random import randint
import matplotlib.pyplot as plt

times = []


def timer(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time() - start
        times.append(end)
        return result
    return wrapper


def generate_random_data(length):
    if length < 1:
        raise ValueError("Length of the list must be at least 1")
    random_list = [randint(1, 10*6) for _ in range(length)]
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

    random_list = [randint(1, 10*6) for _ in range(length)]
    sorted_list = sorted(random_list)
    return sorted_list


def generate_descending_data(length):
    if length < 1:
        raise ValueError("Length of the list must be at least 1")

    random_list = [randint(1, 10*6) for _ in range(length)]
    sorted_list = sorted(random_list,reverse=True)
    return sorted_list


@timer
def selection_sort(tab):
    n = len(tab)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if tab[j] < tab[min_idx]:
                min_idx = j
        tab[i], tab[min_idx] = tab[min_idx], tab[i]
    return tab


data_num = [10, 100, 500, 1000, 5000]
for num in data_num:
    random_data = generate_random_data(num)
    selection_sort(random_data)
print(times)

times = []
for num in data_num:
    a_data = generate_A_shaped_array(num)
    selection_sort(a_data)

print(times)

# fig, ax = plt.subplots()
# ax.plot(data_num, times)
# ax.set_title("Selection Sort time with different number of data")
# ax.set_xlabel('Number of data')
# ax.set_ylabel('Seconds (s)')
# plt.show()
