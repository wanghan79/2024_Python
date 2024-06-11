import random
import string

class Sampling:
    def dataSampling(self,**kwargs):
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
                elements.append(self.dataSampling(**sub_kwargs))
            if kwargs['datatype'] == 'list':
                return elements
            else:  # tuple
                return tuple(elements)
    def generate_data(self,num):
        results = []
        for i in range(num):
            result = self.dataSampling(**nested_structure)
            results.append(result)
        return results

# 假定的嵌套模型
nested_structure = {
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
sampling=Sampling()
samples = sampling.generate_data(num)
print(samples)
