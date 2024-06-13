import random
import string
import statistics
from functools import wraps


class RandomDataGenerator:
    def __init__(self):
        self.data_structure = {"datatype": tuple,
                               "subs": {
                                   "sub1": {
                                       "datatype": list,
                                       "subs": {
                                           "sub1": {
                                               "datatype": str,  # 姓名
                                               "datarange": string.ascii_letters
                                           },
                                           "sub2": {
                                               "datatype": int,  # 学号
                                               "datarange": (2020000000, 2023000000)
                                           }
                                       }
                                   },
                                   "sub2": {
                                       "datatype": list,
                                       "subs": {
                                           "sub1": {
                                               "datatype": int,  # 年龄
                                               "datarange": (16, 24)
                                           },
                                           "sub2": {
                                               "datatype": int,  # 入学日期
                                               "datarange": (2020, 2023)
                                           }
                                       }
                                   },
                                   "sub3": {
                                       "datatype": list,
                                       "subs": {
                                           "sub1": {
                                               "datatype": str,  # 学院
                                               "datarange": string.ascii_letters
                                           },
                                           "sub2": {
                                               "datatype": float,  # 绩点
                                               "datarange": (0, 5)
                                           },
                                       }
                                   },
                               }
                               }

    def generate_random_data(self, data_structure=None):
        if data_structure is None:
            data_structure = self.data_structure

        if data_structure["datatype"] == tuple:
            data = ()
        elif data_structure["datatype"] == list:
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
                random_data = self.generate_random_data(value)

            if isinstance(data, tuple):
                data += (random_data,)
            elif isinstance(data, list):
                data.append(random_data)

        return data

    def generate_random_students(self, num_students):
        student_info_list = []
        for _ in range(num_students):
            student_info = self.generate_random_data()
            student_info_list.append(student_info)

        return student_info_list

    def calculate_statistics(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            student_data = func(*args, **kwargs)
            if student_data:
                ages = [student[1][0] for student in student_data]
                enrollment_years = [student[1][1] for student in student_data]
                gpas = [student[2][1] for student in student_data]

                age_mean = statistics.mean(ages)
                age_variance = statistics.variance(ages)
                enrollment_year_mean = statistics.mean(enrollment_years)
                enrollment_year_variance = statistics.variance(enrollment_years)
                gpa_mean = statistics.mean(gpas)
                gpa_variance = statistics.variance(gpas)
            else:
                age_mean = age_variance = 0
                enrollment_year_mean = enrollment_year_variance = 0
                gpa_mean = gpa_variance = 0

            stats = {
                'age': {'mean': age_mean, 'variance': age_variance},
                'enrollment_year': {'mean': enrollment_year_mean, 'variance': enrollment_year_variance},
                'gpa': {'mean': gpa_mean, 'variance': gpa_variance}
            }

            return student_data, stats

        return wrapper

    @calculate_statistics
    def generate_and_calculate_statistics(self, num_students):
        return self.generate_random_students(num_students)


random_data_generator = RandomDataGenerator()
num_students = random.randint(0, 100)
random_students, statistics = random_data_generator.generate_and_calculate_statistics(num_students)

print("Students Information:")
for random_student in random_students:
    print(random_student)

print("Statistics:")
print(statistics)
