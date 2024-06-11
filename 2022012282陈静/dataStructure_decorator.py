import string
import random

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

def count_calls(func):
    counts = {}

    def wrapper(*args, **kwargs):
        data_type = func.__name__
        if data_type in counts:
            counts[data_type] += 1
        else:
            counts[data_type] = 1
        return func(*args, **kwargs)

    wrapper.counts = counts
    return wrapper

@count_calls
def generate_random_data(**kwargs):
    data_structure = kwargs.get("data_structure")
    datatype = data_structure["datatype"]
    if datatype == tuple:
        return generate_random_tuple(data_structure["subs"])
    elif datatype == list:
        return generate_random_list(data_structure["subs"])
    elif datatype == str:
        return generate_random_string(data_structure["datarange"])
    elif datatype == int:
        return generate_random_int(data_structure["datarange"])
    elif datatype == float:
        return generate_random_float(data_structure["datarange"])

def generate_random_tuple(subs):
    data = {}
    for key, value in subs.items():
        data[key] = generate_random_data(data_structure=value)
    return data

def generate_random_list(subs):
    data = []
    for _ in range(random.randint(1, 5)):
        item = {}
        for key, value in subs.items():
            item[key] = generate_random_data(data_structure=value)
        data.append(item)
    return data

def generate_random_int(datarange):
    range_l = datarange[0]
    range_r = datarange[1]
    return random.randint(range_l, range_r)

def generate_random_float(datarange):
    range_l = datarange[0]
    range_r = datarange[1]
    return random.uniform(range_l, range_r)

def generate_random_string(datarange):
    return ''.join(random.choice(datarange) for _ in range(random.randint(5, 10)))

random_data = generate_random_data(data_structure=dataStructure)
print(random_data)
print(generate_random_data.counts)
