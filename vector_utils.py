from functools import reduce
from typing import Callable


def are_equal(*args) -> bool:
    first = args[0]
    for x in args[1:]:
        if len(first) is not len(x):
            return False

    return True


def validate_equality(*args):
    if not are_equal(*args):
        raise ArithmeticError('Only vectors with equal dimensions supports this operation')


def reduce_operation_with_validation(operation: Callable, validation: Callable, *args):
    validation(*args)
    return reduce(operation, args)


def add(*args) -> list:
    return reduce_operation_with_validation(simple_add, validate_equality, *args)


def simple_add(x: list, y: list) -> list:
    return [x_ + y_ for x_, y_ in zip(x, y)]


def subtract(*args) -> list:
    return reduce_operation_with_validation(simple_subtract, validate_equality, *args)


def simple_subtract(x: list, y: list) -> list:
    return [x_ - y_ for x_, y_ in zip(x, y)]
