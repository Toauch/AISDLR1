import random
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sorts import *
from functions import make_plot

random.seed(777)


def square(x):
    return x ** 2


def line(x):
    return x


def nlognsquare(x):
    return x * np.log(x) ** 2


def nlogn(x):
    return x * np.log(x)


def n32(x):
    return x ** (3 / 2)


def n54(x):
    return x ** (5 / 4)


def n43(x):
    return x ** (4 / 3)


def plot_complexity(functions):

    for func, label, title in functions:
        plt.figure(figsize=(10, 6))
        x = np.linspace(1, 20001, 500)
        y = func(x)

        plt.plot(x, y, label=label)
        plt.title(title)
        plt.xlabel('Размер массива')
        plt.ylabel('Время (условные единицы)')
        plt.grid()
        plt.legend()
        plt.show()



functions = [
    (square, 'O(n^2)', 'Время выполнения с квадратичной асимптотикой'),
    (line, 'O(n)', 'Время выполнения с линейной асимптотикой'),
    (n32, 'O(n^(3/2))', 'Время выполнения с n^(3/2) асимптотикой'),
    (n43, 'O(n^(4/3))', 'Время выполнения с n^(4/3) асимптотикой'),
    (n54, 'O(n^(5/4))', 'Время выполнения с n^(5/4) асимптотикой'),
    (nlogn, 'O(n log n)', 'Время выполнения с n log n асимптотикой'),
    (nlognsquare, 'O(n log^2 n)', 'Время выполнения с n log^2 n асимптотикой')
]


plot_complexity(functions)


array_sizes = list(range(1, 20002, 1000))
min_value = 1
max_value = 1000000


def calculate_time(func, array):

    start_time = time.time()
    func(array.copy())
    return time.time() - start_time


def measure_sorting_times(random_array):

    sorting_algorithms = {
        'insertion': insertion_sort,
        'quick': quick_sort,
        'shell': shell_sort,
        'selection': selection_sort,
        'bubble': bubble_sort,
        'merge': merge_sort,
        'heap': heap_sort,
        'shell_pratt': shell_pratt_sort,
        'shell_hibbard': shell_hibbard_sort,
    }

    sort_times = {name: [] for name in sorting_algorithms}

    for name, algorithm in sorting_algorithms.items():
        sort_times[name].append(calculate_time(algorithm, random_array))

    return sort_times



plots_data = {sort_name: {'average': [], 'best': [], 'worst': [], 'almost': []} for sort_name in
              ['insertion', 'selection', 'quick',
               'shell', 'shell_pratt',
               "shell_hibbard",
               'heap', 'bubble',
               'merge']}


for size in array_sizes:
    random_array = [random.randint(min_value, max_value) for _ in range(size)]
    sort_times = measure_sorting_times(random_array)

    for sort_name in sort_times.keys():
        plots_data[sort_name]['average'].append(sort_times[sort_name])


for sort_name in plots_data.keys():
    make_plot(array_sizes, plots_data[sort_name]['average'], sort_name, "mid")


for size in array_sizes:
    sorted_array = list(range(size))
    sort_times = measure_sorting_times(sorted_array)

    for sort_name in sort_times.keys():
        plots_data[sort_name]['best'].append(sort_times[sort_name])

for sort_name in plots_data.keys():
    make_plot(array_sizes, plots_data[sort_name]['best'], sort_name, "best")


for size in array_sizes:
    sorted_array = list(range(size))[::-1]
    sort_times = measure_sorting_times(sorted_array)

    for sort_name in sort_times.keys():
        plots_data[sort_name]['worst'].append(sort_times[sort_name])

for sort_name in plots_data.keys():
    make_plot(array_sizes, plots_data[sort_name]['worst'], sort_name, "worst")


for size in array_sizes:
    almost_sorted_array = [random.randint(min_value, max_value) for _ in range(int(size * 0.9))]
    almost_sorted_array.sort()

    reverse_sorted_part = [random.randint(min_value, max_value) for _ in range(int(size * 0.1))]
    reverse_sorted_part.sort(reverse=True)

    combined_array = almost_sorted_array + reverse_sorted_part
    sort_times = measure_sorting_times(combined_array)

    for sort_name in sort_times.keys():
        plots_data[sort_name]['almost'].append(sort_times[sort_name])

for sort_name in plots_data.keys():
    make_plot(array_sizes, plots_data[sort_name]['almost'], sort_name, "90|10")


for sort_name, cases in plots_data.items():
    print(f'Sort: {sort_name}')

    for case_type, timings in cases.items():
        print(f'  Case: {case_type}')

        for size_index, time_taken in enumerate(timings):
            print(f'   Размер массива: {array_sizes[size_index]}, Время сортировки: {time_taken}')

for sort_name, sort_cases in plots_data.items():
    plt.figure(figsize=(15, 6))
    for sort_type, timings in sort_cases.items():
        x = np.array(array_sizes)
        y = np.array(timings).flatten() # Берем данные для текущей сортировки и типа

        # Полиномиальная регрессия
        poly = PolynomialFeatures(degree=2, include_bias=False)
        poly_features = poly.fit_transform(x.reshape(-1, 1))
        poly_reg_model = LinearRegression()
        poly_reg_model.fit(poly_features, y)
        y_predicted = poly_reg_model.predict(poly_features)

        # Построение графика

        plt.plot(x, y_predicted, label=f'{sort_name} - {sort_type}')

# Настройка графика
    plt.title('Время выполнения различных сортировок для разных случаев')
    plt.xlabel('Размер массива * 0.1')
    plt.ylabel('Время (секунды)')
    plt.xticks(array_sizes)
    plt.grid(True)
    plt.legend()
    plt.show()