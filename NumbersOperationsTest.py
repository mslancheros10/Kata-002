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

    def test_elementsNumbersMultipleNumbers(self):
        self.assertEquals(self.numbersOperations.elementsNumbers('5,9,0,1,3')[0],5,"Elements number")

    def test_elementsNumbersMultipleNumbers(self):
        self.assertEquals(self.numbersOperations.elementsNumbers('5,9,0,1,3')[0],5,"Elements number")

    def test_elementsMinEmpty(self):
        self.assertEquals(self.numbersOperations.elementsMin(''),[0,0],"Elements number and minimum")

    def test_elementsMinOneNumber(self):
        self.assertEquals(self.numbersOperations.elementsMin('3'),[1,3],"Elements number and minimum")

    def test_elementsMinTwoNumbers(self):
        self.assertEquals(self.numbersOperations.elementsMin('7,4'),[2,4],"Elements number and minimum")

    def test_elementsMinTwoNumbers(self):
        self.assertEquals(self.numbersOperations.elementsMin('5,1,9,6,1,13'),[6,1],"Elements number and minimum")

    def test_elementsMaxEmpty(self):
        self.assertEquals(self.numbersOperations.elementsMax(''),[0,0,0],"Elements number, minimum and maximum")

    def test_elementsMaxOneNumber(self):
        self.assertEquals(self.numbersOperations.elementsMax('9'),[1,9,9],"Elements number, minimum and maximum")

    def test_elementsMaxTwoNumbers(self):
        self.assertEquals(self.numbersOperations.elementsMax('10,20'),[2,10,20],"Elements number, minimum and maximum")

    def test_elementsMaxMultipleNumbers(self):
        self.assertEquals(self.numbersOperations.elementsMax('8,13,20,5,9,12'),[2,10,20],"Elements number, minimum and maximum")
