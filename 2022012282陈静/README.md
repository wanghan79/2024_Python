# Python作业

学生姓名：陈静

学号：2022012282

github地址：https://github.com/Florae006



## Sample Input

```python
# input
test_data = {
    "datatype": "tuple",
    "subs": {
        "sub1": {
            "datatype": "list",
            "subs": {
                "sub1": {
                    "datatype": "int",
                    "datarange": (0, 100)
                },
                "sub2": {
                    "datatype": "str",
                    "datarange": "this is a string"
                }
            }
        },
        "sub2": {
            "datatype": "tuple",
            "subs": {
                "sub1": {
                    "datatype": "float",
                    "datarange": (0.0, 100.0)
                },
                "sub2": {
                    "datatype": "bool",
                    "datarange": (True, False)
                }
            }
        }
    }
}

# output
([49, 'i'], (90.96790581086461, True))
```



## 作业 1

给定一个带有类型描述和值范围的复杂结构数据，要求写一个程序实现随机数据生成的功能。

### 代码:dataStructure_class.py

```python
import string
import random

def generate_random_data(**kwargs):
    data_structure = kwargs.get("data_structure")
    datatype = data_structure["datatype"]
    if datatype == tuple:
        return generate_random_tuple(data_structure["subs"])
    elif datatype == list:
        return generate_random_list(data_structure["subs"])
    elif datatype == str:
        return generate_random_string(data_structure["datarange"])
    elif datatype == int:
        return generate_random_int(data_structure["datarange"])
    elif datatype == float:
        return generate_random_float(data_structure["datarange"])

def generate_random_tuple(subs):
    data = {}
    for key, value in subs.items():
        data[key] = generate_random_data(data_structure=value)
    return data

def generate_random_list(subs):
    data = []
    for _ in range(random.randint(1, 5)):
        item = {}
        for key, value in subs.items():
            item[key] = generate_random_data(data_structure=value)
        data.append(item)
    return data

def generate_random_int(datarange):
    range_l = datarange[0]
    range_r = datarange[1]
    return random.randint(range_l, range_r)

def generate_random_float(datarange):
    range_l = datarange[0]
    range_r = datarange[1]
    return random.uniform(range_l, range_r)

def generate_random_string(datarange):
    return ''.join(random.choice(datarange) for _ in range(random.randint(5, 10)))

dataStructure = {
    "datatype": tuple,
    "subs": {
        "sub1": {
            "datatype": list,
            "subs": {
                "sub1": {
                    "datatype": float,
                    "datarange": (0, 5000),
                },
                "sub2": {
                    "datatype": int,
                    "datarange": (0, 50),
                }
            }
        },
        "sub2": {
            "datatype": str,
            "datarange": string.ascii_uppercase,
        },
        "sub3": {
            "datatype": tuple,
            "subs": {
                "sub1": {
                    "datatype": int,
                    "datarange": (0, 100),
                },
                "sub2": {
                    "datatype": str,
                    "datarange": string.ascii_lowercase,
                },
                "sub3": {
                    "datatype": str,
                    "datarange": string.digits,
                }
            }
        }
    }
}

random_data = generate_random_data(data_structure=dataStructure)
print(random_data)

```

### 运行结果

控制台输出：

```plaintext
{'sub1': [{'sub1': 153.24106293769069, 'sub2': 42}, {'sub1': 1766.158693483153, 'sub2': 35}, {'sub1': 2700.102419728088, 'sub2': 13}], 'sub2': 'FPFQLEZLOL', 'sub3': {'sub1': 14, 'sub2': 'qnwiqmpj', 'sub3': '8780247'}}
```

运行截图：

![96198c81600df84693b9a5dc94720465](https://img.dodolalorc.cn/i/2024/06/11/66684a899c8b0.png)

## 作业 2:dataStructure_class.py

在作业 1 的基础上使用类封装程序

### 代码

```python
import random
import string

class RandomDataGenerator:
    def __init__(self, **kwargs):
        self.data_structure = kwargs.get("data_structure")

    def generate_random_data(self):
        return self._generate_random_data(self.data_structure)

    def _generate_random_data(self, data_structure):
        datatype = data_structure["datatype"]
        if datatype == tuple:
            return self.generate_random_tuple(data_structure["subs"])
        elif datatype == list:
            return self.generate_random_list(data_structure["subs"])
        elif datatype == str:
            return self.generate_random_string(data_structure["datarange"])
        elif datatype == int:
            return self.generate_random_int(data_structure["datarange"])
        elif datatype == float:
            return self.generate_random_float(data_structure["datarange"])

    def generate_random_tuple(self, subs):
        data = {}
        for key, value in subs.items():
            data[key] = self._generate_random_data(value)
        return data

    def generate_random_list(self, subs):
        data = []
        for _ in range(random.randint(1, 5)):
            item = {}
            for key, value in subs.items():
                item[key] = self._generate_random_data(value)
            data.append(item)
        return data

    def generate_random_int(self, datarange):
        range_l = datarange[0]
        range_r = datarange[1]
        return random.randint(range_l, range_r)

    def generate_random_float(self, datarange):
        range_l = datarange[0]
        range_r = datarange[1]
        return random.uniform(range_l, range_r)

    def generate_random_string(self, datarange):
        return ''.join(random.choice(datarange) for _ in range(random.randint(5, 10)))

dataStructure = {
    "datatype": tuple,
    "subs": {
        "sub1": {
            "datatype": list,
            "subs": {
                "sub1": {
                    "datatype": float,
                    "datarange": (0, 5000),
                },
                "sub2": {
                    "datatype": int,
                    "datarange": (0, 50),
                }
            }
        },
        "sub2": {
            "datatype": str,
            "datarange": string.ascii_uppercase,
        },
        "sub3": {
            "datatype": tuple,
            "subs": {
                "sub1": {
                    "datatype": int,
                    "datarange": (0, 100),
                },
                "sub2": {
                    "datatype": str,
                    "datarange": string.ascii_lowercase,
                },
                "sub3": {
                    "datatype": str,
                    "datarange": string.digits,
                }
            }
        }
    }
}

random_data_generator = RandomDataGenerator(data_structure=dataStructure)
random_data = random_data_generator.generate_random_data()
print(random_data)

```

### 运行结果

控制台输出：

```plaintext
{'sub1': [{'sub1': 623.327763468291, 'sub2': 16}], 'sub2': 'YWBHVDNZ', 'sub3': {'sub1': 62, 'sub2': 'fkepqc', 'sub3': '74796'}}
```

运行截图：

![1718110893335](https://img.dodolalorc.cn/i/2024/06/11/66684ab554296.png)

## 作业 3:dataStructure_decorator.py

在前面作业的基础上使用装饰器实现对各类型数据计数的功能

### 代码

```python
import string
import random

dataStructure = {
    "datatype": tuple,
    "subs": {
        "sub1": {
            "datatype": list,
            "subs": {
                "sub1": {
                    "datatype": float,
                    "datarange": (0, 5000),
                },
                "sub2": {
                    "datatype": int,
                    "datarange": (0, 50),
                }
            }
        },
        "sub2": {
            "datatype": str,
            "datarange": string.ascii_uppercase,
        },
        "sub3": {
            "datatype": tuple,
            "subs": {
                "sub1": {
                    "datatype": int,
                    "datarange": (0, 100),
                },
                "sub2": {
                    "datatype": str,
                    "datarange": string.ascii_lowercase,
                },
                "sub3": {
                    "datatype": str,
                    "datarange": string.digits,
                }
            }
        }
    }
}

def count_calls(func):
    counts = {}

    def wrapper(*args, **kwargs):
        data_type = func.__name__
        if data_type in counts:
            counts[data_type] += 1
        else:
            counts[data_type] = 1
        return func(*args, **kwargs)

    wrapper.counts = counts
    return wrapper

@count_calls
def generate_random_data(**kwargs):
    data_structure = kwargs.get("data_structure")
    datatype = data_structure["datatype"]
    if datatype == tuple:
        return generate_random_tuple(data_structure["subs"])
    elif datatype == list:
        return generate_random_list(data_structure["subs"])
    elif datatype == str:
        return generate_random_string(data_structure["datarange"])
    elif datatype == int:
        return generate_random_int(data_structure["datarange"])
    elif datatype == float:
        return generate_random_float(data_structure["datarange"])

def generate_random_tuple(subs):
    data = {}
    for key, value in subs.items():
        data[key] = generate_random_data(data_structure=value)
    return data

def generate_random_list(subs):
    data = []
    for _ in range(random.randint(1, 5)):
        item = {}
        for key, value in subs.items():
            item[key] = generate_random_data(data_structure=value)
        data.append(item)
    return data

def generate_random_int(datarange):
    range_l = datarange[0]
    range_r = datarange[1]
    return random.randint(range_l, range_r)

def generate_random_float(datarange):
    range_l = datarange[0]
    range_r = datarange[1]
    return random.uniform(range_l, range_r)

def generate_random_string(datarange):
    return ''.join(random.choice(datarange) for _ in range(random.randint(5, 10)))

random_data = generate_random_data(data_structure=dataStructure)
print(random_data)
print(generate_random_data.counts)

```



### 运行结果

控制台输出：

```plaintext
{'sub1': [{'sub1': 521.5030608578436, 'sub2': 16}], 'sub2': 'BQQVFLBGE', 'sub3': {'sub1': 86, 'sub2': 'qyqka', 'sub3': '15627461'}}
{'generate_random_data': 9}
```

运行截图：

![4e4b2609c14d3f1a5057a906254bb1cd](https://img.dodolalorc.cn/i/2024/06/11/6668521c9edad.png)

## 作业 4:dataStructure_yield.py

使用迭代器和生成器改进前面的作业

### 代码

```python
import string
import random

def generate_random_data(**kwargs):
    data_structure = kwargs.get("data_structure")
    datatype = data_structure["datatype"]
    if datatype == tuple:
        yield from generate_random_tuple(data_structure["subs"])
    elif datatype == list:
        yield from generate_random_list(data_structure["subs"])
    elif datatype == str:
        yield from generate_random_string(data_structure["datarange"])
    elif datatype == int:
        yield from generate_random_int(data_structure["datarange"])
    elif datatype == float:
        yield from generate_random_float(data_structure["datarange"])

def generate_random_tuple(subs):
    data = {}
    for key, value in subs.items():
        data[key] = list(generate_random_data(data_structure=value))
    yield data

def generate_random_list(subs):
    for _ in range(random.randint(1, 5)):
        item = {}
        for key, value in subs.items():
            item[key] = list(generate_random_data(data_structure=value))
        yield item

def generate_random_int(datarange):
    range_l = datarange[0]
    range_r = datarange[1]
    yield random.randint(range_l, range_r)

def generate_random_float(datarange):
    range_l = datarange[0]
    range_r = datarange[1]
    yield random.uniform(range_l, range_r)

def generate_random_string(datarange):
    yield ''.join(random.choice(datarange) for _ in range(random.randint(5, 10)))

dataStructure = {
    "datatype": tuple,
    "subs": {
        "sub1": {
            "datatype": list,
            "subs": {
                "sub1": {
                    "datatype": float,
                    "datarange": (0, 5000),
                },
                "sub2": {
                    "datatype": int,
                    "datarange": (0, 50),
                }
            }
        },
        "sub2": {
            "datatype": str,
            "datarange": string.ascii_uppercase,
        },
        "sub3": {
            "datatype": tuple,
            "subs": {
                "sub1": {
                    "datatype": int,
                    "datarange": (0, 100),
                },
                "sub2": {
                    "datatype": str,
                    "datarange": string.ascii_lowercase,
                },
                "sub3": {
                    "datatype": str,
                    "datarange": string.digits,
                }
            }
        }
    }
}

random_data = list(generate_random_data(data_structure=dataStructure))
print(random_data)

```



### 运行结果

控制台输出：

```plaintext
[{'sub1': [{'sub1': [3473.330939551449], 'sub2': [25]}, {'sub1': [465.1036971750361], 'sub2': [24]}, {'sub1': [3047.3534560277944], 'sub2': [19]}, {'sub1': [1475.7552442410592], 'sub2': [33]}, {'sub1': [264.42250484342065], 'sub2': [11]}], 'sub2': ['GJMWTXJ'], 'sub3': [{'sub1': [55], 'sub2': ['biwbpq'], 'sub3': ['57054180']}]}]

```

运行结果：

![d12cc090cbc8e410f7eb75b3d6b272ec](https://img.dodolalorc.cn/i/2024/06/11/66684fe491fa2.png)
