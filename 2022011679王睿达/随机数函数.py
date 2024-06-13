import random
import string

kwargs = {
    "num": 5,
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
                    "datarange": string.ascii_letters
                },
            },
        },
        "sub2": {
            "datatype": tuple,
            "subs": {
                "sub1": {
                    "datatype": float,
                    "datarange": (0, 100)
                },
                "sub2": {
                    "datatype": int,
                    "datarange": (0, 100)
                },
            },
        },
        "sub3": {
            "datatype": str,
            "datarange": string.ascii_letters
        }
    }
}

def structdatasampling(kwargs):
    datatype = kwargs["datatype"]
    if datatype == int:
        it = iter(kwargs["datarange"])
        return random.randint(next(it), next(it))
    elif datatype == float:
        it = iter(kwargs["datarange"])
        return random.uniform(next(it), next(it))
    elif datatype == str:
        return ''.join(random.SystemRandom().choice(kwargs["datarange"]) for _ in range(7))
    elif datatype in (list, tuple):
        elements = []
        for sub_key, sub_value in kwargs["subs"].items():
            elements.append(structdatasampling(sub_value))
        if datatype == list:
            return elements
        else:
            return tuple(elements)

def number(kwargs):
    num = kwargs["num"]
    elements = []
    for i in range(num):
        elements.append(structdatasampling(kwargs))
    return elements

print(number(kwargs))
