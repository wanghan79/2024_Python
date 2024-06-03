import random
import string

#使用类封装
class RandomDataGenerator:
    def __init__(self, data):
        self.data = data

    def generate_random_data(self, data=None):
        if data is None:
            data = self.data

        if data["datatype"] == int:
            return random.randint(data["datarange"][0], data["datarange"][1])
        elif data["datatype"] == float:
            return random.uniform(data["datarange"][0], data["datarange"][1])
        elif data["datatype"] == str:
            if isinstance(data["datarange"], str):
                data_len = data["strlength"]
                return ''.join(random.choices(data["datarange"], k=data_len))
            else:
                r_index = random.randint(0, len(data["datarange"]) - 1)
                return data["datarange"][r_index]
        elif data["datatype"] == tuple:
            result = {}
            for key, value in data["subs"].items():
                result[key] = self.generate_random_data(data=value)
            return result
        elif data["datatype"] == list:
            size = data["subs"]["size"]
            return [self.generate_random_data(data=data["subs"]) for _ in range(size)]
        elif data["datatype"] == dict:
            return {key: self.generate_random_data(data=value) for key, value in data["subs"].items()}
        elif data["datatype"] == set:
            size = data["subs"]["size"]
            return {self.generate_random_data(data=data["subs"]) for _ in range(size)}

    def generate(self):
        random_data = self.generate_random_data()
        return random_data


data = {
    "datatype": tuple,
    "subs": {
        "Sub1": {
            "datatype": int,
            "datarange": (0, 100)
        },
        "Sub2": {
            "datatype": str,
            "datarange": string.ascii_uppercase,
            "strlength": 5
        },
        "Sub3": {
            "datatype": tuple,
            "subs": {
                "Sub1": {
                    "datatype": float,
                    "datarange": (0, 5008)
                },
                "Sub2": {
                    "datatype": int,
                    "datarange": (1, 200)
                },
                "Sub3": {
                    "datatype": str,
                    "datarange": string.ascii_uppercase,
                    "strlength": 5
                }
            }
        },
        "Sub4": {
            "datatype": list,
            "subs": {
                "datatype": int,
                "size": 5,
                "datarange": (0, 50)
            }
        },
        "Sub5": {
            "datatype": dict,
            "subs": {
                "key1": {
                    "datatype": str,
                    "datarange": string.ascii_lowercase,
                    "strlength": 5
                },
                "key2": {
                    "datatype": float,
                    "datarange": (0, 1000)
                }
            }
        },
        "Sub6": {
            "datatype": set,
            "subs": {
                "size": 3,
                "datatype": str,
                "datarange": ("Chongqing", "Sichuan", "Hubei", "Jilin", "Heilongjiang", "Shaanxi")
            }
        }
    }
}

generator = RandomDataGenerator(data=data)
random_data = generator.generate()
print(random_data)