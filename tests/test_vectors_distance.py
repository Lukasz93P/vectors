import vector_utils
from tests.vectors_test_preparation import VectorsTestPreparation


class TestVectorsMagnitude(VectorsTestPreparation):
    def test_vector_distance(self):
        self.assertEqual(6.7, round(vector_utils.distance([5, 3, 8], [-1, 3, 5]), 1))
