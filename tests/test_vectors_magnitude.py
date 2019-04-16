import vector_utils
from tests.vectors_test_preparation import VectorsTestPreparation


class TestVectorsMagnitude(VectorsTestPreparation):
    def test_vector_magnitudes(self):
        self.assertEqual(9.9, round(vector_utils.magnitude([5, 3, 8]), 1))
