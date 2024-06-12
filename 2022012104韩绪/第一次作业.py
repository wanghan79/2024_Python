import random

data_range = {
    'name': {'John', 'Smith','Bob'},
    'age': {'20', '18', '22'},
    'id': {'1', '2', '4'}
}

def dataSampling(datatype, datarange, num, strlen=10):
    result = set()
    for _ in range(num):
        if datatype == int:
            item = random.randint(datarange[0], datarange[1])
        elif datatype == float:
            item = random.uniform(datarange[0], datarange[1])
        elif datatype == str:
            item = ''.join(random.choices(datarange, k=strlen))
        result.add(item)
    return result

def dataExtraction(example, num, data_range):

    result = set()
    for _ in range(num):
        temp = []
        for key in example:
            if key in data_range:
                item = random.choice(list(data_range[key]))
                temp.append(item)
        result.add(tuple(temp))
    return result

if __name__ == '__main__':
    example = ('name', 'age', 'id')
    extracted_data = dataExtraction(example, num=3, data_range=data_range)

    print("随机抽取的数据集：")
    for data in extracted_data:
        print(data)
