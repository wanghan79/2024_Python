import random

def decorator(aClass):
    class DecoratorClass():
        def __init__(self):
            self.aClass = aClass()

        def dataExtraction(self, example, num):
            return self.aClass.dataExtraction(example, num)

        def data_iterator(self, example, n):
            for i in range(n):
                yield self.dataExtraction(example, num=1)

    return DecoratorClass

@decorator
class DataProcessor:
    def __init__(self):
        self.data_range = {
            'name': {'John', 'Smith', 'Bob'},
            'age': {'20', '18', '22'},
            'id': {'1', '2', '4'}
        }

    def dataExtraction(self, example, num):
        result = set()
        for _ in range(num):
            temp = []
            for i in example:
                if i in self.data_range:
                    item = random.choice(list(self.data_range[i]))
                    temp.append(item)
            result.add(tuple(temp))
        return result

    def data_iterator(self, example, n):
        return self.aClass.data_iterator(example, n)

if __name__ == '__main__':
    dataProcessor = DataProcessor()

    example = ('id', 'name', 'age')
    for data in dataProcessor.data_iterator(example, n=5):
        print(data)
