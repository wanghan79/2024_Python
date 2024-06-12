import random


class DataProcessor:
    def __init__(self):
        self.data_range = {
            'name': {'John', 'Smith'},
            'age': {'20', '18', '22'},
            'id': {'1', '2', '4'}
        }
    """dataSampling(datatype, datarange, num, strlen=10): 这个函数用于从指定的数据范围中随机抽样生成一定数量的数据。
    根据输入的数据类型 datatype，数据范围 datarange，生成数量 num，以及字符串长度 strlen（仅在数据类型为字符串时有效），返回一个集合（set）包含随机生成的数据样本。"""
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
    """dataExtraction(example, data_range, num): 这个函数根据给定的示例和数据范围，从数据范围中抽取数据，形成一组数据集合。"""
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


if __name__ == '__main__':
    processor = DataProcessor()

    example = ('name', 'age', 'id')
    extracted_data = processor.dataExtraction(example, num=3)

    print("随机抽取的数据集：")
    for data in extracted_data:
        print(data)
