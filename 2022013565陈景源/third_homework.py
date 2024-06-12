import random
import string
from functools import wraps
from collections import defaultdict


class DataGenerator:
    def __init__(self, template):
        self.template = template
        self.type_counter = defaultdict(int)

    def generate_data(self, template=None):
        if template is None:
            template = self.template

        datatype = template.get("datatype")
        subs = template.get("subs", {})

        if datatype == tuple:
            result = ()
        elif datatype == list:
            result = []
        elif datatype == dict:
            result = {}
        elif datatype == set:
            result = set()

        for key, value in subs.items():
            if "datatype" in value and "datarange" in value:
                if value["datatype"] == int:
                    data_range = value["datarange"]
                    data = random.randint(*data_range)
                elif value["datatype"] == float:
                    data_range = value["datarange"]
                    data = random.uniform(*data_range)
                elif value["datatype"] == bool:
                    data = random.choice([True, False])
                elif value["datatype"] == str:
                    data_range = value["datarange"]
                    strlen = value.get("len", 1)
                    data = ''.join(random.SystemRandom().choice(data_range) for _ in range(strlen))
                else:
                    data = self.generate_data(value)
            else:
                data = self.generate_data(value)

            self.type_counter[type(data).__name__] += 1

            if datatype == tuple:
                result += (data,)
            elif datatype == list:
                result.append(data)
            elif datatype == dict:
                result[key] = data
            elif datatype == set:
                result.add(data)

        return result


def data_counter(template, operation_func=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            generator = DataGenerator(template)
            generated_data = generator.generate_data()
            counts = generator.type_counter
            if operation_func:
                operation_result = operation_func(generated_data)
            else:
                operation_result = None
            return func(*args, generated_data=generated_data, counts=counts, operation_result=operation_result,
                        **kwargs)

        return wrapper

    return decorator


def iterate(data):
    if isinstance(data, (list, tuple, set)):
        for item in data:
            yield from iterate(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            yield from iterate(value)
    else:
        yield data


def sum_data(data):
    return sum(value for value in iterate(data) if isinstance(value, (int, float)))


# Example template
example = {
    "datatype": tuple,
    "subs": {
        "sub1": {
            "datatype": list,
            "subs": {
                "sub1": {
                    "datatype": int,
                    "datarange": (0, 100)
                },
                "sub2": {
                    "datatype": str,
                    "datarange": string.ascii_uppercase,
                    "len": 5
                },
                "sub3": {
                    "datatype": float,
                    "datarange": (0.0, 1.0)
                },
            }
        },
        "sub2": {
            "datatype": tuple,
            "subs": {
                "sub1": {
                    "datatype": int,
                    "datarange": (0, 100)
                },
                "sub2": {
                    "datatype": str,
                    "datarange": string.ascii_uppercase,
                    "len": 5
                }
            }
        },
        "sub3": {
            "datatype": str,
            "datarange": string.ascii_uppercase,
            "len": 5
        }
    }
}


@data_counter(example, operation_func=sum_data)
def my_function(generated_data, counts, operation_result):
    print("Generated data:", generated_data)
    print("Type counts:", dict(counts))
    print("Sum of numbers:", operation_result)


# Call the decorated function
my_function()
