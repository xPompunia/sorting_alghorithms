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
    random_list = [randint(1, 10 * 6) for _ in range(length)]
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

    random_list = [randint(1, 10 * 6) for _ in range(length)]
    sorted_list = sorted(random_list)
    return sorted_list


def generate_descending_data(length):
    if length < 1:
        raise ValueError("Length of the list must be at least 1")

    random_list = [randint(1, 10 * 6) for _ in range(length)]
    sorted_list = sorted(random_list, reverse=True)
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


def heap_transform(tab, n, i):
    max_element = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and tab[max_element] < tab[left]:
        max_element = left
    if right < n and tab[max_element] < tab[right]:
        max_element = right
    if max_element != i:
        tab[i], tab[max_element] = tab[max_element], tab[i]

        heap_transform(tab, n, max_element)


@timer
def heap_sort(tab):
    print(tab)
    heap_transform(tab,  len(tab), 0)
    print(tab)
    for i in range(len(tab) - 1, -1, -1):
        tab[i], tab[0] = tab[0], tab[i]
        heap_transform(tab, i, 0)
    print(tab)



def partition(tab, p, r)
    x = tab[r]
    i, j = p, r
    while True:
        while i < len(tab) and tab[i] < x:
            i += 1
        while j >= 0 and tab[j] > x:
            j -= 1
        if i < j:
            tab[i], tab[j] = tab[j], tab[i]
            i += 1
            j-= 1
        else:
            return j

@timer
def quick_sort(tab, n):
    pass



heap_sort([4, 10, 3, 5, 1])




# data_num = [10, 100, 500, 1000, 5000]
# for num in data_num:
#     random_data = generate_random_data(num)
#     selection_sort(random_data)
# print(times)
#
# times = []
# for num in data_num:
#     a_data = generate_A_shaped_array(num)
#     selection_sort(a_data)
#
# print(times)

# fig, ax = plt.subplots()
# ax.plot(data_num, times)
# ax.set_title("Selection Sort time with different number of data")
# ax.set_xlabel('Number of data')
# ax.set_ylabel('Seconds (s)')
# plt.show()
