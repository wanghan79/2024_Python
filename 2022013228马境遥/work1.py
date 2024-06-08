import random
import string

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

def random_value(kwargs):
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
        return [random_value(sub_kwargs) for sub_kwargs in kwargs['subs'].values()]
    elif datatype == tuple:
        return tuple(random_value(sub_kwargs) for sub_kwargs in kwargs['subs'].values())

def traverse_dict(struct):
    results = {}
    for key, value in struct['subs'].items():
        result = random_value(value)
        results[key] = result
    return results

# 生成五组随机数
random_values_list = [traverse_dict(structure) for _ in range(5)]

for i, random_values in enumerate(random_values_list):
    print(f"{i+1}: {random_values}")


