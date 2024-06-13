import random
import string


def Sat(*args):
    def decorator(func):
        def wrapper(**kwargs):
            data = func(**kwargs)
            print(data)
            for item in args:
                Analysis(data, item)

        return wrapper

    return decorator


def Analysis(data, args):
    def data_search(data):
        data_list = []
        count = 0
        for item in data:
            if isinstance(item, (int, float)):
                data_list.append(item)
                count += 1
            elif isinstance(item, (tuple, list)) and len(item) > 0:
                new_list, new_count = data_search(item)
                data_list.extend(new_list)
                count += new_count
        return data_list, count

    data_list, count = data_search(data)

    # print(data_list)

    def data_sum_func(data_list):
        data_sum = 0
        for i in data_list:
            data_sum += i
        return data_sum

    def data_ave_func(count):
        data_sum = data_sum_func(data_list)
        return data_sum / count if count > 0 else 0

    if args == 'sum':
        print(f"sum:{data_sum_func(data_list)}")
    if args == 'ave':
        print(f"average:{data_ave_func(count)}")
    if args == 'max':
        print(f"max:{max(data_list)}")


@Sat('sum', 'ave', 'max')
def dataSampling(**kwargs):
    results = []
    for i in range(kwargs['num']):
        result = dataRange(kwargs['struct'])
        results.append(result)
    return results


def dataRange(kwargs):
    if kwargs['datatype'] == 'int':
        it = iter(kwargs['datarange'])
        return random.randint(next(it), next(it))
    elif kwargs['datatype'] == 'float':
        it = iter(kwargs['datarange'])
        return random.uniform(next(it), next(it))
    elif kwargs['datatype'] == 'str':
        if isinstance(kwargs['datarange'], str):
            # 从给定的字符串中随机选择字符来构建新字符串
            return ''.join(random.choice(kwargs['datarange']) for _ in range(random.randint(1, len(kwargs['datarange']))))
        elif isinstance(kwargs['datarange'], int):
            # 生成一个固定长度的随机字符串，该字符串由ASCII字母组成
            return ''.join(random.SystemRandom().choice(string.ascii_letters) for _ in range(kwargs['datarange']))
    elif kwargs['datatype'] in ('list', 'tuple'):
        elements = []
        for sub_key, sub_kwargs in kwargs['subs'].items():
            elements.append(dataRange(sub_kwargs))
        if kwargs['datatype'] == 'list':
            return elements
        else:  # tuple
            return tuple(elements)

if __name__ == '__main__':

    para = {"num": 3,
            "struct": {
                "datatype": "tuple",
                "subs": {
                    "sub1": {
                        "datatype": "tuple",
                        "subs": {
                            "sub1": {
                                "datatype": "int",
                                "datarange": (0, 100)
                            },
                            "sub2": {
                                "datatype": "str",
                                "datarange": "abcd"
                            }
                        }
                    },
                    "sub2": {
                        "datatype": "tuple",
                        "subs": {
                            "sub1": {
                                "datatype": "float",
                                "datarange": (0, 5000)
                            },
                            "sub2": {
                                "datatype": "int",
                                "datarange": (1, 200)
                            }
                        }
                    },
                    "sub3": {
                        "datatype": "str",
                        "datarange": "efgh"
                    }
                }
            }
            }

    dataSampling(**para)
