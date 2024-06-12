import random
import string

# 数据结构定义
dataStructure = {
    "datatype": tuple,
    "subs": {
        "sub1": {
            "datatype": list,
            # 姓名学号
            "subs": {
                "sub1": {"datatype": str, "datarange": string.ascii_letters},
                "sub2": {"datatype": int, "datarange": (2022010000, 2022019999)}
            }
        },
        "sub2": {
            "datatype": dict,
            # 专业班级
            "subs": {
                "sub1": {"datatype": str, "datarange": string.ascii_letters},
                "sub2": {"datatype": int, "datarange": (1, 10)}
            }
        },
        "sub3": {
            "datatype": list,
            # 成绩科目
            "subs": {
                "sub1": {"datatype": str, "datarange": string.ascii_letters},
                "sub2": {"datatype": float, "datarange": (0, 5)}
            }
        },
    }
}
def generate_random_data(**kwargs):
    data_structure = kwargs.get("data_structure")

    if data_structure["datatype"] == tuple:
        while True:
            data = ()
            for key, value in data_structure["subs"].items():
                if "datarange" in value:
                    if value["datatype"] == str:
                        random_data = ''.join(random.choice(value["datarange"]) for _ in range(10))
                    elif value["datatype"] == int:
                        random_data = random.randint(value["datarange"][0], value["datarange"][1])
                    elif value["datatype"] == float:
                        random_data = round(random.uniform(value["datarange"][0], value["datarange"][1]), 2)
                else:
                    random_data = next(generate_random_data(data_structure=value))
                data += (random_data,)
            yield data
    elif data_structure["datatype"] == list:
        while True:
            data = []
            for key, value in data_structure["subs"].items():
                if "datarange" in value:
                    if value["datatype"] == str:
                        random_data = ''.join(random.choice(value["datarange"]) for _ in range(10))
                    elif value["datatype"] == int:
                        random_data = random.randint(value["datarange"][0], value["datarange"][1])
                    elif value["datatype"] == float:
                        random_data = round(random.uniform(value["datarange"][0], value["datarange"][1]), 2)
                else:
                    random_data = next(generate_random_data(data_structure=value))
                data.append(random_data)
            yield data
    elif data_structure["datatype"] == dict:
        while True:
            data = {}
            for key, value in data_structure["subs"].items():
                if "datarange" in value:
                    if value["datatype"] == str:
                        random_data = ''.join(random.choice(value["datarange"]) for _ in range(10))
                    elif value["datatype"] == int:
                        random_data = random.randint(value["datarange"][0], value["datarange"][1])
                    elif value["datatype"] == float:
                        random_data = round(random.uniform(value["datarange"][0], value["datarange"][1]), 2)
                else:
                    random_data = next(generate_random_data(data_structure=value))
                data[key] = random_data
            yield data
def generate_random_students(num_students, **kwargs):
    student_info_list = []
    data_gen = generate_random_data(**kwargs)
    for _ in range(num_students):
        student_info = next(data_gen)
        student_info_list.append(student_info)
    return student_info_list
num_students = random.randint(1, 100)
random_students = generate_random_students(num_students, data_structure=dataStructure)
print(f"Generated {num_students} students:")
print(random_students)
