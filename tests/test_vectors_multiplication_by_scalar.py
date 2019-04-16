import vector_utils
from tests.vectors_test_preparation import VectorsTestPreparation


class TestVectorsMultiplicationByScalar(VectorsTestPreparation):
    @classmethod
    def setUpClass(cls):
        VectorsTestPreparation.setUpClass()
        cls.first_result = [2, 4, 10, 12]

    def test_should_multiply_by_two(self):
        self.assertEqual(self.first_result, vector_utils.multiply_by_scalar(self.x_test_vector, 2))
