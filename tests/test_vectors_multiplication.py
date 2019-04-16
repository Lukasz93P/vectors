import vector_utils
from tests.vectors_test_preparation import VectorsTestPreparation


class TestVectorsMultiplication(VectorsTestPreparation):
    def test_multiply_two_vectors(self):
        self.assertEqual([5, 3, 8], vector_utils.multiply([2.5, 6, 4], [2, .5, 2]))

    def test_multiply_three_vectors(self):
        self.assertEqual([20, 15, 12],
                         vector_utils.multiply([2, 2, 2], [5, 7.5, 2], [2, 1, 3]))
