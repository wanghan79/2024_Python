import random
import string
from functools import wraps

class Class:
    def __init__(self, name, number, ID):
        self.name = name
        self.number = number
        self.ID = ID

    def __repr__(self):
        return f'Class name:{self.name} age:{self.number} ID:{self.ID}'

example = {
    "data_type": tuple,
    "subs": {
        "sub1": {"data_type": list,
                 "subs": {
                     "sub1": {
                         "data_type": int,
                         "data_range": (0, 1000)
                     },
                     "sub2": {
                         "data_type": str,
                         "data_range": string.ascii_uppercase,
                         "len": 10
                     }
                 },
                 },
        "sub2": {"data_type": tuple,
                 "subs": {
                     "sub1": {
                         "data_type": int,
                         "data_range": (0, 1000)
                     },
                     "sub2": {
                         "data_type": str,
                         "data_range": string.ascii_uppercase,
                         "len": 10
                     }
                 },
                 },
        "sub3": {
            "data_type": str,
            "data_range": string.ascii_lowercase,
            "len": 5
        },
        "sub4": {
            "data_type": list,
            "subs": {
                "subs": {
                    "data_type": Class,
                    "subs": {
                        "name": {
                            "data_type": str,
                            "data_range": "2024计算机",
                            "len": 10
                        },
                        "number": {
                            "data_type": int,
                            "data_range": (0, 100)
                        },
                        "ID": {
                            "data_type": int,
                            "data_range": (0, 100)
                        }
                    }
                }
            }
        }
    }
}

def int_stats(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 调用原始函数获取数据结构
        data_structure = func(*args, **kwargs)

        # 递归函数，用于寻找数据结构中的所有int类型数据
        def find_ints(data, ints):
            if isinstance(data, int):
                ints.append(data)
            elif isinstance(data, (list, tuple, set)):
                for item in data:
                    find_ints(item, ints)
            elif isinstance(data, dict):
                for value in data.values():
                    find_ints(value, ints)

        # 存储找到的int类型数据
        int_values = []
        find_ints(data_structure, int_values)

        # 计算总和和平均值
        total_sum = sum(int_values)
        average = total_sum / len(int_values) if int_values else 0

        # 返回原始数据结构以及int的总和和平均值
        return data_structure, total_sum, average

    return wrapper

class Data:
    def __init__(self, num, **kwargs):
        self.data_struct = kwargs.copy()
        self.num = num

    def __iter__(self):
        for _ in range(self.num):
            yield self.data_sampling(**self.data_struct)


# 应用修饰器
    @int_stats
    def data_sampling(self,**kwargs):
        def sample_int(data_range):
            if len(data_range) == 1:
                return data_range[0]
            else:
                return random.choice(data_range) if len(data_range) > 2 else random.randint(*data_range)

        def sample_bool(data_range):
            return data_range[0] if len(data_range) == 1 else random.random() < 0.5

        def sample_float(data_range):
            if len(data_range) == 1:
                return data_range[0]
            else:
                return random.uniform(*data_range) if len(data_range) == 2 else random.choice(data_range)

        def sample_str(data_range, length):
            return ''.join(random.choice(data_range) for _ in range(length)) if isinstance(data_range, str) else random.choice(data_range)

        def sample_collection(collection_type, items):
            return collection_type(self.data_sampling(**v) for v in items.values())

        typ = kwargs.get('data_type')
        data_range = kwargs.get('data_range')
        subs = kwargs.get('subs')
        length = kwargs.get('len')

        if typ is int:
            return sample_int(data_range)
        elif typ is bool:
            return sample_bool(data_range)
        elif typ is float:
            return sample_float(data_range)
        elif typ is str:
            return sample_str(data_range, length)
        elif typ is tuple:
            return sample_collection(tuple, subs)
        elif typ is set:
            return sample_collection(set, subs)
        elif typ is list:
            return sample_collection(list, subs)
        else:
            return typ(**{k: self.data_sampling(**v) for k, v in subs.items()})


if __name__ == '__main__':
    dso = Data(100, **example)
    for val, total_sum, average in dso:
        print(f"Sampled Data: {val}")
        print(f"Total Sum of Ints: {total_sum}")
        print(f"Average of Ints: {average}\n")