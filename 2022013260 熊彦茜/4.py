import random
import string

def generate_random_student():
    while True:
        subject = random.choice(["Math", "Science", "History", "English"])
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
                        subject: {
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

        student_generator = generate_data(data)
        yield next(student_generator)

def generate_data(data):
    if data["datatype"] == int:
        while True:
            yield random.randint(data["datarange"][0], data["datarange"][1])
    elif data["datatype"] == float:
        while True:
            yield random.uniform(data["datarange"][0], data["datarange"][1])
    elif data["datatype"] == str:
        if isinstance(data["datarange"], str):
            while True:
                yield ''.join(random.choices(data["datarange"], k=data.get("strlength", 1)))
        else:
            while True:
                yield random.choice(data["datarange"])
    elif data["datatype"] == dict:
        while True:
            result = {}
            for key, value in data["subs"].items():
                result[key] = next(generate_data(value))
            yield result

def generate_random_students(num_students):
    student_generator = generate_random_student()
    for _ in range(num_students):
        yield next(student_generator)

# 随机生成1到100个学生数量
num_students = random.randint(1, 100)
random_students = generate_random_students(num_students)
for student in random_students:
    print(student)
