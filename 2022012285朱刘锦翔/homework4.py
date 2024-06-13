from pprint import pprint
import random
from typing import Iterable, Optional
from data_example import test_data


class Counter:
    basic_type_counter = {
        "all": 0,
        "int": 0,
        "float": 0,
        "str": 0,
        "bool": 0,
    }
    container_type_counter = {
        "all": 0,
        "tuple": 0,
        "list": 0,
        "set": 0,
        "dict": 0,
    }

    @staticmethod
    def count(func):
        def wrapper(self, *args, **kwargs):
            if args[0].get("subs", None):
                Counter.container_type_counter["all"] += 1
                Counter.container_type_counter[args[0]["datatype"]] += 1
            else:
                Counter.basic_type_counter["all"] += 1
                Counter.basic_type_counter[args[0]["datatype"]] += 1

            return func(self, *args, **kwargs)

        return wrapper

    @staticmethod
    def print_count_result():
        print("basic type counter:")
        pprint(Counter.basic_type_counter)
        print("container type counter:")
        pprint(Counter.container_type_counter)

    @staticmethod
    def reset():
        Counter.basic_type_counter = {
            "all": 0,
            "int": 0,
            "float": 0,
            "str": 0,
            "bool": 0,
        }
        Counter.container_type_counter = {
            "all": 0,
            "tuple": 0,
            "list": 0,
            "set": 0,
            "dict": 0,
        }


class RandomDataGenerator:
    """
    Random data generator
    """

    def __init__(self, all_data=None):
        self.all_data = all_data
        self.auto_type_counter = False
        self.basic_type_counter = {
            "all": 0,
            "int": 0,
            "float": 0,
            "str": 0,
            "bool": 0,
        }
        self.container_type_counter = {
            "all": 0,
            "tuple": 0,
            "list": 0,
            "set": 0,
            "dict": 0,
        }

    @Counter.count
    def _generate_basic_type(self, data):
        """
        Generate basic type data
        :param data: basic type data
        :return: random value
        """

        data_range: Optional[Iterable] = data.get("datarange", None)
        if data["datatype"] == "int":
            return random.randint(data_range[0], data_range[1])
        elif data["datatype"] == "float":
            return random.uniform(data_range[0], data_range[1])
        elif data["datatype"] == "str":
            return random.choice(data_range)
        elif data["datatype"] == "bool":
            return random.choice(data_range)
        else:
            raise Exception("Unsupported data type")

    @Counter.count
    def _generate_container_type(self, data):
        """
        Generate container type data
        :param data: container type data
        :return: random value
        """

        if data["datatype"] == "tuple":
            return tuple(self.generate_random_data(sub_data) for sub_data in data["subs"].values())
        elif data["datatype"] == "list":
            return [self.generate_random_data(sub_data) for sub_data in data["subs"].values()]
        elif data["datatype"] == "set":
            return set(self.generate_random_data(sub_data) for sub_data in data["subs"].values())
        else:
            raise Exception("Unsupported data type")

    def generate_random_data(self, data):
        """
        Generate random data
        :param data: random data description
        :return: random value
        """
        if data is None:
            return None

        if data.get("subs", None) is None:
            return self._generate_basic_type(data)
        else:
            return self._generate_container_type(data)

    def __iter__(self):
        for data in self.all_data:
            yield self.generate_random_data(data)


if __name__ == "__main__":
    datas = [test_data for _ in range(5)]
    generator = RandomDataGenerator(datas)
    for index, result in enumerate(generator):
        print(f"This is result {index+1}")
        pprint(result)
        Counter.print_count_result()
        Counter.reset()
        print()
