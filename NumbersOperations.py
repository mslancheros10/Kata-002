

class NumbersOperations:

    def elementsNumbers(self, numbers):
        arraynumbers = numbers.split(',')
        if arraynumbers[0] == '':
            return [0]
        array = [len(arraynumbers)]
        return array


    def elementsMin(self, numbers):
        elementNumers = self.elementsNumbers(numbers)
        arraynumbers = numbers.split(',')
        if arraynumbers[0] == '':
            return [elementNumers[0],0]
        array = [min(arraynumbers)]
        return [elementNumers[0],int(array[0])]

