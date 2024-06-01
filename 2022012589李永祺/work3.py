import string
import random
from functools import wraps


class Student:
    pass


operationStruct = {
    "operations": {"operation1": {"type": int, "op": "sum"}, "operation2": {"type": int, "op": "average"}}}

structFormat = {"num": 3,
                "dataStructure": {"datatype": Student,
                                  "subs": {"sub1": {"datatype": int, "datarange": (0, 100)},
                                           "sub2": {"datatype": float, "datarange": (0, 100)},
                                           "sub3": {"datatype": list, "subs": {
                                               "sub1": {"datatype": str, "datarange": string.ascii_lowercase},
                                               "sub2": {"datatype": str, "datarange": string.ascii_uppercase,
                                                        "strlen": 10}}}}}}


# 从work2弄来的处理操作的函数
def handle(answerList, datatype, op):  # a为list，b为type，c为处理类型
    if answerList.__class__ is int or answerList.__class__ is float or answerList.__class__ is str:  # int or float
        if answerList.__class__ is datatype:
            return answerList, 1
        return 0, 0
    elif answerList.__class__ is list or answerList.__class__ is tuple:
        an = 0
        num = 0
        for i in answerList:
            tuplez = handle(i, datatype, 0)
            an += tuplez[0]
            num += tuplez[1]
        if op == 0:
            return an, num
        if op == "sum":
            return an
        return an / num


def decorator(**op):
    def deco(func):
        @wraps(func)
        def inner(*args, **kwargs):
            z = func(*args, **kwargs)
            if not op.__contains__("operations"):
                return z
            for i, j in op["operations"].items():
                print(handle(z, j["type"], j["op"]))
            return z

        return inner

    return deco


def dataSampling(**kwargs):
    if kwargs.__contains__("num"):
        answer = list()
        for i in range(0, kwargs["num"]):
            answer.append(dataSampling(**(kwargs["dataStructure"])))
        return answer
    else:

        if kwargs["datatype"] is int:
            it = iter(kwargs["datarange"])
            return random.randint(next(it), next(it))
        elif kwargs["datatype"] is float:
            it = iter(kwargs["datarange"])
            return random.uniform(next(it), next(it))
        elif kwargs["datatype"] is str:
            strlen = 5
            if kwargs.__contains__("strlen"):
                strlen = kwargs["strlen"]
            return ''.join(random.SystemRandom().choice(kwargs["datarange"]) for _ in range(strlen))
        else:
            an = list()
            subdic = kwargs["subs"]
            for key, value in subdic.items():
                an.append(dataSampling(**value))
            if kwargs["datatype"] is tuple:
                an = tuple(an)
            return an


@decorator(**operationStruct)
def funct(**kwargs):
    return dataSampling(**kwargs)


print(funct(**structFormat))
