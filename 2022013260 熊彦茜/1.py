import random
import string
def generate_random_student():
    data = {
        "datatype": dict,
        "subs": {
            "Basic Info": {
                "datatype": dict,
                "subs": {
                    "Name": {
                        "datatype": str,
                        "datarange": string.ascii_uppercase,
                        "strlength": 3
                    },
                    "Gender": {
                        "datatype": str,
                        "datarange": ["Male", "Female"]
                    },
                    "Age": {
                        "datatype": int,
                        "datarange": (18, 22)
                    }
                }
            },
            "Enrollment Year": {
                "datatype": int,
                "datarange": (2010, 2024)
            },
            "Student ID": {
                "datatype": str,
                "datarange": string.digits,
                "strlength": 6
            },
            "Subjects": {
                "datatype": dict,
                "subs": {
                    random.choice(["Math", "Science", "History", "English"]): {
                        "datatype": float,
                        "datarange": (60, 100)
                    }
                }
            },
            "Hometown": {
                "datatype": str,
                "datarange": ["Beijing", "Shanghai", "Guangzhou", "Chengdu", "Wuhan"]
            }
        }
    }

    return generate_data(data)
def generate_data(data):
    if data["datatype"] == int:
        return random.randint(data["datarange"][0], data["datarange"][1])
    elif data["datatype"] == float:
        return random.uniform(data["datarange"][0], data["datarange"][1])
    elif data["datatype"] == str:
        if isinstance(data["datarange"], str):
            return ''.join(random.choices(data["datarange"], k=data.get("strlength", 1)))
        else:
            return random.choice(data["datarange"])
    elif data["datatype"] == dict:
        return {key: generate_data(value) for key, value in data["subs"].items()}



def generate_random_students():
    # 随机生成1到100个学生数量
    num_students = random.randint(1, 100)
    students = [generate_random_student() for _ in range(num_students)]
    return students

# 生成随机数量的学生信息
random_students = generate_random_students()
for student in random_students:
    print(student)
