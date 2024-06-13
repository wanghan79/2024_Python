import random
import string
from functools import wraps
def generate_random_student():
    data = {
        "Basic Info": {
            "Name": ''.join(random.choices(string.ascii_uppercase, k=3)),
            "Gender": random.choice(["Male", "Female"]),
            "Age": random.randint(18, 22)
        },
        "Enrollment Year": random.randint(2010, 2024),
        "Student ID": ''.join(random.choices(string.digits, k=6)),
        "Subjects": {
            random.choice(["Math", "Science", "History", "English"]): random.uniform(60, 100)
        },
        "Hometown": random.choice(["Beijing", "Shanghai", "Guangzhou", "Chengdu", "Wuhan"])
    }
    return data
def generate_random_students(num_students):
    students = [generate_random_student() for _ in range(num_students)]
    return students
def calculate_sum_and_mean(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        calculate_sum = kwargs.get("sum", False)
        calculate_mean = kwargs.get("mean", False)
        if calculate_sum or calculate_mean:
            total_sum = 0
            scores = []
            for student in data:
                if "Subjects" in student:
                    for subject, score in student["Subjects"].items():
                        total_sum += score
                        scores.append(score)
            if calculate_mean:
                mean = sum(scores) / len(scores) if scores else None
            else:
                mean = None
            return data, total_sum, mean
        return data, None, None
    return wrapper
@calculate_sum_and_mean
def generate_and_analyze_students(num_students, sum=False, mean=False):
    students = generate_random_students(num_students)
    return students
random_students, total_sum, mean = generate_and_analyze_students(5, sum=True, mean=True)
for student in random_students:
    print(student)
print(f"总分: {total_sum}")
print(f"平均分: {mean}")
