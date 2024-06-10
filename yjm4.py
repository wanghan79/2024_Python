import random
import string
import time


def dataSampling(**args):
    if args["datatype"] is int:
        it = iter(args["datarange"])
        return random.randint(next(it), next(it))
    elif args["datatype"] is float:
        it = iter(args["datarange"])
        return random.uniform(next(it), next(it))
    elif args["datatype"] is str:
        strlen = 5
        if args.__contains__("strlen"):
            strlen = args["strlen"]
        return ''.join(random.SystemRandom().choice(args["datarange"]) for _ in range(strlen))
    else:
        an = list()
        subdic = args["subs"]
        for key, value in subdic.items():
            an.append(dataSampling(**value))
        if args["datatype"] is tuple:
            an = tuple(an)
        return an


def functionA(num, **args):
    for i in range(0, num):
        yield dataSampling(**(args["dataStructure"]))


class Student:
    pass


struct = {"dataStructure": {"datatype": Student,
                            "subs": {"sub1": {"datatype": int, "datarange": (0, 100)},
                                     "sub2": {"datatype": float, "datarange": (0, 100)},
                                     "sub3": {"datatype": list, "subs": {
                                         "sub1": {"datatype": str, "datarange": string.ascii_lowercase},
                                         "sub2": {"datatype": str, "datarange": string.ascii_uppercase,
                                                  "strlen": 10}}}}}}
iterator = functionA(1000, **struct)
for i in iterator:
    print(i)
