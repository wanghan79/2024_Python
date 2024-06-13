import random
import string

class DataGenerator:
    def __init__(self):
        self.structure = {
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
                            "datarange": (0, 100)
                        }
                    }
                },
                "sub2": {
                    "datatype": list,
                    "subs": {
                        "sub1": {
                            "datatype": int,
                            "datarange": (18, 24)
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
                            "datarange": string.ascii_letters
                        },
                        "sub2": {
                            "datatype": float,
                            "datarange": (0, 5)
                        },
                    }
                }
            }
        }

    def create_random_value(self, datatype, datarange):
        if datatype == str:
            return ''.join(random.choice(datarange) for _ in range(10))
        elif datatype == int:
            return random.randint(datarange[0], datarange[1])
        elif datatype == float:
            return round(random.uniform(datarange[0], datarange[1]), 2)

    def generate_data(self, structure):
        data = [] if structure["datatype"] == list else ()
        for key, value in structure["subs"].items():
            if "datarange" in value:
                random_value = self.create_random_value(value["datatype"], value["datarange"])
            else:
                random_value = self.generate_data(value)

            if isinstance(data, tuple):
                data += (random_value,)
            else:
                data.append(random_value)

        return data

    def create_students(self, num_students):
        return [self.generate_data(self.structure) for _ in range(num_students)]

data_gen = DataGenerator()
students = data_gen.create_students(random.randint(1, 100))
print(students)
