import random
import string
def random_data():
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
    while True:
        yield dataSampling(**data_structure)

num=int(input("请输入要生成的数据组数："))
random_data_gen = random_data()
samples = [next(random_data_gen) for _ in range(num)]
print(samples)
# for sample in samples:
#     print(sample)
