import vector_utils
from tests.vectors_test_preparation import VectorsTestPreparation


class TestVectorsMean(VectorsTestPreparation):
    def test_vectors_mean(self):
        result = [5.3, 16.3, 5]
        for x, y in zip(vector_utils.mean([5, 3, 8], [-1, 3, 5], [12, 43, 2]), result):
            self.assertEqual(round(x, 1), y)
