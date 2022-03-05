"""
Taylor series
"""
import math
from itertools import count
from typing import Union

EPSILON = 0.0001

def get_item_n(x, n):
    """
    Очередной элемент бесконечного ряда по общей формуле из интернета
    """
    return ((-1) ** (n - 1) * x ** (2 * n - 1)) / math.factorial(2 * n - 1)


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    print(x)
    return 0



def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """

    sum_ = 0
    for i in count(1, 1):
        current_item = get_item_n(x, i)
        sum_ += current_item
        if abs(current_item) <= EPSILON:
            return sum_
