import random
import string
def creatdatastruct(**kwargs):
    data=list()
    struct=kwargs["struct"]
    for key in struct:
        substruct=struct[key]
        if substruct["datatype"] == int:
            it = iter(substruct["range"])
            randomint_lst = random.randint(next(it), next(it))
            data.append(randomint_lst)
        elif substruct["datatype"] == float:
            it = iter(substruct["range"])
            randomfloat_lst = random.uniform(next(it), next(it))
            data.append(randomfloat_lst)
        elif substruct["datatype"] == str:
            randomstr_lst = ''.join(random.SystemRandom().choice(substruct["range"]) for _ in range(substruct["len"]))
            data.append(randomstr_lst)
        elif substruct["datatype"] == tuple:
            data.append(creatdatastruct(**substruct))
        elif substruct["datatype"] == list:
            data.append(creatdatastruct(**substruct))
    if kwargs["datatype"] == tuple: return tuple(data)
    return data
def dataselector(**args):
    res = list()
    struct = args["struct"]
    for i in range(0, args["num"]):
        lst = list(struct.values())
        ran = random.choice(lst)
    # for keywdf in struct:
    #     ran=struct[keywdf]
        if ran["datatype"] == int:
            it = iter(ran["range"])
            randomint = random.randint(next(it), next(it))
            res.append(randomint)
        elif ran["datatype"] == float:
            it = iter(ran["range"])
            randomfloat = random.uniform(next(it), next(it))
            res.append(randomfloat)
        elif ran["datatype"] == str:
            randomstr = ''.join(random.SystemRandom().choice(ran["range"]) for _ in range(ran["len"]))
            res.append(randomstr)
        elif ran["datatype"] == tuple:
            tupval = list()
            tupstruct = ran["struct"]
            for key in tupstruct:
                subtupstruct = tupstruct[key]
                if subtupstruct["datatype"] == int:
                    it = iter(subtupstruct["range"])
                    randomint_tup = random.randint(next(it), next(it))
                    tupval.append(randomint_tup)
                elif subtupstruct["datatype"] == float:
                    it = iter(subtupstruct["range"])
                    randomfloat_tup = random.uniform(next(it), next(it))
                    tupval.append(randomfloat_tup)
                elif subtupstruct["datatype"] == str:
                    randomstr_tup = ''.join(random.SystemRandom().choice(subtupstruct["range"]) for _ in range(subtupstruct["len"]))
                    tupval.append(randomstr_tup)
                elif subtupstruct["datatype"] == tuple:
                    tupval.append(creatdatastruct(**subtupstruct))
                elif subtupstruct["datatype"] == list:
                    tupval.append(creatdatastruct(**subtupstruct))
            res.append(tuple(tupval))
        elif ran["datatype"] == list:
            lstval = list()
            lststruct = ran["struct"]
            for key in lststruct:
                sublststruct=lststruct[key]
                if sublststruct["datatype"]==int:
                    it = iter(sublststruct["range"])
                    randomint_lst = random.randint(next(it), next(it))
                    lstval.append(randomint_lst)
                elif sublststruct["datatype"]==float:
                    it = iter(sublststruct["range"])
                    randomfloat_lst = random.uniform(next(it), next(it))
                    lstval.append(randomfloat_lst)
                elif sublststruct["datatype"]==str:
                    randomstr_lst = ''.join(random.SystemRandom().choice(sublststruct["range"]) for _ in range(sublststruct["len"]))
                    lstval.append(randomstr_lst)
                elif sublststruct["datatype"]==tuple:
                    lstval.append(creatdatastruct(**sublststruct))
                elif sublststruct["datatype"]==list:
                    lstval.append(creatdatastruct(**sublststruct))
            res.append(lstval)
        elif ran["datatype"] == set:
            setval = set()
            structset = ran["struct"]
            it = iter(structset["intrange"])
            randomint_set = random.randint(next(it), next(it))
            it = iter(structset["floatrange"])
            randomfloat_set = random.uniform(next(it), next(it))
            strstruct_set = structset["strstruct"]
            randomstr_set = ''.join(random.SystemRandom().choice(strstruct_set["range"]) for _ in range(strstruct_set["len"]))
            setval.add(randomint_set)
            setval.add(randomfloat_set)
            setval.add(randomstr_set)
            res.append(setval)
        elif ran["datatype"] == dict:
            dictval = dict()
            structdict = ran["struct"]
            it = iter(structdict["intrange"])
            randomint_dict = random.randint(next(it), next(it))
            it = iter(structdict["floatrange"])
            randomfloat_dict = random.uniform(next(it), next(it))
            strstruct_dict = structdict["strstruct"]
            randomstr_dict = ''.join(random.SystemRandom().choice(strstruct_dict["range"]) for _ in range(strstruct_dict["len"]))
            dictval["int"]=randomint_dict
            dictval["float"]=randomfloat_dict
            dictval["str"]=randomstr_dict
            res.append(dictval)
    return res

nomaltype_tup = {
    "intstruct": {"datatype":int,"range":(0, 1000)},
    "floatstruct":{"datatype":float,"range":(0, 100)},
    "strstruct": {"datatype":str,"range": string.ascii_uppercase, "len": 4},
    "substruct":{
        "datatype":tuple,
        "struct":{
            "intstruct": {"datatype":int,"range":(0, 1000)},
            "floatstruct": {"datatype":float,"range":(0, 100)},
            "strstruct": {"datatype":str,"range": string.ascii_uppercase, "len": 4},
            "substruct": {
                "datatype":list,
                "struct": {
                    "intstruct": {"datatype": int, "range": (0, 1000)},
                    "floatstruct": {"datatype": float, "range": (0, 100)},
                    "strstruct": {"datatype": str, "range": string.ascii_uppercase, "len": 4},
                }
            }
        }
    }
}
nomaltype_lst = {
    "substruct":{
        "datatype":list,
        "struct":{
            "intstruct": {"datatype":int,"range":(0, 1000)},
            "floatstruct":{"datatype":float,"range":(0, 100)},
            "strstruct": {"datatype":str,"range": string.ascii_uppercase, "len": 4},
            "substruct":{
                "datatype":tuple,
                "struct": nomaltype_tup
            }
        }
    },
    "floatstruct": {"datatype": float, "range": (0, 100)},
    "strstruct1": {"datatype":str,"range": string.ascii_letters, "len": 7},
}
nomaltype_dict = {
    "intrange": (0, 1000),
    "floatrange": (0, 100),
    "strstruct": {"range": string.ascii_uppercase, "len": 4}
}
nomaltype_set = {
    "intrange": (0, 1000),
    "floatrange": (0, 100),
    "strstruct": {"range": string.ascii_uppercase, "len": 4}
}

struct = {
    "intstruct": {"datatype": int, "range": (0, 999)},
    "floatstruct": {"datatype": float, "range": (0, 99)},
    "strstruct": {"datatype": str, "range": string.ascii_lowercase, "len": 5},
    "tuple": {"datatype":tuple, "struct": nomaltype_tup},
    "list": {"datatype": list, "struct": nomaltype_lst},
    "dict": {"datatype": dict, "struct": nomaltype_dict},
    "set": {"datatype": set, "struct": nomaltype_set}
}

dic = {"num": 5, "struct": struct}

res = dataselector(**dic)
for key in res:
    print(key)
