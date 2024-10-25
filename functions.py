import matplotlib.pyplot as plt
import numpy as np
from sorts import (quick_sort, shell_pratt_sort, shell_sort,
                   shell_hibbard_sort, selection_sort, heap_sort,
                   merge_sort, bubble_sort, insertion_sort)
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


def make_plot(array_sizes, execution_times, sort_name, description):

    x = np.array(array_sizes)
    y = np.array(execution_times)


    polynomial_features = PolynomialFeatures(degree=2, include_bias=False)
    x_poly = polynomial_features.fit_transform(x.reshape(-1, 1))


    regression_model = LinearRegression()
    regression_model.fit(x_poly, y)


    y_predicted = regression_model.predict(x_poly)


    plt.title(f'Время выполнения сортировки: {description}')
    plt.xlabel('Размер массива')
    plt.ylabel('Время (секунды)')

    plt.scatter(x, y, color="red", label='Фактическое время')
    plt.plot(x, y_predicted, color="blue", label=sort_name)


    plt.legend()
    plt.grid(True)


    plt.show()