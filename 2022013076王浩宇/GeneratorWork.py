import random
import string

class RandomDataGenerator:
    def __init__(self):
        self.data_structure = {
            "datatype": tuple,
            "subs": {
                "sub1": {
                    "datatype": list,
                    "subs": {
                        "sub1": {
                            "datatype": str,  # 姓名
                            "datarange": string.ascii_letters,
                            "length": 10  # 字符串长度
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
                            "datarange": string.ascii_letters,
                            "length": 10  # 字符串长度
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

        if data_structure["datatype"] == int:
            yield random.randint(data_structure["datarange"][0], data_structure["datarange"][1])
        elif data_structure["datatype"] == float:
            yield round(random.uniform(data_structure["datarange"][0], data_structure["datarange"][1]), 2)
        elif data_structure["datatype"] == str:
            length = data_structure.get("length", 10)
            yield ''.join(random.choices(data_structure["datarange"], k=length))
        elif data_structure["datatype"] == list:
            result = []
            for key, value in data_structure["subs"].items():
                result.append(next(self.generate_random_data(value)))
            yield result
        elif data_structure["datatype"] == tuple:
            result = []
            for key, value in data_structure["subs"].items():
                result.append(next(self.generate_random_data(value)))
            yield result

    def generate_random_students(self, num_students):
        for _ in range(num_students):
            yield next(self.generate_random_data(self.data_structure))

random_data_generator = RandomDataGenerator()
num_students = random.randint(0, 100)
random_students = random_data_generator.generate_random_students(num_students)
print("Students Information:")
for random_student in random_students:
    print(random_student)