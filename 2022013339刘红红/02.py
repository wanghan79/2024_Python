import random
import string
import math

class Random:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def random_data(self, **kwargs):
        data_type = kwargs['datatype']
        while True:
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
                    data.append(self.random_data(**sub_kwargs))
                return data
            elif data_type == 'tuple':
                data = ()
                for sub_kwargs in kwargs['subs'].values():
                    data += (self.random_data(**sub_kwargs),)
                return data

    def apply(self):
        results = []
        for _ in range(self.kwargs['num']):
            results.append(self.random_data(**self.kwargs['struct']))
        return results

    def flatten(self, data):
        flat_list = []
        if isinstance(data, (list, tuple)):
            for item in data:
                flat_list.extend(self.flatten(item))
        else:
            flat_list.append(data)
        return flat_list

    def sum(self, data):
        return sum(data)

    def average(self, data):
        return sum(data) / len(data) if data else None

    def max(self, data):
        return max(data) if data else None

    def min(self, data):
        return min(data) if data else None

    def product(self, data):
        return math.prod(data) if data else None


# 实例测试
# 生成一个元组，包含三个子元组，第一个子元组包含两个元素（整数和字符串），第二个子元组包含浮点数和整数，第三个子元素是一个字符串
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

# 生成一个包含 3 个元素的列表，每个元素都是一个包含两个随机整数的元组
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

# 生成一个包含 5 个元素的元组，每个元素都是一个随机字符串
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

# 生成一个包含 2 个元素的列表，每个元素都是一个包含 3 个随机浮点数的元组
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
    generated_data = generator.apply()
    flat_data = generator.flatten(generated_data)
    data = [x for x in flat_data if isinstance(x, (int, float))]
    print("Data:", generated_data)
    print("Sum:", generator.sum(data))
    print("Average:", generator.average(data))
    print("Max:", generator.max(data))
    print("Min:", generator.min(data))
    print("Product:", generator.product(data))
    print("\n")

# 运行测试
paras = [para0, para1, para2, para3]
for i, para in enumerate(paras):
    print(f"para {i} :")
    test_para(para)
