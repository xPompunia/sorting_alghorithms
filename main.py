from time import time
import matplotlib.pyplot as plt
from data_generator import *
import sys

sys.setrecursionlimit(100000)


def timer(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time() - start
        times.append(end)
        return result

    return wrapper

# -----------------------------------------


# SELECTION SORT
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


# -----------------------------------------


# HEAP SORT
def heap_transform(tab, n, i):
    max_element = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and tab[max_element] < tab[left]:
        max_element = left
    if right < n and tab[max_element] < tab[right]:
        max_element = right
    if max_element != i:
        tab[i], tab[max_element] = tab[max_element], tab[i]

        heap_transform(tab, n, max_element)


@timer
def heap_sort(tab):
    n = len(tab)
    for i in range(n // 2 - 1, -1, -1):
        heap_transform(tab, n, i)
    for i in range(n - 1, 0, -1):
        tab[i], tab[0] = tab[0], tab[i]
        heap_transform(tab, i, 0)
    return tab


# -----------------------------------------


# QUICK SORT
def partition(tab, p, r, pivot):
    if pivot == 'l':
        x = tab[p]
    else:
        x = tab[randint(p, r)]
    i, j = p, r
    while True:
        while i <= j and tab[i] < x:
            i += 1
        while j >= i and tab[j] > x:
            j -= 1
        if i < j:
            tab[i], tab[j] = tab[j], tab[i]
            i += 1
            j -= 1
        else:
            return j


def quick_sort(tab, p, r, pivot):
    if p < r:
        q = partition(tab, p, r, pivot)
        quick_sort(tab, p, q, pivot)
        quick_sort(tab, q + 1, r, pivot)
    return tab


# ------------------------------------------

sorting_type = {'h': (heap_sort, "Heap Sort"), 's': (selection_sort, "Selection Sort"), 'q': (quick_sort, "Quick Sort")}
user_input = input("Select sorting type\n"
                   "Heap Sort (type 'h')\n"
                   "Selection Sort (type 's')\n"
                   "Quick Sort (type 'q')\n"
                   "Your input: ")
if user_input == 'q':
    pivot = (input("Select pivot (most left - type 'l'), (random - type 'r') "))

data_num = [10, 50, 100, 500, 1000, 2000, 3000, 4000, 5000, 10000]
data_type_name = ["constant", "random", "ascending order", "descending order", "A shaped"]
data_type = [generate_constant_data, generate_random_data, generate_ascending_data, generate_descending_data,
             generate_A_shaped_array]
for data in data_type:
    times = []
    for num in data_num:
        d = data(num)
        if user_input == 'q':
            start = time()
            quick_sort(d, 0, len(d) - 1, pivot)
            end = time() - start
            times.append(end)
        else:
            sorting_type[user_input][0](d)
        if num == 10:
            print(f"Sorted array: {d}")
    plt.plot(data_num, times, label=f"{data_type_name[data_type.index(data)]}")


plt.legend()
plt.title(f"{sorting_type[user_input][1]} with different type of data")
plt.xlabel("Number of data")
plt.ylabel("Seconds (s)")
plt.show()


