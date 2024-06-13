import random
import string

# 定义数据结构
data_structure = {
    "datatype": tuple,
    "subs": {
        "sub1": {
            "datatype": list,
            "subs": {
                "sub1": {
                    "datatype": str,
                    "datarange": string.ascii_letters
                },
                "sub2": {
                    "datatype": int,
                    "datarange": (0, 100)
                }
            }
        },
        "sub2": {
            "datatype": list,
            "subs": {
                "sub1": {
                    "datatype": int,
                    "datarange": (18, 24)
                },
                "sub2": {
                    "datatype": int,
                    "datarange": (2020, 2023)
                }
            }
        },
        "sub3": {
            "datatype": list,
            "subs": {
                "sub1": {
                    "datatype": str,
                    "datarange": string.ascii_letters
                },
                "sub2": {
                    "datatype": float,
                    "datarange": (0, 5)
                }
            }
        }
    }
}

# 生成随机值的函数
def generate_random_value(datatype, datarange):
    if datatype == str:
        return ''.join(random.choice(datarange) for _ in range(10))
    elif datatype == int:
        return random.randint(datarange[0], datarange[1])
    elif datatype == float:
        return round(random.uniform(datarange[0], datarange[1]), 2)

# 生成随机数据的函数
def generate_random_data(structure):
    data = [] if structure["datatype"] == list else ()
    for sub_key, sub_value in structure["subs"].items():
        if "datarange" in sub_value:
            random_data = generate_random_value(sub_value["datatype"], sub_value["datarange"])
        else:
            random_data = generate_random_data(sub_value)
        if isinstance(data, tuple):
            data += (random_data,)
        else:
            data.append(random_data)
    return data

# 生成随机学生信息的函数
def generate_random_students(num_students):
    return [generate_random_data(data_structure) for _ in range(num_students)]

# 随机生成1到100个学生数据
random_students = generate_random_students(random.randint(1, 100))
print(random_students)
