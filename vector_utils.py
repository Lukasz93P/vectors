from functools import reduce
from typing import Callable
from vector_types import Vector, Number
from math import sqrt


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


def add(*args) -> Vector:
    return reduce_operation_with_validation(simple_add, validate_equality, *args)


def simple_add(x: Vector, y: Vector) -> Vector:
    return [x_ + y_ for x_, y_ in zip(x, y)]


def subtract(*args) -> Vector:
    return reduce_operation_with_validation(simple_subtract, validate_equality, *args)


def simple_subtract(x: Vector, y: Vector) -> Vector:
    return [x_ - y_ for x_, y_ in zip(x, y)]


def multiply_by_scalar(x: Vector, scalar: Number) -> Vector:
    return [x_ * scalar for x_ in x]


def divide(x: Vector, num: Number) -> Vector:
    return multiply_by_scalar(x, 1 / num)


def multiply(*args) -> Vector:
    return reduce_operation_with_validation(simple_multiply, validate_equality, *args)


def simple_multiply(x: Vector, y: Vector) -> Vector:
    return [x_ * y_ for x_, y_ in zip(x, y)]


def magnitude(x: Vector) -> float:
    return sqrt(sum(multiply(x, x)))


def distance(x: Vector, y: Vector) -> float:
    return magnitude(subtract(x, y))


def mean(*args) -> Vector:
    quantity = len(args)
    return [x / quantity for x in add(*args)]
