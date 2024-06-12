import random
import string
from functools import wraps

dataStructure = {
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
                    "datarange": (1, 100)
                }
            }
        },
        "sub2": {
            "datatype": list,
            "subs": {
                "sub1": {
                    "datatype": int,
                    "datarange": (16, 24)
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
                    "datatype": list,
                    "subs": {
                        "sub1": {
                            "datatype": str,
                            "datarange": ["数学", "语文", "英语", "物理", "化学", "生物", "历史", "地理", "政治"]
                        },
                        "sub2": {
                            "datatype": float,
                            "datarange": (0, 100)
                        }
                    }
                },
            }
        },
        "sub4": {
            "datatype": str,
            "datarange": ["北京", "上海", "广州", "深圳", "杭州", "南京", "武汉", "成都"]
        }
    }
}

def generate_random_data(data_structure):
    if data_structure["datatype"] == tuple:
        data = ()
    elif data_structure["datatype"] == list:
        data = []

    for key, value in data_structure["subs"].items():
        if "datarange" in value:
            if value["datatype"] == str:
                if isinstance(value["datarange"], list):
                    random_data = random.choice(value["datarange"])
                else:
                    random_data = ''.join(random.choice(value["datarange"]) for _ in range(10))
            elif value["datatype"] == int:
                random_data = random.randint(value["datarange"][0], value["datarange"][1])
            elif value["datatype"] == float:
                random_data = round(random.uniform(value["datarange"][0], value["datarange"][1]), 2)
        else:
            random_data = generate_random_data(value)

        if isinstance(data, tuple):
            data += (random_data,)
        elif isinstance(data, list):
            data.append(random_data)

    return data

def calculate_stats(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        total_scores = 0
        score_count = 0
        total_students = 0

        for student in func(*args, **kwargs):
            total_students += 1
            sub3_list = student[2]
            for sub3_item in sub3_list:
                if isinstance(sub3_item, list) and len(sub3_item) == 2 and isinstance(sub3_item[1], float):
                    total_scores += sub3_item[1]
                    score_count += 1

            yield student

        average_score = total_scores / score_count if score_count else 0

        print(f"学生总数: {total_students}")
        print(f"总分数: {total_scores}")
        print(f"平均分数: {average_score}")

    return wrapper

@calculate_stats
def generate_random_students(num_students):
    for _ in range(num_students):
        student_info = generate_random_data(dataStructure)
        yield student_info

random_students = list(generate_random_students(random.randint(1, 100)))
print(random_students)
