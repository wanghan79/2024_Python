import random
from typing import Iterable, Optional
from data_example import test_data


def generate_random_data(data: dict):
    data_range: Optional[Iterable] = data.get("datarange", None)
    if data.get("subs", None) is None:
        if data["datatype"] == "int":
            return random.randint(data_range[0], data_range[1])
        elif data["datatype"] == "float":
            return random.uniform(data_range[0], data_range[1])
        elif data["datatype"] == "str":
            return random.choice(data_range)
        elif data["datatype"] == "bool":
            return random.choice(data_range)

    result = None
    if data["datatype"] == "tuple":
        result = ()
        for sub_data in data["subs"].values():
            result += (generate_random_data(sub_data),)
    elif data["datatype"] == "list":
        result = []
        for sub_data in data["subs"].values():
            result.append(generate_random_data(sub_data))
    elif data["datatype"] == "set":
        result = set()
        for sub_data in data["subs"].values():
            result.add(generate_random_data(sub_data))

    return result


if __name__ == "__main__":
    print(generate_random_data(test_data))
