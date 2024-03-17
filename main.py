from time import time
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, splrep, splev

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


# INSERTION SORT
@timer
def insertion_sort(tab):
    for i in range(1, len(tab)):
        key = tab[i]

        j = i - 1
        while j >= 0 and key < tab[j]:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key
    return tab

# -----------------------------------------


# SHELL SORT
@timer
def shell_sort(tab):
    n = len(tab)
    sedgewick_gaps = [1]
    gap = 1
    while gap < n:
        gap = 4 * gap + 3 * 2 ** (len(sedgewick_gaps) - 1) + 1
        sedgewick_gaps.append(gap)

    for gap in reversed(sedgewick_gaps):
        for i in range(gap, n):
            temp = tab[i]
            j = i
            while j >= gap and tab[j - gap] > temp:
                tab[j] = tab[j - gap]
                j -= gap
            tab[j] = temp
    return tab


# -----------------------------------------


sorting_type = {'h': (heap_sort, "Heap Sort"), 's': (selection_sort, "Selection Sort"), 'q': (quick_sort, "Quick Sort"), "i": (insertion_sort, "Insertion Sort"), 'l': (shell_sort, "Shell Sort")}


data_num = [10, 50, 100, 500, 1000, 2000, 3000, 4000, 5000, 10000]
data_num2 = [10, 50, 100, 200, 500, 1000, 5000, 10000, 25000, 50000]
data_type_name = ["constant", "random", "ascending order", "descending order", "A shaped"]
data_type = [generate_constant_data, generate_random_data, generate_ascending_data, generate_descending_data,
             generate_A_shaped_array]



# Wszystkie sorty w danym ukladzie danych
# times_ql = []
# times_qr = []
#
# for alg in sorting_type.values():
#     times = []
#     for d in data_num:
#         data = generate_ascending_data(d)
#         if alg[1] == 'Quick Sort':
#             start = time()
#             quick_sort(data, 0, len(data) - 1, 'l')
#             end = time() - start
#             times_ql.append(end)
#
#             start = time()
#             quick_sort(data, 0, len(data) - 1, 'r')
#             end = time() - start
#             times_qr.append(end)
#         else:
#             alg[0](data)
#     if alg[1] == 'Quick Sort':
#         plt.plot(data_num, times_qr, label=f"{alg[1]} - random pivot")
#         plt.plot(data_num, times_ql, label=f"{alg[1]} - left pivot")
#     else:
#         plt.plot(data_num, times, label=f"{alg[1]}")



# Jeden sort dla wszystkich układów danych
user_input = input("Select sorting type\n"
                   "Heap Sort (type 'h')\n"
                   "Selection Sort (type 's')\n"
                   "Quick Sort (type 'q')\n"
                   "Insertion Sort (type 'i')\n"
                   "Shell Sort (type 'l')\n"
                   "Your input: ")
if user_input == 'q':
    pivot = (input("Select pivot (most left - type 'l'), (random - type 'r') "))

for data in data_type:
    times = []
    for num in data_num:
        d = data(num)
        if num == 10:
            print(f"Unsorted array: {d}")
        if user_input == 'q':
            start = time()
            quick_sort(d, 0, len(d) - 1, pivot)
            end = time() - start
            times.append(end)
        else:
            sorting_type[user_input][0](d)
        if num == 10:
            print(f"Sorted array: {d}\n")

    spline = splrep(data_num, times)
    x_new = data_num.copy()
    y_new = splev(x_new, spline)
    plt.plot(x_new, y_new, label=f"{data_type_name[data_type.index(data)]}")



# Pojednycze sorty + pojedyncze typy danych
# times = []
# for d in data_num:
#     data = generate_constant_data(d)
#     shell_sort(data)
#
# data_num_sorted, times_sorted = zip(*sorted(zip(data_num, times)))
# spline = splrep(data_num_sorted, times_sorted)
# x_new = data_num.copy()
# y_new = splev(x_new, spline)
# plt.plot(x_new, y_new, label=f"constant")



plt.legend()
# plt.title(f"Shell Sort with different type of data")
plt.title(f"{sorting_type[user_input][1]} with different type of data")
plt.xlabel("Number of data")
plt.ylabel("Seconds (s)")
plt.show()


