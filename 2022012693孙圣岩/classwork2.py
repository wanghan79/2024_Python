import random
import string


class RandomDataGenerator:
    def __init__(self, data_structure):
        self.data_structure = data_structure

    def fill_random_values(self, **kwargs):
        if kwargs["datatype"] == int:
            return random.randint(kwargs["datarange"][0], kwargs["datarange"][1])
        elif kwargs["datatype"] == float:
            return random.uniform(kwargs["datarange"][0], kwargs["datarange"][1])
        elif kwargs["datatype"] == str:
            return ''.join(random.choices(kwargs["datarange"], k=random.randint(1, 10)))
        elif kwargs["datatype"] == list:
            sublist = {}
            for key, value in kwargs["subs"].items():
                sublist[key] = self.fill_random_values(**value)
            return [sublist[key] for key in sorted(sublist)]
        elif kwargs["datatype"] == tuple:
            sublist = {}
            for key, value in kwargs["subs"].items():
                sublist[key] = self.fill_random_values(**value)
            return tuple(sublist[key] for key in sorted(sublist))

    def generate_random_data(self, num):
        for x in range(num):
            print(self.fill_random_values(**self.data_structure))


# 示例数据结构模板
dataStructure = {
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
num = int(input("请输入要生成的数据结构数量："))
random_data_generate = RandomDataGenerator(dataStructure)
random_data_generate.generate_random_data(num)


