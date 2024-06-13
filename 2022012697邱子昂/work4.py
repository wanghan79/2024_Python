
import string
import random

def generate_random_data(**kwargs):
    data_structure = kwargs.get("data_structure")
    datatype = data_structure["datatype"]
    if datatype == tuple:
        yield from generate_random_tuple(data_structure["subs"])
    elif datatype == list:
        yield from generate_random_list(data_structure["subs"])
    elif datatype == str:
        yield from generate_random_string(data_structure["datarange"])
    elif datatype == int:
        yield from generate_random_int(data_structure["datarange"])
    elif datatype == float:
        yield from generate_random_float(data_structure["datarange"])

def generate_random_tuple(subs):
    data = {}
    for key, value in subs.items():
        data[key] = list(generate_random_data(data_structure=value))
    yield data

def generate_random_list(subs):
    for _ in range(random.randint(1, 5)):
        item = {}
        for key, value in subs.items():
            item[key] = list(generate_random_data(data_structure=value))
        yield item

def generate_random_int(datarange):
    range_l = datarange[0]
    range_r = datarange[1]
    yield random.randint(range_l, range_r)

def generate_random_float(datarange):
    range_l = datarange[0]
    range_r = datarange[1]
    yield random.uniform(range_l, range_r)

def generate_random_string(datarange):
    yield ''.join(random.choice(datarange) for _ in range(random.randint(5, 10)))

example = {
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

random_data = list(generate_random_data(data_structure=example))
print(random_data)

