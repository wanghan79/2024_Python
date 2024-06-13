import random
import string

data_range = {
    'name': {'John', 'Smith', 'Bob','Jane'},
    'age': {'20', '18', '22'},
    'id': {'1', '2', '4'}
}

example_template = {
    "datatype": tuple,
    "subs": {
        "name": {
            "datatype": str,
            "datarange": data_range['name'],
            "len": 1  # specifying length 1 for single random choice
        },
        "age": {
            "datatype": str,
            "datarange": data_range['age'],
            "len": 1
        },
        "id": {
            "datatype": str,
            "datarange": data_range['id'],
            "len": 1
        }
    }
}

def generate_data(template):
    datatype = template.get("datatype")
    subs = template.get("subs", {})

    result = {
        tuple: (),
        list: [],
        dict: {},
        set: set()
    }[datatype]

    for key, value in subs.items():
        data = generate_item(value)
        if datatype == tuple:
            result += (data,)
        elif datatype == list:
            result.append(data)
        elif datatype == dict:
            result[key] = data
        elif datatype == set:
            result.add(data)

    return result

def generate_item(value):
    if "datatype" in value and "datarange" in value:
        if value["datatype"] == int:
            return random.randint(*value["datarange"])
        elif value["datatype"] == float:
            return random.uniform(*value["datarange"])
        elif value["datatype"] == bool:
            return random.choice([True, False])
        elif value["datatype"] == str:
            datarange_list = list(value["datarange"])  # Convert set to list
            return ''.join(random.choices(datarange_list, k=value.get("len", 1)))
    return generate_data(value)


def dataExtraction(example, num, data_range):
    result = set()
    for _ in range(num):
        extracted_data = generate_data(example)
        result.add(extracted_data)
    return result

if __name__ == '__main__':
    extracted_data = dataExtraction(example_template, num=3, data_range=data_range)

    print("Generated random data:")
    for data in extracted_data:
        print(data)
'''import random

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
'''
