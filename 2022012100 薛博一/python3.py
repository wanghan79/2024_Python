import random
import string
from collections import defaultdict

float_group = []
int_group = []
def statistics(stats):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
# 初始化stats字典
stats = defaultdict(int)
@statistics(stats)
def dataSampling(**kwargs):
    if kwargs['datatype'] == 'int':
        it = iter(kwargs['datarange'])
        return random.randint(next(it), next(it))
    elif kwargs['datatype'] == 'float':
        it = iter(kwargs['datarange'])
        return random.uniform(next(it), next(it))
    elif kwargs['datatype'] == 'str':
        if isinstance(kwargs['datarange'], str):
            return random.choice(kwargs['datarange'])
        elif isinstance(kwargs['datarange'], int):
            return ''.join(random.SystemRandom().choice(string.ascii_letters) for _ in range(kwargs['datarange']))
    elif kwargs['datatype'] in ('list', 'tuple'):
        elements = []
        for sub_key, sub_kwargs in kwargs['subs'].items():
            elements.append(dataSampling(**sub_kwargs))
        if kwargs['datatype'] == 'list':
            return elements
        else:
            return tuple(elements)

def sum_data(results):
    total_sum=0
    for result in results:
        total_sum+=result
    return total_sum
#
def mean_data(results):
    total_sum = sum_data(results)
    count = len(results)
    return total_sum / count if count else 0
def count_data(data):
    if isinstance(data, (list, tuple)):
        for item in data:
            count_data(item)
    elif isinstance(data, float):
        float_group.append(data)
        stats[type(data).__name__] += 1
    elif isinstance(data, int):
        int_group.append(data)
        stats[type(data).__name__] += 1
def operation(option):
    dic = {}
    if option == 'both':
        dic.setdefault('int_sum',sum_data(int_group))
        dic.setdefault('float_sum',sum_data(float_group))
        dic.setdefault('int_mean',mean_data(int_group))
        dic.setdefault('float_mean',mean_data(float_group))
    elif option == 'sum':
        dic.setdefault('int_sum',sum_data(int_group))
        dic.setdefault('float_sum',sum_data(float_group))
    elif option == 'mean':
        dic.setdefault('int_mean',mean_data(int_group))
        dic.setdefault('float_mean',mean_data(float_group))
    return dic

data_structure = {
            "datatype": "tuple",
            "subs": {
                "sub1": {"datatype": "tuple",
                          "subs": {"sub1": {"datatype": "int","datarange": (0, 500)},
                                   "sub2": {"datatype": "str","datarange": string.ascii_letters }}
                        },
                "sub2": {
                    "datatype": "list",
                    "subs": {"sub1": {"datatype": "float","datarange": (0, 2000) },
                             "sub2": {"datatype": "int","datarange": (1, 250)} }
                        },
                "sub3": {
                    "datatype": "str","datarange": string.ascii_letters
                        }
                    }
                }

num=int(input("请输入要生成的数据组数："))
option = input("请选择要进行的操作（sum/average/both）：")
samples = [dataSampling(**data_structure) for _ in range(num)]
count_data(samples)
for sample in samples:
    print(sample)
# print(int_group)
# print(float_group)
print("随机数类型统计（int和float）:", dict(stats))
print(operation(option))
