import random
import string
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
        data = ()
    elif data_structure["datatype"] == list:
        data = []
    elif data_structure["datatype"] == dict:
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
            random_data = generate_random_data(data_structure=value)
        if isinstance(data, tuple):
            data += (random_data,)
        elif isinstance(data, list):
            data.append(random_data)
        elif isinstance(data, dict):
            data[key] = random_data
    return data
def generate_random_students(num_students, **kwargs):
    student_info_list = []
    for _ in range(num_students):
        student_info = generate_random_data(**kwargs)
        student_info_list.append(student_info)
    return student_info_list

num_students = random.randint(0, 100)
random_students = generate_random_students(num_students, data_structure=dataStructure)
print(random_students)
