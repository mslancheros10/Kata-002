from unittest import TestCase

from NumbersOperations import NumbersOperations

class NumbersOperationsTest(TestCase):

    numbersOperations = NumbersOperations()

    def test_elementsNumbersEmptyString(self):
        self.assertEquals(self.numbersOperations.elementsNumbers('')[0],0,"Elements number")

    def test_elementsNumbersOneNumber(self):
        self.assertEquals(self.numbersOperations.elementsNumbers('5')[0],1,"Elements number")

    def test_elementsNumbersTwoNumbers(self):
        self.assertEquals(self.numbersOperations.elementsNumbers('5,6')[0],2,"Elements number")


