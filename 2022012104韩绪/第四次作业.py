import random

def decorator(aClass):
    class DecoratorClass():
        def __init__(self):
            self.aClass = aClass()

        def dataExtraction(self, example, num):
            print(self.aClass.dataExtraction(example, num))

        def data_iterator(self, example, n):
            for i in range(n):
                yield self.dataExtraction(example, num=1)

    return DecoratorClass


@decorator
class DataProcessor:
    def __init__(self):
        self.data_range = {
            'name': {'John', 'Smith','Bob'},
            'age': {'20', '18', '22'},
            'id': {'1', '2', '4'}
        }
    """
    def dataSampling(self, datatype, datarange, num, strlen=10):
        result = set()
        for index in range(num):
            if datatype == int:
                item = random.randint(datarange[0], datarange[1])
                result.add(item)
            elif datatype == float:
                item = random.uniform(datarange[0], datarange[1])
                result.add(item)
            elif datatype == str:
                item = ''.join(random.choices(datarange, k=strlen))
                result.add(item)
        return result
    """
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
        pass

def yield_test(n:int):
    i = 0
    while i <= n:
        i += 1
        tmp = yield i
        if tmp is not None:
            i = tmp


if __name__ == '__main__':

    dataProcessor = DataProcessor()
    # dataProcessor.dataExtraction(example=('id', 'name', 'age'), num=10)
    data_it = dataProcessor.data_iterator(example=('id', 'name', 'age'), n=50)
    next(data_it)
    next(data_it)
    next(data_it)
'''
processor = DataProcessor()
 example = ('name', 'age', 'id')
 extracted_data = processor.dataExtraction(example, num=3)
 print("随机抽取的数据集：")
 for data in extracted_data:
     print(data)
 '''
