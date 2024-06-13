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


class RandomDataGenerator:
    """
    Random data generator
    """

    def __init__(self):
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
            result = ()
            for sub_data in data["subs"].values():
                result += (self.generate_random_data(sub_data),)
        elif data["datatype"] == "list":
            result = []
            for sub_data in data["subs"].values():
                result.append(self.generate_random_data(sub_data))
        elif data["datatype"] == "set":
            result = set()
            for sub_data in data["subs"].values():
                result.add(self.generate_random_data(sub_data))
        else:
            raise Exception("Unsupported data type")

        return result

    def generate_random_data(self, data):
        """
        Generate random data
        :param data: random data description
        :return: random value
        """
        if data is None:
            return None

        if data.get("subs", None) is None:
            result = self._generate_basic_type(data)
        else:
            result = self._generate_container_type(data)

        return result


if __name__ == "__main__":
    generator = RandomDataGenerator()
    pprint(generator.generate_random_data(test_data))
    Counter.print_count_result()
