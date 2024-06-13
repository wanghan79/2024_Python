import random
import string
import statistics

class DataGenerator:
    def __init__(self):
        self.data_structure = {
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
                            # 学生成绩
                            "datarange": (0, 5)
                        },
                    }
                }
            }
        }

    def generate_random_data(self, data_structure):
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

    def calculate_stats(func):
        def wrapper(*args, **kwargs):
            student_data = func(*args, **kwargs)

            grades = []
            for student in student_data:
                grade = student[2][1]
                grades.append(grade)

            if grades:
                mean = statistics.mean(grades)
                variance = statistics.variance(grades) if len(grades) > 1 else 0.0
            else:
                mean = 0.0
                variance = 0.0

            print(f"Mean of grades: {mean}")
            print(f"Variance of grades: {variance}")

            return student_data

        return wrapper

    @calculate_stats
    def generate_random_students(self, num_students):
        student_info_list = []
        for _ in range(num_students):
            student_info = self.generate_random_data(self.data_structure)
            student_info_list.append(student_info)

        for student in student_info_list:
            print(student)

        return student_info_list


data_generator = DataGenerator()
random_students = data_generator.generate_random_students(random.randint(0, 100))
