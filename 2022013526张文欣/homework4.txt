import random
import string
import usualClass
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
        else:
            data.append(creatdatastruct(**substruct))
    if kwargs["datatype"] == tuple: return tuple(data)
    elif kwargs["datatype"] == dict: return dict(data)
    elif kwargs["datatype"] == set: return set(data)
    return data
def dataselector(**args):
    struct = args["struct"]
    for i in range(0, args["num"]):
        lst = list(struct.values())
        ran = random.choice(lst)
        if ran["datatype"] == int:
            it = iter(ran["range"])
            randomint = random.randint(next(it), next(it))
            yield randomint
        elif ran["datatype"] == float:
            it = iter(ran["range"])
            randomfloat = random.uniform(next(it), next(it))
            yield randomfloat
        elif ran["datatype"] == str:
            randomstr = ''.join(random.SystemRandom().choice(ran["range"]) for _ in range(ran["len"]))
            yield randomstr
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
                else:
                    tupval.append(creatdatastruct(**subtupstruct))
            yield tuple(tupval)
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
                else:
                    lstval.append(creatdatastruct(**sublststruct))
            yield lstval
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
            yield setval
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
            yield dictval


#废案
# def data_yield(datatype,struct_yield,struct_display):  #struct_display是指你是否需要显示结构
#     for key in struct_yield:
#         if struct_display == 1: print(key)

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

struct = {
    "intstruct": {"datatype": int, "range": (0, 999)},
    "floatstruct": {"datatype": float, "range": (0, 99)},
    "strstruct": {"datatype": str, "range": string.ascii_lowercase, "len": 5},
    "tuple": {"datatype":tuple, "struct": nomaltype_tup},
    "list": {"datatype": list, "struct": nomaltype_lst},
    # 下面别管
    # "dict": {"datatype": dict, "struct": nomaltype_dict},
    # "set": {"datatype": set, "struct": nomaltype_set}
}

dic = {"num": 5, "struct": struct}


res=dataselector(**dic)

for key in res:
    print(key)

#废案
# while(True):
#     res = dataselector(**dic)
#     print("输入生成类型：int，float，不生成：0，退出：exit")
#     datatype = input()
#     if datatype == "exit" :exit(0)
#     if datatype == "0":
#         for key in res:
#             print(key)
#         continue
#     print("是否显示结构：是：1；否：0")
#     struct_display = input()
#     ls = data_yield(datatype,res,struct_display)#获取符合要求的数据项，可做和与平均
#     cnt = 0
#     res_sum = 0
#     for k in ls:
#         cnt+=1
#         res_sum+=k
#     print("求和？：是：1，不是：0")
#     print("求平均？：是：1，不是：0")
#     judge_sum=input()
#     judge_ave=input()
#     if(judge_sum=="1" or judge_ave=="1"):
#         print("%s个数为：" % datatype,cnt)
#     if (judge_sum == "1"):
#         print("%s和为：" % datatype,res_sum)
#     if (judge_ave == "1"):
#         print("%s平均值为：" % datatype,res_sum/cnt)
