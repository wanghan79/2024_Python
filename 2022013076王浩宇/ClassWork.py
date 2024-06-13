import random
import string

class RandomDataGenerator:
    def __init__(self):
        self.data_structure = {"datatype": tuple,
                               "subs": {
                                   "sub1": {
                                       "datatype": list,
                                       "subs": {
                                           "sub1": {
                                               "datatype": str, #姓名
                                               "datarange": string.ascii_letters
                                           },
                                           "sub2": {
                                               "datatype": int, #学号
                                               "datarange": (2020000000, 2023000000)
                                           }
                                       }
                                   },
                                   "sub2": {
                                       "datatype": list,
                                       "subs": {
                                           "sub1": {
                                               "datatype": int, #年龄
                                               "datarange": (16, 24)
                                           },
                                           "sub2": {
                                               "datatype": int, #入学日期
                                               "datarange": (2020, 2023)
                                           }
                                       }
                                   },
                                   "sub3": {
                                       "datatype": list,
                                       "subs": {
                                           "sub1": {
                                               "datatype": str, #学院
                                               "datarange": string.ascii_letters
                                           },
                                           "sub2": {
                                               "datatype": float, #绩点
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


random_data_generator = RandomDataGenerator()
random_students = random_data_generator.generate_random_students(random.randint(0, 100))
print("Students Information:")
for random_student in random_students:
    print(random_student)
