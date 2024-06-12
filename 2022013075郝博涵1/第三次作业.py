import random
import string
from functools import wraps
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
def calculate_mean_and_variance(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        calculate_mean = kwargs.get("mean", False)
        calculate_variance = kwargs.get("variance", False)
        if calculate_mean or calculate_variance:
            scores = extract_scores(data)
            if calculate_mean:
                mean = sum(scores) / len(scores) if scores else None
            else:
                mean = None
            if calculate_variance:
                variance = sum((x - mean) ** 2 for x in scores) / len(scores) if scores else None
            else:
                variance = None
            return data, mean, variance
        return data, None, None
    return wrapper
def extract_scores(data):
    scores = []
    for student in data:
        if len(student) > 2:
            scores.append(student[2][1])
    return scores
def generate_random_data(data_structure, **kwargs):
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
            random_data = generate_random_data(data_structure=value, **kwargs)
        if isinstance(data, tuple):
            data += (random_data,)
        elif isinstance(data, list):
            data.append(random_data)
        elif isinstance(data, dict):
            data[key] = random_data
    return data
@calculate_mean_and_variance
def generate_random_students_with_stats(num_students, data_structure, **kwargs):
    student_info_list = []
    for _ in range(num_students):
        student_info = generate_random_data(data_structure, **kwargs)
        student_info_list.append(student_info)
    return student_info_list
result = generate_random_students_with_stats(random.randint(0, 100), data_structure=dataStructure, mean=True, variance=True)
random_students = result[0]
mean_score = result[1]
variance_score = result[2]
print("Generated Random Students:")
for student in random_students:
    print(student)
print("平均成绩:", mean_score)
print("成绩方差:", variance_score)
