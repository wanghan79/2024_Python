import random
import string

def generate_random_data(**kwargs):
    datatype = kwargs.get("datatype")
    if datatype == int:
        drange = kwargs.get("drange")
        return random.randint(drange[0], drange[1])
    elif datatype == float:
        drange = kwargs.get("drange")
        return random.uniform(drange[0], drange[1])
    elif datatype == str:
        length = kwargs.get("len")
        chars = kwargs.get("drange", string.ascii_lowercase)
        return ''.join(random.choices(chars, k=length))
    elif datatype in (list, tuple, set):
        subs = kwargs.get("subs")
        if subs is None:
            return [] if datatype == list else () if datatype == tuple else set()
        result = []
        for sub_kwargs in subs.values():
            result.append(generate_random_data(**sub_kwargs))
        if datatype == list:
            return result
        elif datatype == tuple:
            return tuple(result)
        else:
            return set(result)

#迭代器
# class Ran:
#     def __init__(self, **kwargs):
#         self.n = kwargs.get("num")
#         self.m = kwargs.get("struct")
#         self.num=1
#     def __iter__(self):
#             return self
#     def __next__(self):
#         if self.num>self.n:
#             raise StopIteration
#         result = generate_random_data(**self.m)
#         self.num+=1
#         return result
#生成器
def Ran(**kwargs):
    for i in range(kwargs.get("num")):
        yield generate_random_data(**kwargs.get("struct"))

para = {
    "num": 3,
    "struct": {
        "datatype": tuple,
        "subs": {
            "sub1": {
                "datatype": list,
                "subs": {
                    "sub1": {
                        "datatype": int,
                        "drange": (0, 150),
                    },
                    "sub2": {
                        "datatype": str,
                        "drange": string.ascii_lowercase,
                        "len": 8
                    },
                },
            },
            "sub2": {
                "datatype": float,
                "drange": (0, 100),
            },
        },
    },
}
if __name__ == '__main__':
    rg = Ran(**para)
    for i in range(3):
        print(next(rg))

