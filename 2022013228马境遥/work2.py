import random
import string

class RandomData:
    def __init__(self, data_structure):
        self.data_structure = data_structure

    def random_value(self, kwargs):
        datatype = kwargs['datatype']
        if datatype == int:
            return random.randint(*kwargs['datarange'])
        elif datatype == float:
            return random.uniform(*kwargs['datarange'])
        elif datatype == str:
            if isinstance(kwargs['datarange'], str):
                return random.choice(kwargs['datarange'])
            else:
                length = kwargs['datarange']
                return ''.join(random.choice(string.ascii_letters) for _ in range(length))
        elif datatype == list:
            return [self.random_value(sub_kwargs) for sub_kwargs in kwargs['subs'].values()]
        elif datatype == tuple:
            return tuple(self.random_value(sub_kwargs) for sub_kwargs in kwargs['subs'].values())

    def traverse_dict(self):
        results = {}
        for key, value in self.data_structure['subs'].items():
            result = self.random_value(value)
            results[key] = result
        return results

    def generate_random(self, num):
        return [self.traverse_dict() for _ in range(num)]

# 定义数据结构
structure = {
    'datatype': tuple,
    'subs': {
        'sub1': {
            'datatype': list,
            'subs': {
                'sub1': {
                    'datatype': int,
                    'datarange': (0, 100)
                },
                'sub2': {
                    'datatype': str,
                    'datarange': string.ascii_uppercase
                },
            }
        },
        'sub2': {
            'datatype': list,
            'subs': {
                'sub1': {
                    'datatype': float,
                    'datarange': (0, 5000)
                },
                'sub2': {
                    'datatype': int,
                    'datarange': (0, 200)
                },
            },
        },
        'sub3': {
            'datatype': str,
            'datarange': string.ascii_uppercase
        }
    }
}

generator = RandomData(structure)
random_values_list = generator.generate_random(5)

# 打印结果
for i, random_values in enumerate(random_values_list):
    print(f"{i+1}: {random_values}")