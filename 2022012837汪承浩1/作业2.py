import random
import string


class RandomDataGenerator:
    def __init__(self, data_structure):
        self.data_structure = data_structure

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
                    if isinstance(value["datarange"], list):
                        random_data = random.choice(value["datarange"])
                    else:
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


data_structure = {
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
                    "datatype": str,
                    "datarange": ["数学", "语文", "英语", "物理", "化学", "生物", "历史", "地理", "政治"]
                },
                "sub2": {
                    "datatype": float,
                    "datarange": (0, 100)
                },
            }
        },
        "sub4": {
            "datatype": str,
            "datarange": ["北京", "上海", "广州", "深圳", "杭州", "南京", "武汉", "成都"]
        }
    }
}

generator = RandomDataGenerator(data_structure)
random_students = generator.generate_random_students(random.randint(1, 100))
print(random_students)
