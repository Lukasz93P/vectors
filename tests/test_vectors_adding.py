import vector_utils
from tests.vectors_test_preparation import VectorsTestPreparation


class TestVectorsAdding(VectorsTestPreparation):
    @classmethod
    def setUpClass(cls) -> None:
        VectorsTestPreparation.setUpClass()
        cls.simple_add_result = [3, 6, 13, 13]
        cls.three_vectors_add_result = [8, 12, 16, 28]
        cls.four_vectors_add_test = [9, 14, 20, 33]

    def test_sum_two_vectors(self):
        self.assertEqual(self.simple_add_result, vector_utils.add(self.x_test_vector, self.y_test_vector))

    def test_sum_three_vectors(self):
        self.assertEqual(self.three_vectors_add_result,
                         vector_utils.add(self.x_test_vector, self.y_test_vector, self.z_test_vector))

    def test_sum_four_vectors(self):
        self.assertEqual(self.four_vectors_add_test,
                         vector_utils.add(self.x_test_vector, self.y_test_vector, self.z_test_vector,
                                          self.v_test_vector))

    def test_should_throw_error_while_adding_not_equal_vectors(self):
        super().should_throw_error_while_performing_operation_on_not_equal_vectors(vector_utils.add, [1, 2], [2, 3, 4])
