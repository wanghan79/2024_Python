import random
import string


def dataSampling(**kwargs):
    result = []
    for key, specs in kwargs.items():
        if key == 'int':
            range_l, range_r = specs['datarange']
            result.append(random.randint(range_l, range_r))
        elif key == 'float':
            range_l, range_r = specs['datarange']
            result.append(random.uniform(range_l, range_r))
        elif key == 'str':
            chars = specs['datarange']
            length = specs['len']
            result.append(''.join(random.choice(chars) for _ in range(length)))
        elif key == 'tuple':
            tuple_elements = [dataSampling(**{k: v} if isinstance(v, dict) else v) for k, v in specs.items()]
            result.append(tuple(tuple_elements))
        elif key == 'list':
            list_elements = [dataSampling(**specs) for _ in range(specs.get('count', 1))]
            result.append(list_elements)
    return result


def dataScreening(num, data_type=None, datarange=None, length=None, **kwargs):
    screened_data = []
    for _ in range(num):
        if data_type is not None:
            if data_type == 'str':
                result = ''.join(random.choice(datarange) for _ in range(length))
            elif data_type == 'int':
                range_s, range_e = datarange
                result = random.randint(range_s, range_e)
            elif data_type == 'float':
                range_s, range_e = datarange
                result = random.uniform(range_s, range_e)
        else:
            result = dataSampling(**kwargs)
        screened_data.append(result)
    return screened_data


# 使用示例
def apply01():
    result = dataScreening(10, 'str', string.ascii_letters + string.digits + "@#$!", 5)
    print(result)
    print("\n")


def apply02():
    result = dataScreening(10, 'float', (-100, 100))
    print(result)
    print("\n")


def apply03():
    struct = {"int": {"datarange": (0, 10)}, "float": {"datarange": (0, 10)}}
    result = dataScreening(3, **struct)
    for item in result:
        print(item)
    print("\n")


def apply04():
    struct = {
        'int': {'datarange': [1, 10]},
        'float': {'datarange': [1.0, 10.0]},
        'tuple': {
            'int': {'datarange': [1, 100]},
            'str': {'datarange': string.ascii_uppercase, 'len': 0}
        },
        'list': {
            'int': {'datarange': [1, 100]},
            'str': {'datarange': string.ascii_lowercase, 'len': 8},
            'float': {'datarange': [1.0, 10.0]}
        }
    }
    result = dataScreening(3, **struct)
    for item in result:
        print(item)


apply01()
apply02()
apply03()
apply04()
