import vector_utils
from tests.vectors_test_preparation import VectorsTestPreparation


class TestVectorsLengthEquality(VectorsTestPreparation):
    def test_should_return_true(self):
        self.assertTrue(vector_utils.are_equal(self.x_test_vector, self.y_test_vector, self.z_test_vector))

    def test_should_return_false(self):
        self.assertFalse(vector_utils.are_equal([2, 4, 5], self.x_test_vector, self.y_test_vector, self.z_test_vector))
