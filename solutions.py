import math
import test1 as func
from scipy import constants as sci
import operator as np
from statistics import mean
from numpy import power


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
    answer = np.truediv(
        np.mul(
            sci.g,
            func.add(
                np.mul(
                    list_of_numbers[0],
                    list_of_numbers[2]
                ),
                np.mul(
                    list_of_numbers[3],
                    mean(
                        list_of_numbers[0:2]
                    )
                )
            )
        ),
        math.fsum(
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
    answer = np.truediv(
        math.prod(
            list_of_numbers
        ),
        4
    )
    return answer


def solution_4(*list_of_numbers):
    g_to_kg = sci.gram * list_of_numbers[0]
    answer = np.mul(
        np.sub(
            g_to_kg,
            np.mul(
                g_to_kg,
                np.pow(
                    0.5,
                    np.truediv(
                        (list_of_numbers[2] * sci.minute),
                        (list_of_numbers[1] * sci.day)
                    )
                )
            )
        ),
        (sci.c ** 2)
    )
    answer = answer / sci.giga
    return answer


def solution_5(*list_of_numbers):
    answer = np.truediv(
        (
                (list_of_numbers[1] * sci.day)
                *
                (list_of_numbers[0] * sci.giga)
        ),
        (sci.c ** 2)
    )
    answer = answer / sci.gram
    return answer


def solution_6(*list_of_numbers):
    answer = np.truediv(
        list_of_numbers[0],
        math.log2(
            np.truediv(
                2520,
                list_of_numbers[1]
            )
        )
    )
    answer = answer * 60
    return answer


def solution_7(*list_of_numbers):
    answer = np.truediv(np.mul((list_of_numbers[1] * sci.metric_ton), (sci.c ** 2)), (list_of_numbers[0] * sci.peta))
    answer = answer / sci.hour
    return answer


def solution_8(*list_of_numbers):
    answer = (math.prod(list_of_numbers[:3]) * sci.centi) / list_of_numbers[3]
    return answer


def solution_9(*list_of_numbers):
    answer = list_of_numbers[0] * math.fsum(
        power(
            list_of_numbers[1:], -1
        )
    )
    return answer


def solution_10(*list_of_numbers):
    answer = list_of_numbers[0] * (
            (list_of_numbers[3] / (list_of_numbers[0] ** 2))
            +
            math.fsum(
                power(
                    list_of_numbers[1:3], -1
                )
            )
    )
    return answer


def solution_11(*list_of_numbers):
    c = (2.00, sci.pi, list_of_numbers[1], sci.milli, 0.50,)
    answer = abs(
        (sci.mu_0 * (np.truediv(
            list_of_numbers[0], list_of_numbers[2]
        ) - np.truediv(
            list_of_numbers[0], list_of_numbers[3]
        )) / math.prod(
            c
        ))
    )
    answer = answer / sci.micro
    return answer
