import random
import string

data_structure = {
    "datatype": tuple,
    "subs": {
        "sub1": {
            "datatype": list,
            "subs": {
                # 学生姓名
                "sub1": {
                    "datatype": str,
                    "datarange": string.ascii_letters
                },
                # 学生序号
                "sub2": {
                    "datatype": int,
                    "datarange": (0, 100)
                }
            }
        },
        "sub2": {
            "datatype": list,
            "subs": {
                # 学生年龄
                "sub1": {
                    "datatype": int,
                    "datarange": (18, 24)
                },
                # 入学年份
                "sub2": {
                    "datatype": int,
                    "datarange": (2020, 2023)
                }
            }
        },
        "sub3": {
            "datatype": list,
            "subs": {
                # 专业名称
                "sub1": {
                    "datatype": str,
                    "datarange": string.ascii_letters
                },
                # 学生成绩
                "sub2": {
                    "datatype": float,
                    "datarange": (0, 5)
                }
            }
        }
    }
}

def generate_random_value(data_type, data_range):
    if data_type == str:
        return ''.join(random.choice(data_range) for _ in range(10))
    elif data_type == int:
        return random.randint(data_range[0], data_range[1])
    elif data_type == float:
        return round(random.uniform(data_range[0], data_range[1]), 2)

def generate_random_data(data_structure):
    if data_structure["datatype"] == tuple:
        while True:
            data = tuple(next(generate_random_data(value)) for key, value in data_structure["subs"].items())
            yield data

    elif data_structure["datatype"] == list:
        while True:
            data = [next(generate_random_data(value)) for key, value in data_structure["subs"].items()]
            yield data

    else:
        while True:
            yield generate_random_value(data_structure["datatype"], data_structure["datarange"])

def generate_random_students(num_students):
    generator = generate_random_data(data_structure)
    for _ in range(num_students):
        yield next(generator)

num_students = random.randint(1, 100)
random_students = list(generate_random_students(num_students))
print(random_students)
