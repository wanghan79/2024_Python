from pprint import pprint
import random
from typing import Iterable, Optional
from data_example import test_data


class RandomDataGenerator:
    """
    Random data generator
    """

    def __init__(self, ):
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

    def _generate_basic_type(self, data):
        """
        Generate basic type data
        :param data: basic type data
        :return: random value
        """

        self.basic_type_counter["all"] += 1

        data_range: Optional[Iterable] = data.get("datarange", None)
        if data["datatype"] == "int":
            self.basic_type_counter["int"] += 1
            return random.randint(data_range[0], data_range[1])
        elif data["datatype"] == "float":
            self.basic_type_counter["float"] += 1
            return random.uniform(data_range[0], data_range[1])
        elif data["datatype"] == "str":
            self.basic_type_counter["str"] += 1
            return random.choice(data_range)
        elif data["datatype"] == "bool":
            self.basic_type_counter["bool"] += 1
            return random.choice(data_range)
        else:
            raise Exception("Unsupported data type")

    def _generate_container_type(self, data):
        """
        Generate container type data
        :param data: container type data
        :return: random value
        """

        self.container_type_counter["all"] += 1

        inner_level = "sub"

        if data["datatype"] == "tuple":
            self.container_type_counter["tuple"] += 1
            result = ()
            for sub_data in data["subs"].values():
                result += (self.generate_random_data(sub_data, level=inner_level),)
        elif data["datatype"] == "list":
            self.container_type_counter["list"] += 1
            result = []
            for sub_data in data["subs"].values():
                result.append(self.generate_random_data(sub_data, level=inner_level))
        elif data["datatype"] == "set":
            self.container_type_counter["set"] += 1
            result = set()
            for sub_data in data["subs"].values():
                result.add(self.generate_random_data(sub_data, level=inner_level))
        else:
            raise Exception("Unsupported data type")

        return result

    def generate_random_data(self, data, auto_type_counter=False, level="master"):
        """
        Generate random data
        :param data: random data description
        :param auto_type_counter: auto count type
        :param level: when user call this function, level should be "master"
        :return: random value
        """
        if level == "master":
            self.auto_type_counter = auto_type_counter

        if data is None:
            return None

        if data.get("subs", None) is None:
            result = self._generate_basic_type(data)
        else:
            result = self._generate_container_type(data)

        if level == "master" and self.auto_type_counter:
            pprint(self.basic_type_counter)
            pprint(self.container_type_counter)

        return result


if __name__ == "__main__":
    generator = RandomDataGenerator()
    pprint(generator.generate_random_data(test_data, auto_type_counter=True, level="master"))
