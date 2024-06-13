import random
import string

dataStructure = {
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

def generate_random_data(data_structure):
    if data_structure["datatype"] == tuple:
        while True:
            data = []
            for key, value in data_structure["subs"].items():
                data.append(next(generate_random_data(value)))
            yield tuple(data)

    elif data_structure["datatype"] == list:
        while True:
            data = []
            for key, value in data_structure["subs"].items():
                data.append(next(generate_random_data(value)))
            yield data

    elif data_structure["datatype"] == str:
        while True:
            yield ''.join(random.choice(data_structure["datarange"]) for _ in range(10))

    elif data_structure["datatype"] == int:
        while True:
            yield random.randint(data_structure["datarange"][0], data_structure["datarange"][1])

    elif data_structure["datatype"] == float:
        while True:
            yield round(random.uniform(data_structure["datarange"][0], data_structure["datarange"][1]), 2)

def generate_random_students(num_students):
    generator = generate_random_data(dataStructure)
    for _ in range(num_students):
        yield next(generator)

num_students = random.randint(1, 100)
random_students = list(generate_random_students(num_students))
print(random_students)
