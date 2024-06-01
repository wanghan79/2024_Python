import string
import random


class learn:

    @staticmethod
    def dataSampling(**args):
        if args.__contains__("num"):
            answer = list()
            for i in range(0, args["num"]):
                answer.append(learn.dataSampling(**(args["dataStructure"])))
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
                    an.append(learn.dataSampling(**value))
                if args["datatype"] is tuple:
                    an = tuple(an)
                return an
    @staticmethod
    def summon(**args):
        answer = learn.dataSampling(**args)
        print(answer)
        return learn.__handle__(answer, args["type"], args["operate"])

    @staticmethod
    def __handle__(answerList, datatype, op):  # a为list，b为type，c为处理类型
        if answerList.__class__ is int or answerList.__class__ is float or answerList.__class__ is str:  # int or float
            if answerList.__class__ is datatype:
                return answerList, 1
            return 0, 0
        elif answerList.__class__ is list or answerList.__class__ is tuple:
            an = 0
            num = 0
            for i in answerList:
                tuplez = learn.__handle__(i, datatype, 0)
                an += tuplez[0]
                num += tuplez[1]
            if op == 0:
                return an, num
            if op == "sum":
                return an
            return an / num



class Student:
    pass


answer = learn.summon(**{"type": int, "operate": "sum", "num": 3, "dataStructure": {"datatype": Student,
                                                                                    "subs": {"sub1": {"datatype": int,
                                                                                                      "datarange": (
                                                                                                          0, 100)},
                                                                                             "sub2": {"datatype": float,
                                                                                                      "datarange": (
                                                                                                          0, 100)},
                                                                                             "sub3": {"datatype": list,
                                                                                                      "subs": {"sub1": {
                                                                                                          "datatype": str,
                                                                                                          "datarange": string.ascii_lowercase},
                                                                                                          "sub2": {
                                                                                                              "datatype": str,
                                                                                                              "datarange": string.ascii_uppercase,
                                                                                                              "strlen": 10}}}}}})
print(answer)
