import random
import string

def generate_data(template):
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
                data = generate_data(value)
        else:
            data = generate_data(value)

        if datatype == tuple:
            result += (data,)
        elif datatype == list:
            result.append(data)
        elif datatype == dict:
            result[key] = data
        elif datatype == set:
            result.add(data)

    return result


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
                }
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

print(generate_data(example))
