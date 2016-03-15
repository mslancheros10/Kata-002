

class NumbersOperations:

    def elementsNumbers(self, numbers):
        arraynumbers = numbers.split(',')
        if arraynumbers[0] == '':
            return [0]
        arraynumbers = map(int,arraynumbers)
        array = [len(arraynumbers)]
        return array


    def elementsMin(self, numbers):
        elementNumers = self.elementsNumbers(numbers)
        arraynumbers = numbers.split(',')
        if arraynumbers[0] == '':
            return [elementNumers[0],0]
        arraynumbers = map(int,arraynumbers)
        array = [min(arraynumbers)]
        return [elementNumers[0],int(array[0])]

    def elementsMax(self, numbers):
        minNumber = self.elementsMin(numbers)
        arraynumbers = numbers.split(',')
        if arraynumbers[0] == '':
            return [minNumber[0],minNumber[1],0]
        arraynumbers = map(int,arraynumbers)
        array = [max(arraynumbers)]
        return [minNumber[0],minNumber[1],int(array[0])]

    def elementsAvg(self, numbers):
        maxNumber = self.elementsMax(numbers)
        arraynumbers = numbers.split(',')
        if arraynumbers[0] == '':
            return [maxNumber[0],maxNumber[1],0]
        array = [max(arraynumbers)]
        return [maxNumber[0],maxNumber[1],int(array[0])]

