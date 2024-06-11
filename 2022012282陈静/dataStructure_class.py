import random
import string

class RandomDataGenerator:
    def __init__(self, **kwargs):
        self.data_structure = kwargs.get("data_structure")

    def generate_random_data(self):
        return self._generate_random_data(self.data_structure)

    def _generate_random_data(self, data_structure):
        datatype = data_structure["datatype"]
        if datatype == tuple:
            return self.generate_random_tuple(data_structure["subs"])
        elif datatype == list:
            return self.generate_random_list(data_structure["subs"])
        elif datatype == str:
            return self.generate_random_string(data_structure["datarange"])
        elif datatype == int:
            return self.generate_random_int(data_structure["datarange"])
        elif datatype == float:
            return self.generate_random_float(data_structure["datarange"])

    def generate_random_tuple(self, subs):
        data = {}
        for key, value in subs.items():
            data[key] = self._generate_random_data(value)
        return data

    def generate_random_list(self, subs):
        data = []
        for _ in range(random.randint(1, 5)):
            item = {}
            for key, value in subs.items():
                item[key] = self._generate_random_data(value)
            data.append(item)
        return data

    def generate_random_int(self, datarange):
        range_l = datarange[0]
        range_r = datarange[1]
        return random.randint(range_l, range_r)

    def generate_random_float(self, datarange):
        range_l = datarange[0]
        range_r = datarange[1]
        return random.uniform(range_l, range_r)

    def generate_random_string(self, datarange):
        return ''.join(random.choice(datarange) for _ in range(random.randint(5, 10)))

dataStructure = {
    "datatype": tuple,
    "subs": {
        "sub1": {
            "datatype": list,
            "subs": {
                "sub1": {
                    "datatype": float,
                    "datarange": (0, 5000),
                },
                "sub2": {
                    "datatype": int,
                    "datarange": (0, 50),
                }
            }
        },
        "sub2": {
            "datatype": str,
            "datarange": string.ascii_uppercase,
        },
        "sub3": {
            "datatype": tuple,
            "subs": {
                "sub1": {
                    "datatype": int,
                    "datarange": (0, 100),
                },
                "sub2": {
                    "datatype": str,
                    "datarange": string.ascii_lowercase,
                },
                "sub3": {
                    "datatype": str,
                    "datarange": string.digits,
                }
            }
        }
    }
}

random_data_generator = RandomDataGenerator(data_structure=dataStructure)
random_data = random_data_generator.generate_random_data()
print(random_data)
