from unittest import TestCase
from typing import Callable


class VectorsTestPreparation(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.x_test_vector = [1, 2, 5, 6]
        cls.y_test_vector = [2, 4, 8, 7]
        cls.z_test_vector = [5, 6, 3, 15]
        cls.v_test_vector = [1, 2, 4, 5]

    def should_throw_error_while_performing_operation_on_not_equal_vectors(self, operation: Callable, *args):
        error = False
        try:
            operation(*args)
        except ArithmeticError:
            error = True
        self.assertTrue(error)
