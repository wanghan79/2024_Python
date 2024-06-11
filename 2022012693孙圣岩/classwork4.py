import random
import string


class RandomDataGenerator:
    def __init__(self, data_structure):
        self.data_structure = data_structure
        self.data_counts = {}  # 用于记录数据类型的计数

    def count_data_type(func):
        def wrapper(self, *args, **kwargs):
            data_type = func(self, *args, **kwargs)
            if data_type in self.data_counts:
                self.data_counts[data_type] += 1
            else:
                self.data_counts[data_type] = 1
            return data_type

        return wrapper

    @count_data_type
    def type_count(self, **kwargs):
        data_type = None
        if kwargs["datatype"] == int:
            data_type = "int"
        elif kwargs["datatype"] == float:
            data_type = "float"
        elif kwargs["datatype"] == str:
            data_type = "str"
        elif kwargs["datatype"] == list:
            data_type = "list"
            for key, value in kwargs["subs"].items():
                self.type_count(**value)
        elif kwargs["datatype"] == tuple:
            data_type = "tuple"
            for key, value in kwargs["subs"].items():
                self.type_count(**value)
        return data_type

    def fill_data_generator(self, **kwargs):
        def generate_data(**kwargs):
            if kwargs["datatype"] == int:
                return random.randint(kwargs["datarange"][0], kwargs["datarange"][1])
            elif kwargs["datatype"] == float:
                return random.uniform(kwargs["datarange"][0], kwargs["datarange"][1])
            elif kwargs["datatype"] == str:
                return ''.join(random.choices(kwargs["datarange"], k=random.randint(1, 10)))
            elif kwargs["datatype"] == list:
                sublist = {}
                for key, value in kwargs["subs"].items():
                    sublist[key] = generate_data(**value)
                return [sublist[key] for key in sorted(sublist)]
            elif kwargs["datatype"] == tuple:
                sublist = {}
                for key, value in kwargs["subs"].items():
                    sublist[key] = generate_data(**value)
                return tuple(sublist[key] for key in sorted(sublist))

        return generate_data(**kwargs)

    def generate_random_data(self):
        self.type_count(**self.data_structure)
        return self.data_counts, self.fill_data_generator(**self.data_structure)


# 示例调用
data_structure = {
    "datatype": tuple,
    "subs": {
        "sub1": {
            "datatype": list,
            "subs": {
                "sub1": {
                    "datatype": int,
                    "datarange": (0, 100)
                },
                "sub2": {
                    "datatype": str,
                    "datarange": string.ascii_uppercase
                }
            }
        },
        "sub2": {
            "datatype": tuple,
            "subs": {
                "sub1": {
                    "datatype": float,
                    "datarange": (0, 5000),
                },
                "sub2": {
                    "datatype": int,
                    "datarange": (1, 200),
                }
            }
        },
        "sub3": {
            "datatype": str,
            "datarange": string.ascii_uppercase
        }
    }
}

random_data_generator = RandomDataGenerator(data_structure)
data_counts, filled_data = random_data_generator.generate_random_data()

# 使用迭代器逐步生成数据
def data_generator(data):
    if isinstance(data, list) or isinstance(data, tuple):
        for sub_data in data:
            yield from data_generator(sub_data)
    else:
        yield data

data_iterator = data_generator(filled_data)

# 逐步生成数据
for data_point in data_iterator:
    print("Generated Data Point:", data_point)

print("Data Type Counts:", data_counts)
