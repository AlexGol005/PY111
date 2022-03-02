"""
This module implements some functions based on linear search algo
Этот модуль реализует некоторые функции, основанные на алгоритме линейного поиска
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    Функция, которая находит минимальный элемент в массиве

    :param arr: Массив, содержащий числа
    :return: индекс первого появления минимального элемента в массиве
    """

    i = 0
    min_ = arr[i]
    while i < len(arr):
        if arr[i] < min_:
            min_ = arr[i]
            i += 1
        elif arr[i] >= min_:
            i += 1
    return arr.index(min_)
arr = [2, 1, 2, -1, -11, 2, 7,-10, 7, -12, 8]
print(arr)
print(min_search(arr))
