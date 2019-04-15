import vector_utils
from tests.vectors_test_preparation import VectorsTestPreparation


class TestVectorsSubtracting(VectorsTestPreparation):
    @classmethod
    def setUpClass(cls):
        VectorsTestPreparation.setUpClass()
        cls.two_vectors_subtr_result = [-1, -2, -3, -1]
        cls.three_vectors_subtr_result = [-6, -8, -6, -16]

    def test_two_vectors_subtraction(self):
        for x, y in zip(vector_utils.subtract(self.x_test_vector, self.y_test_vector), self.two_vectors_subtr_result):
            self.assertEqual(x, y)

    def test_three_vectors_subtraction(self):
        for x, y in zip(vector_utils.subtract(self.x_test_vector, self.y_test_vector, self.z_test_vector),
                        self.three_vectors_subtr_result):
            self.assertEqual(x, y)

    def test_should_throw_error_subtracting_adding_not_equal_vectors(self):
        super().should_throw_error_while_performing_operation_on_not_equal_vectors(vector_utils.subtract, [1, 2],
                                                                                   [2, 3, 4])
