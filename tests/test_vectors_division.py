import vector_utils
from tests.vectors_test_preparation import VectorsTestPreparation


class TestVectorsDivision(VectorsTestPreparation):
    @classmethod
    def setUpClass(cls):
        VectorsTestPreparation.setUpClass()
        cls.first_result = [.5, 1, 2.5, 3]

    def test_should_multiply_by_two(self):
        self.assertEqual(self.first_result, vector_utils.divide(self.x_test_vector, 2))
