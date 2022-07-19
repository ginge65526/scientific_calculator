import math
import test1 as func
import numpy as np
from scipy import constants as sci


def solution_0(*list_of_numbers):
    answer = list_of_numbers[0] * func.dvt(
        displacement=list_of_numbers[2],
        velocity=math.hypot(
            list_of_numbers[0],
            list_of_numbers[1]
        )
    )
    return answer


def solution_1(*list_of_numbers):
    answer = np.divide(
        np.multiply(
            sci.g,
            func.add(
                np.multiply(
                    list_of_numbers[0],
                    list_of_numbers[2]
                ),
                np.multiply(
                    list_of_numbers[3],
                    np.mean(
                        list_of_numbers[0:2]
                    )
                )
            )
        ),
        sum(
            list_of_numbers[0:2]
        )
    )
    return answer


def solution_2(*list_of_numbers):
    answer = math.hypot(
        list_of_numbers[0],
        list_of_numbers[1]
    )
    return answer


def solution_3(*list_of_numbers):
    answer = np.divide(
        np.prod(
            list_of_numbers
        ),
        4
    )
    return answer


def solution_4(*list_of_numbers):
    g_to_kg = sci.gram * list_of_numbers[0]
    answer = np.multiply(
        np.subtract(
            g_to_kg,
            np.multiply(
                g_to_kg,
                np.power(
                    0.5,
                    np.true_divide(
                        (list_of_numbers[2] * sci.minute),
                        (list_of_numbers[1] * sci.day)
                    )
                )
            )
        ),
        np.square(
            sci.c
        )
    )
    answer = answer / sci.giga
    return answer


def solution_5(*list_of_numbers):
    pass


def solution_6(*list_of_numbers):
    pass


def solution_7(*list_of_numbers):
    pass


def solution_8(*list_of_numbers):
    pass


def solution_9(*list_of_numbers):
    pass


def solution_10(*list_of_numbers):
    pass


def solution_11(*list_of_numbers):
    pass
