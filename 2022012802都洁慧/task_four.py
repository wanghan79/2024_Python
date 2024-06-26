import random
import string
import sys


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
            return ''.join(
                random.choice(kwargs['datarange']) for _ in range(random.randint(1, len(kwargs['datarange']))))
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


def dataSampling(**kwargs):
    counter = 1
    while True:
        if counter > kwargs['num']:
            return
        yield dataRange(kwargs['struct'])
        counter += 1


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

    example = dataSampling(**para)
    # for x in example:
    #     print((x))
    while True:
        try:
            print(next(example))
        except StopIteration:
            sys.exit()
