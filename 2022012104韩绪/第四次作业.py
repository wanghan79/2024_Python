import random
import string

def decorator(aClass):
    class DecoratorClass():
        def __init__(self):
            self.aClass = aClass()

        def dataExtraction(self, example, num):
            return self.aClass.dataExtraction(example, num)

        def data_yield(self, example, num):
            for i in range(num):
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

        self.example_template = {
            "datatype": tuple,
            "subs": {
                "name": {
                    "datatype": str,
                    "datarange": self.data_range['name'],
                    "len": 1  # specifying length 1 for single random choice
                },
                "age": {
                    "datatype": str,
                    "datarange": self.data_range['age'],
                    "len": 1
                },
                "id": {
                    "datatype": str,
                    "datarange": self.data_range['id'],
                    "len": 1
                }
            }
        }

    def generate_data(self, template):
        datatype = template.get("datatype")
        subs = template.get("subs", {})

        result = {
            tuple: (),
            list: [],
            dict: {},
            set: set()
        }[datatype]

        for key, value in subs.items():
            data = self.generate_item(value)
            if datatype == tuple:
                result += (data,)
            elif datatype == list:
                result.append(data)
            elif datatype == dict:
                result[key] = data
            elif datatype == set:
                result.add(data)

        return result

    def generate_item(self, value):
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
        return self.generate_data(value)

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

    def data_yield(self, example, num):
        return self.aClass.data_yield(example, num)

if __name__ == '__main__':
    processor = DataProcessor()

    example = ('name', 'age', 'id')
    for data in processor.data_yield(example, num=3):
        print(str(data))
