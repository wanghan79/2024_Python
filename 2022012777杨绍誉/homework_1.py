import random
import string

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

def generate_random_data(**kwargs):
    # 从关键字参数中获取数据规范
    data = kwargs.get("data")
    # 根据数据类型生成相应的随机数据
    if data["datatype"] == int:
        # 生成一个指定范围内的随机整数
        return random.randint(data["datarange"][0], data["datarange"][1])
    elif data["datatype"] == float:
        # 生成一个指定范围内的随机浮点数
        return random.uniform(data["datarange"][0], data["datarange"][1])
    elif data["datatype"] == str:
        # 生成一个随机字符串
        if isinstance(data["datarange"], str):
            # 如果datarange是一个字符串，则从中选择字符
            data_len = data["strlength"]
            return ''.join(random.choices(data["datarange"], k=data_len))
        else:
            # 如果datarange是一个列表，则从中选择一个元素
            r_index = random.randint(0, len(data["datarange"]) - 1)
            return data["datarange"][r_index]
    elif data["datatype"] == tuple:
        # 生成一个包含随机数据的元组
        result = {}
        for key, value in data["subs"].items():
            result[key] = generate_random_data(data=value)
        return result
    elif data["datatype"] == list:
        # 生成一个包含随机数据的列表
        size = data["subs"]["size"]
        return [generate_random_data(data=data["subs"]) for _ in range(size)]
    elif data["datatype"] == dict:
        # 生成一个包含随机数据的字典
        return {key: generate_random_data(data=value) for key, value in data["subs"].items()}
    elif data["datatype"] == set:
        # 生成一个包含随机数据的集合
        size = data["subs"]["size"]
        return {generate_random_data(data=data["subs"]) for _ in range(size)}


random_data = generate_random_data(data=data)
print(random_data)
