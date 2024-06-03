import random
import string

def generate_random_data(**kwargs):
    data = kwargs.get("data")
    if data["datatype"] == int:
        yield random.randint(data["datarange"][0], data["datarange"][1])
    elif data["datatype"] == float:
        yield random.uniform(data["datarange"][0], data["datarange"][1])
    elif data["datatype"] == str:
        if isinstance(data["datarange"], str):
            data_len = data["strlength"]
            while True:  # 无限生成字符串
                yield ''.join(random.choices(data["datarange"], k=data_len))
        else:
            while True:  # 无限选择列表中的元素
                r_index = random.randint(0, len(data["datarange"]) - 1)
                yield data["datarange"][r_index]
    elif data["datatype"] == tuple:
        while True:  # 无限生成元组数据
            result = {}
            for key, value in data["subs"].items():
                result[key] = next(generate_random_data(data=value))
            yield result
    elif data["datatype"] == list:
        size = data["subs"]["size"]
        while True:  # 无限生成列表
            yield [next(generate_random_data(data=data["subs"])) for _ in range(size)]
    elif data["datatype"] == dict:
        while True:  # 无限生成字典
            yield {key: next(generate_random_data(data=value)) for key, value in data["subs"].items()}
    elif data["datatype"] == set:
        size = data["subs"]["size"]
        while True:  # 无限生成集合
            yield {next(generate_random_data(data=data["subs"])) for _ in range(size)}

data = {
    "datatype": tuple,
    "subs": {
        "Sub1": {
            "datatype": int,
            "datarange": (0, 100)
        },
        "Sub2": {
            "datatype": str,
            "datarange": string.ascii_uppercase,
            "strlength": 5
        },
        "Sub3": {
            "datatype": tuple,
            "subs": {
                "Sub1": {
                    "datatype": float,
                    "datarange": (0, 5008)
                },
                "Sub2": {
                    "datatype": int,
                    "datarange": (1, 200)
                },
                "Sub3": {
                    "datatype": str,
                    "datarange": string.ascii_uppercase,
                    "strlength": 5
                }
            }
        },
        "Sub4": {
            "datatype": list,
            "subs": {
                "datatype": int,
                "size":5,
                "datarange": (0, 50)
            }
        },
        "Sub5": {
            "datatype": dict,
            "subs": {
                "key1": {
                    "datatype": str,
                    "datarange": string.ascii_lowercase,
                    "strlength": 5
                },
                "key2": {
                    "datatype": float,
                    "datarange": (0, 1000)
                }
            }
        },
        "Sub6": {
            "datatype": set,
            "subs": {
                "size":3,
                "datatype": str,
                "datarange": ("Chongqing", "Sichuan", "Hubei", "Jilin", "Heilongjiang", "Shaanxi")
            }
        }
    }
}


# 创建生成器实例
gen = generate_random_data(data=data)
print(next(gen))


