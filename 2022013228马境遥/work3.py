import random
import string
from functools import wraps

# 修饰器
def stats_decorator(func):
    @wraps(func)
    def wrapper(random_data_list, *args, **kwargs):
        # 初始化数值数据列表
        data = []
        # 遍历列表中的每个字典
        for data_set in random_data_list:
            # 遍历字典中的每个子项
            for key, value in data_set.items():
                # 如果子项是数值类型，则添加到列表中
                if isinstance(value, (int, float)):
                    data.append(value)
                # 如果子项是列表，进一步检查列表中的每个元素是否是数值类型
                elif isinstance(value, list):
                    for item in value:
                        if isinstance(item, (int, float)):
                            data.append(item)

        # 计算总和和均值
        sum_values = sum(data)
        mean_values = sum_values / len(data) if data else 0

        # 调用原始函数，并传入计算结果和其他参数
        return func(sum_values, mean_values, *args, **kwargs)

    return wrapper

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

@stats_decorator
def process_data(sum_values, mean_values, *args, **kwargs):
    print(f"求和: {sum_values}")
    print(f"均值: {mean_values}")

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

for i, random_values in enumerate(random_values_list):
    print(f"{i+1}: {random_values}")

process_data(random_values_list)