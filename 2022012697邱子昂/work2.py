import random
import string

class RandomDataGenerator:

    def generate_random_data(self, data_structure):
        datatype = data_structure['datatype']
        if datatype == tuple:
            return self.generate_random_tuple(data_structure['subs'])
        elif datatype == list:
            return self.generate_random_list(data_structure['subs'])
        elif datatype == str:
            return self.generate_random_string(data_structure['datarange'])
        elif datatype == int:
            return self.generate_random_int(data_structure['datarange'])
        elif datatype == float:
            return self.generate_random_float(data_structure['datarange'])

    def generate_random_tuple(self, subs):
        return tuple(self.generate_random_data(item) for item in subs.values())

    def generate_random_list(self, subs):
        return [
            self.generate_random_data(item)
            for _ in range(random.randint(1, 5))
            for item in subs.values()
        ]

    def generate_random_int(self, datarange):
        return random.randint(*datarange)

    def generate_random_float(self, datarange):
        return random.uniform(*datarange)

    def generate_random_string(self, datarange):
        length = random.randint(5, 10)
        return ''.join(random.choice(datarange) for _ in range(length))


example = {
    "datatype": tuple,
    "subs": {
        "sub1": {
            "datatype": list,
            "subs": {
                "sub1": {
                    "datatype": float, 
                    "datarange": (0, 5000)
                },
                "sub2": {
                    "datatype": int,
                    "datarange": (0, 50)
                }
            }
        },
        "sub2": {
            "datatype": str,
            "datarange": string.ascii_uppercase
        },
        "sub3": {
            "datatype": tuple,
            "subs": {
                "sub1": {
                    "datatype": int,
                    "datarange": (0, 100)
                },
                "sub2": {
                    "datatype": str,
                    "datarange": string.ascii_lowercase
                },
                "sub3": {
                    "datatype": str, 
                    "datarange": string.digits
                }
            }
        }
    }
}

generator = RandomDataGenerator()
random_data = generator.generate_random_data(example)
print(random_data)
