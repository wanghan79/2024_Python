import random
import string


def dataSampling(kwargs):
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
            elements.append(dataSampling(sub_kwargs))
        if kwargs['datatype'] == 'list':
            return elements
        else:
            return tuple(elements)


def apply(**kwargs):
    results = []
    for i in range(kwargs['num']):
        result = dataSampling(kwargs['struct'])
        results.append(result)
    return results


para = {"num": 5,
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
print(apply(**para))