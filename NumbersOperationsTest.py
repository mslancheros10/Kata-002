from unittest import TestCase

from NumbersOperations import NumbersOperations

class NumbersOperationsTest(TestCase):

    numbersOperations = NumbersOperations()

    def test_elementsNumbers(self):
        self.assertEquals(self.numbersOperations.elementsNumbers('')[0],0,"Elements number")
