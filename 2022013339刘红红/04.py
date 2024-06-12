import random
import string
import math
from functools import wraps

# 定义各个统计修饰器
def calculate_sum(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        results = list(func(self, *args, **kwargs))
        flat_data = self.flatten(results)
        numeric_data = [x for x in flat_data if isinstance(x, (int, float))]
        self.sum = sum(numeric_data)
        return results
    return wrapper

def calculate_average(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        results = list(func(self, *args, **kwargs))
        flat_data = self.flatten(results)
        numeric_data = [x for x in flat_data if isinstance(x, (int, float))]
        self.average = sum(numeric_data) / len(numeric_data) if numeric_data else None
        return results
    return wrapper

def calculate_max(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        results = list(func(self, *args, **kwargs))
        flat_data = self.flatten(results)
        numeric_data = [x for x in flat_data if isinstance(x, (int, float))]
        self.max_value = max(numeric_data) if numeric_data else None
        return results
    return wrapper

def calculate_min(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        results = list(func(self, *args, **kwargs))
        flat_data = self.flatten(results)
        numeric_data = [x for x in flat_data if isinstance(x, (int, float))]
        self.min_value = min(numeric_data) if numeric_data else None
        return results
    return wrapper

def calculate_product(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        results = list(func(self, *args, **kwargs))
        flat_data = self.flatten(results)
        numeric_data = [x for x in flat_data if isinstance(x, (int, float))]
        self.product = math.prod(numeric_data) if numeric_data else None
        return results
    return wrapper

class Random:
    def __init__(self, num, struct):
        self.num = num
        self.struct = struct
        self.data = None
        self.sum = None
        self.average = None
        self.max_value = None
        self.min_value = None
        self.product = None

    @calculate_sum
    @calculate_average
    @calculate_max
    @calculate_min
    @calculate_product
    def generate_data(self):
        for _ in range(self.num):
            yield self._random_data(self.struct)

    def _random_data(self, kwargs):
        data_type = kwargs['datatype']
        if data_type == 'int':
            return random.randint(*kwargs['datarange'])
        elif data_type == 'float':
            return random.uniform(*kwargs['datarange'])
        elif data_type == 'str':
            if isinstance(kwargs['datarange'], str):
                return random.choice(kwargs['datarange'])
            elif isinstance(kwargs['datarange'], int):
                return ''.join(random.SystemRandom().choice(string.ascii_letters) for _ in range(kwargs['datarange']))
        elif data_type == 'list':
            data = []
            for sub_kwargs in kwargs['subs'].values():
                data.append(self._random_data(sub_kwargs))
            return data
        elif data_type == 'tuple':
            data = ()
            for sub_kwargs in kwargs['subs'].values():
                data += (self._random_data(sub_kwargs),)
            return data

    def flatten(self, data):
        flat_list = []
        if isinstance(data, (list, tuple)):
            for item in data:
                flat_list.extend(self.flatten(item))
        else:
            flat_list.append(data)
        return flat_list

# 实例测试
para0 = {
    "num": 5,
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

para1 = {
    "num": 2,
    "struct": {
        "datatype": "list",
        "subs": {
            "sub1": {
                "datatype": "tuple",
                "subs": {
                    "sub1": {
                        "datatype": "int",
                        "datarange": (0, 100)
                    },
                    "sub2": {
                        "datatype": "int",
                        "datarange": (0, 100)
                    }
                }
            }
        }
    }
}

para2 = {
    "num": 1,
    "struct": {
        "datatype": "tuple",
        "subs": {
            "sub1": {
                "datatype": "str",
                "datarange": "abcdef"
            },
            "sub2": {
                "datatype": "str",
                "datarange": "123456"
            },
            "sub3": {
                "datatype": "str",
                "datarange": "uvwxyz"
            },
            "sub4": {
                "datatype": "str",
                "datarange": "ABCDEFG"
            },
            "sub5": {
                "datatype": "str",
                "datarange": "7890"
            }
        }
    }
}

para3 = {
    "num": 1,
    "struct": {
        "datatype": "list",
        "subs": {
            "sub1": {
                "datatype": "tuple",
                "subs": {
                    "sub1": {
                        "datatype": "float",
                        "datarange": (0, 100)
                    },
                    "sub2": {
                        "datatype": "float",
                        "datarange": (0, 100)
                    },
                    "sub3": {
                        "datatype": "float",
                        "datarange": (0, 100)
                    }
                }
            },
            "sub2": {
                "datatype": "tuple",
                "subs": {
                    "sub1": {
                        "datatype": "float",
                        "datarange": (0, 100)
                    },
                    "sub2": {
                        "datatype": "float",
                        "datarange": (0, 100)
                    },
                    "sub3": {
                        "datatype": "float",
                        "datarange": (0, 100)
                    }
                }
            }
        }
    }
}

# 测试函数
def test_para(para):
    generator = Random(**para)
    generated_data = list(generator.generate_data())
    print("Data:", generated_data)
    print("Sum:", generator.sum)
    print("Average:", generator.average)
    print("Max:", generator.max_value)
    print("Min:", generator.min_value)
    print("Product:", generator.product)
    print("\n")

# 运行测试
paras = [para0, para1, para2, para3]
for i, para in enumerate(paras):
    print(f"para {i} :")
    test_para(para)
