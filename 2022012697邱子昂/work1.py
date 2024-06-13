import random
import string


def generate_random_data(data_structure):
    datatype = data_structure['datatype']
    if datatype == tuple:
        return generate_random_tuple(data_structure['subs'])
    elif datatype == list:
        return generate_random_list(data_structure['subs'])
    elif datatype == str:
        return generate_random_string(data_structure['datarange'])
    elif datatype == int:
        return generate_random_int(data_structure['datarange'])
    elif datatype == float:
        return generate_random_float(data_structure['datarange'])


def generate_random_tuple(subs):
    return {key: generate_random_data(value) for key, value in subs.items()}


def generate_random_list(subs):
    return [
        generate_random_data({
            'datatype': dict,
            'subs': subs
        })
        for _ in range(random.randint(1, 5))
    ]


def generate_random_int(datarange):
    return random.randint(*datarange)


def generate_random_float(datarange):
    return random.uniform(*datarange)


def generate_random_string(datarange):
    length = random.randint(5, 10)
    return ''.join(random.choice(datarange) for _ in range(length))


# 定义数据结构
example = {
    "datatype": tuple,
    "subs": {
        "sub1": {
            "datatype": str,
            "datarange": string.ascii_uppercase
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

random_data = generate_random_data(example)
print(random_data)
