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


# 定义一个装饰器，用于计算函数返回数据的总和和平均值
def calculate_sum_and_average(func):
    # 定义包装器函数
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        # 从关键字参数中获取是否需要计算总和和平均值的标志
        calculate_sum = kwargs.get("sum", False)
        calculate_average = kwargs.get("average", False)

        # 如果需要计算总和和平均值
        if calculate_sum and calculate_average:
            # 计算数据的总和
            total_sum = _calculate_sum(data)
            # 计算数据的数量
            total_count = _calculate_count(data)
            # 计算平均值
            average = total_sum / total_count if total_count > 0 else 0
            # 返回原始数据、总和和平均值
            return data, total_sum, average
        # 如果只需要计算总和
        elif calculate_sum:
            # 计算数据的总和
            total_sum = _calculate_sum(data)
            # 返回原始数据和总和
            return data, total_sum
        # 如果只需要计算平均值
        elif calculate_average:
            # 计算数据的数量
            total_count = _calculate_count(data)
            # 计算平均值
            average = total_sum / total_count if total_count > 0 else 0
            # 返回原始数据和平均值
            return data, average
        # 如果不需要计算总和和平均值
        else:
            # 只返回原始数据
            return data

    # 定义一个辅助函数，用于计算数据的总和
    def _calculate_sum(data):
        total_sum = 0
        # 如果数据是整数或浮点数
        if isinstance(data, (int, float)):
            # 直接将数据作为总和
            total_sum = data
        # 如果数据是字典
        elif isinstance(data, dict):
            # 遍历字典的值
            for value in data.values():
                # 递归计算值的总和
                total_sum += _calculate_sum(value)
        # 如果数据是列表或元组
        elif isinstance(data, (list, tuple)):
            # 遍历列表的元素
            for element in data:
                # 递归计算元素的总和
                total_sum += _calculate_sum(element)
        # 返回总和
        return total_sum

    # 定义一个辅助函数，用于计算数据的数量
    def _calculate_count(data):
        total_count = 0
        # 如果数据是整数或浮点数
        if isinstance(data, (int, float)):
            # 数量为1
            total_count = 1
        # 如果数据是字典
        elif isinstance(data, dict):
            # 遍历字典的值
            for value in data.values():
                # 递归计算值的数量
                total_count += _calculate_count(value)
        # 如果数据是列表或元组
        elif isinstance(data, (list, tuple)):
            # 遍历列表的元素
            for element in data:
                # 递归计算元素的数量
                total_count += _calculate_count(element)
        # 返回数量
        return total_count

    # 返回包装器函数
    return wrapper



@calculate_sum_and_average
def generate_random_data(**kwargs):
    data = kwargs.get("data")
    if data["datatype"] == int:
        return random.randint(data["datarange"][0], data["datarange"][1])
    elif data["datatype"] == float:
        return random.uniform(data["datarange"][0], data["datarange"][1])
    elif data["datatype"] == str:
        if isinstance(data["datarange"], str):
            data_len = data["strlength"]
            return ''.join(random.choices(data["datarange"], k=data_len))
        else:
            r_index = random.randint(0, len(data["datarange"]) - 1)
            return data["datarange"][r_index]
    elif data["datatype"] == tuple:
        result = {}
        for key, value in data["subs"].items():
            result[key] = generate_random_data(data=value)
        return result
    elif data["datatype"] == list:
        size = data["subs"]["size"]
        return [generate_random_data(data=data["subs"]) for _ in range(size)]
    elif data["datatype"] == dict:
        return {key: generate_random_data(data=value) for key, value in data["subs"].items()}
    elif data["datatype"] == set:
        size = data["subs"]["size"]
        return {generate_random_data(data=data["subs"]) for _ in range(size)}


result = generate_random_data(data=data, sum=True, average=True)
print("Generated Data:", result[0])
print("Total Sum:", result[1])
print("Average:", result[2])