import random
import string

dataStructure = {
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
                    "datarange": string.ascii_uppercase
                }
            }
        },
        "sub2": {
            "datatype": tuple,
            "subs": {
                "sub1": {
                    "datatype": float,
                    "datarange": (0, 5000),
                },
                "sub2": {
                    "datatype": int,
                    "datarange": (1, 200),
                }
            }
        },
        "sub3": {
            "datatype": str,
            "datarange": string.ascii_uppercase
        }
    }
}


def fill_random_values(**kwargs):
    if kwargs["datatype"] == int:
        return random.randint(kwargs["datarange"][0], kwargs["datarange"][1])
    elif kwargs["datatype"] == float:
        return random.uniform(kwargs["datarange"][0], kwargs["datarange"][1])
    elif kwargs["datatype"] == str:
        return ''.join(random.choices(kwargs["datarange"], k=random.randint(1, 10)))
    elif kwargs["datatype"] == list:
        sublist = {}
        for key, value in kwargs["subs"].items():
            sublist[key] = fill_random_values(**value)
        return [sublist[key] for key in sorted(sublist)]
    elif kwargs["datatype"] == tuple:
        sublist = {}
        for key, value in kwargs["subs"].items():
            sublist[key] = fill_random_values(**value)
        return tuple(sublist[key] for key in sorted(sublist))


num = int(input("请输入要生成的数据结构数量："))
for x in range(num):
    print(fill_random_values(**dataStructure))



