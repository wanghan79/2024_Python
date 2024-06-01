
import random
import string


def dataSampling(**args):
    if args.__contains__("num"):
        answer = list()
        for i in range(0, args["num"]):
            z = dataSampling(**(args["dataStructure"]))
            answer.append(Student(z))
            # answer.append(dataSampling(**(args["dataStructure"])))
        return answer
    else:

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


class Student:
    def __init__(self, a):
        self.dataa = a[0]
        self.datab = a[1]
        self.datac = a[2]

    def __str__(self):
        an = ""
        an += self.dataa.__str__()
        an += self.datab.__str__()
        an += self.datac.__str__()
        return an


answera = dataSampling(**{"num": 3, "dataStructure": {"datatype": Student,
                                                      "subs": {"sub1": {"datatype": int, "datarange": (0, 100)},
                                                               "sub2": {"datatype": float, "datarange": (0, 100)},
                                                               "sub3": {"datatype": list,
                                                                        "subs": {"sub1": {"datatype": str,
                                                                                          "datarange": string.ascii_lowercase},
                                                                                 "sub2": {"datatype": str,
                                                                                          "datarange": string.ascii_uppercase,
                                                                                          "strlen": 10}}}}}})

print(type(answera[0]))
for i in answera:
    print(i)
