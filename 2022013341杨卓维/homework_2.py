import string
import random


class DataSampler:
    def __init__(self):
        pass

    def data_Sampling(self, **kwargs):
        result = []
        dataType = kwargs.get('dataType')
        if dataType is None:
            return "Error"

        if dataType == 'int':
            dataRange = kwargs.get('datarange')
            result.append(random.randint(*dataRange))

        elif dataType == 'float':
            dataRange = kwargs.get('datarange')
            result.append(random.uniform(*dataRange))

        elif dataType == 'str':
            dataRange = kwargs.get('datarange')
            length = kwargs.get('len', 1)
            result.append(''.join(random.choice(dataRange) for _ in range(length)))

        elif dataType == 'bool':
            result.append(random.choice([True, False]))

        elif dataType == 'list':
            subs = kwargs.get('subs')
            if isinstance(subs, dict):
                result.append([self.data_Sampling(**sub) for sub in subs.values()])
            else:
                length = subs
                result.append([random.randint(0, 100) for _ in range(length)])

        elif dataType == 'tuple':
            subs = kwargs.get('subs')
            result.append(tuple(self.data_Sampling(**sub) for sub in subs.values()))

        return result

    def generate_data(self, data_structure, count):
        for _ in range(count):
            print(self.data_Sampling(**data_structure))


# 使用封装的程序
if __name__ == "__main__":
    sampler = DataSampler()
    data_structure = {
        "dataType": "tuple",
        "subs": {
            "sub1": {
                "dataType": "list",
                "subs": {
                    "sub1": {
                        "dataType": "int",
                        "datarange": (0, 100)
                    },
                    "sub2": {
                        "dataType": "str",
                        "datarange": string.ascii_letters,
                        "len": 5
                    }
                }
            },
            "sub2": {
                "dataType": "tuple",
                "subs": {
                    "sub1": {
                        "dataType": "float",
                        "datarange": (0, 5000)
                    },
                    "sub2": {
                        "dataType": "int",
                        "datarange": (1, 200)
                    }
                }
            },
            "sub3": {
                "dataType": "str",
                "datarange": string.ascii_letters,
                "len": 3,
            }
        }
    }
    count = int(input("请输入需要生成的数据组数："))
    sampler.generate_data(data_structure, count)