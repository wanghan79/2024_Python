import logging
import string
import random
class func(object):
    args=dict()
    val=0
    cnt=0
    sum=0
    res=list()
    def __init__(self,**args):
        self.args=args

    def getSelfRes(self):
        self.res=self.datasampling()

    def print(self):
        for k in self.res:
            print(k)

    def creatdatastruct(self,**kwargs):
        data = list()
        struct = kwargs["struct"]
        for key in struct:
            substruct = struct[key]
            if substruct["datatype"] == int:
                it = iter(substruct["range"])
                randomint_lst = random.randint(next(it), next(it))
                data.append(randomint_lst)
            elif substruct["datatype"] == float:
                it = iter(substruct["range"])
                randomfloat_lst = random.uniform(next(it), next(it))
                data.append(randomfloat_lst)
            elif substruct["datatype"] == str:
                randomstr_lst = ''.join(
                    random.SystemRandom().choice(substruct["range"]) for _ in range(substruct["len"]))
                data.append(randomstr_lst)
            elif substruct["datatype"] == tuple:
                data.append(self.creatdatastruct(**substruct))
            elif substruct["datatype"] == list:
                data.append(self.creatdatastruct(**substruct))
        if kwargs["datatype"] == tuple: return tuple(data)
        return data

    def datasampling(self):
        res=list()
        struct = self.args["struct"]
        for i in range(0, self.args["num"]):
            lst = list(struct.values())#生成随机类型
            ran = random.choice(lst)
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
                        randomstr_tup = ''.join(
                            random.SystemRandom().choice(subtupstruct["range"]) for _ in range(subtupstruct["len"]))
                        tupval.append(randomstr_tup)
                    elif subtupstruct["datatype"] == tuple:
                        tupval.append(self.creatdatastruct(**subtupstruct))
                    elif subtupstruct["datatype"] == list:
                        tupval.append(self.creatdatastruct(**subtupstruct))
                res.append(tuple(tupval))
            elif ran["datatype"] == set:
                setval = set()
                structset = ran["struct"]
                it = iter(structset["intrange"])
                randomint_set = random.randint(next(it), next(it))
                it = iter(structset["floatrange"])
                randomfloat_set = random.uniform(next(it), next(it))
                strstruct_set = structset["strstruct"]
                randomstr_set = ''.join(
                    random.SystemRandom().choice(strstruct_set["range"]) for _ in range(strstruct_set["len"]))
                setval.add(randomint_set)
                setval.add(randomfloat_set)
                setval.add(randomstr_set)
                res.append(setval)
            elif ran["datatype"] == list:
                lstval = list()
                lststruct = ran["struct"]
                for key in lststruct:
                    sublststruct = lststruct[key]
                    if sublststruct["datatype"] == int:
                        it = iter(sublststruct["range"])
                        randomint_lst = random.randint(next(it), next(it))
                        lstval.append(randomint_lst)
                    elif sublststruct["datatype"] == float:
                        it = iter(sublststruct["range"])
                        randomfloat_lst = random.uniform(next(it), next(it))
                        lstval.append(randomfloat_lst)
                    elif sublststruct["datatype"] == str:
                        randomstr_lst = ''.join(
                            random.SystemRandom().choice(sublststruct["range"]) for _ in range(sublststruct["len"]))
                        lstval.append(randomstr_lst)
                    elif sublststruct["datatype"] == tuple:
                        lstval.append(self.creatdatastruct(**sublststruct))
                    elif sublststruct["datatype"] == list:
                        lstval.append(self.creatdatastruct(**sublststruct))
                res.append(lstval)
        return res

    def calstruct(self,datastruct,flag):
        for key in datastruct:
            if flag == 1:
                if type(key) == float or type(key) == str: continue
                elif type(key) == int:
                    self.sum += key
                    self.cnt += 1
                else:self.calstruct(key,1)
            elif flag == 0:
                if type(key) == int or type(key) == str: continue
                elif type(key) == float:
                    self.sum += key
                    self.cnt += 1
                else:self.calstruct(key,0)
            elif flag == 2:
                if type(key) == str: continue
                elif type(key) == float or type(key) == int:
                    self.sum += key
                    self.cnt += 1
                else:self.calstruct(key,2)
            elif flag == 3:
                if type(key) == str or type(key) == int : continue
                elif type(datastruct) == tuple and type(key) == float:
                    self.sum += key
                    self.cnt += 1
                elif type(key) != float:
                    self.calstruct(key,3)
            elif flag == 4:
                if type(key) == str or type(key) == int : continue
                elif type(datastruct) == list and type(key) == float:
                    self.sum += key
                    self.cnt += 1
                elif type(key) != float:
                    self.calstruct(key,4)
            elif flag == 5:
                if type(key) == str or type(key) == float : continue
                elif type(datastruct) == tuple and type(key) == int:
                    self.sum += key
                    self.cnt += 1
                elif type(key) != int:
                    self.calstruct(key,5)
            elif flag == 6:
                if type(key) == str or type(key) == float : continue
                elif type(datastruct) == list and type(key) == int:
                    self.sum += key
                    self.cnt += 1
                elif type(key) != int:
                    self.calstruct(key,6)

    def tocaldata(self,datatype):
        flag=2
        if(datatype== "int"): flag = 1
        if(datatype == "float"): flag=0
        if (datatype == "float_tuple"): flag = 3
        if (datatype == "float_list"): flag = 4
        if (datatype == "int_tuple"): flag = 5
        if (datatype == "int_list"): flag = 6
        for key in self.res:
            if flag == 1:
                if type(key) == float or type(key) == str: continue
                elif type(key) == int:
                    self.sum += key
                    self.cnt += 1
                else:self.calstruct(key,1)
            elif flag == 0:
                if type(key) == int or type(key) == str: continue
                elif type(key) == float:
                    self.sum += key
                    self.cnt += 1
                else:self.calstruct(key,0)
            elif flag == 2:
                if type(key) == str: continue
                elif type(key) == float or type(key) == int:
                    self.sum += key
                    self.cnt += 1
                else:self.calstruct(key,2)
            elif flag == 3:
                if type(key) == int or type(key) == str : continue
                elif type(self.res) == tuple and type(key) == float :
                    self.sum += key
                    self.cnt += 1
                elif type(key) != float:self.calstruct(key,3)
            elif flag == 4:
                if type(key) == int or type(key) == str : continue
                elif type(self.res) == list and type(key) == float :
                    self.sum += key
                    self.cnt += 1
                elif type(key) != float:self.calstruct(key,4)
            elif flag == 5:
                if type(key) == float or type(key) == str : continue
                elif type(self.res) == tuple and type(key) == int :
                    self.sum += key
                    self.cnt += 1
                elif type(key) != int:self.calstruct(key,5)
            elif flag == 6:
                if type(key) == float or type(key) == str : continue
                elif type(self.res) == list and type(key) == int :
                    self.sum += key
                    self.cnt += 1
                elif type(key) != int:self.calstruct(key,6)
        return self.sum

    def exportdata(self,lst):
        self.getSelfRes()
        self.print()
        for op in lst:
            if op == "int_sum" or op == "int_ave":
                self.tocaldata("int")
                if op == "int_sum":
                    self.summary("int")
                else:
                    self.average("int")
            elif op == "float_sum" or op == "float_ave":
                self.tocaldata("float")
                if op == "float_sum":
                    self.summary("float")
                else:
                    self.average("float")
            elif op == "int&float_sum" or op == "int&float_ave":
                self.tocaldata("int&float")
                if op == "int&float_sum":
                    self.summary("int&float")
                else:
                    self.average("int&float")
            elif op == "float_tuple_sum" or op == "float_tuple_ave":
                self.tocaldata("float_tuple")
                if op == "float_tuple_sum":
                    self.summary("float_tuple")
                else:
                    self.average("float_tuple")
            elif op == "int_tuple_sum" or op == "int_tuple_ave":
                self.tocaldata("int_tuple")
                if op == "int_tuple_sum":
                    self.summary("int_tuple")
                else:
                    self.average("int_tuple")
            elif op == "float_list_sum" or op == "float_list_ave":
                self.tocaldata("float_list")
                if op == "float_list_sum":
                    self.summary("float_list")
                else:
                    self.average("float_list")
            elif op == "int_list_sum" or op == "int_list_ave":
                self.tocaldata("int_list")
                if op == "int_list_sum":
                    self.summary("int_list")
                else:
                    self.average("int_list")
            else:
                logging.warning("%s不合法的输入内容",op)
        self.res.clear()

    def summary(self,datatype):
        if datatype == "int":
            print("int总数为：", self.sum,"int个数为：",self.cnt)
        elif datatype == "float":
            print("float总数为：", self.sum,"int个数为：",self.cnt)
        elif datatype == "int&float":
            print("int&float总数为：", self.sum,"个数为：",self.cnt)
        elif datatype == "float_tuple":
            print("在tuple里float总数为：", self.sum, "个数为：", self.cnt)
        elif datatype == "int_tuple":
            print("在tuple里int总数为：", self.sum, "个数为：", self.cnt)
        elif datatype == "float_list":
            print("在list里float总数为：", self.sum, "个数为：", self.cnt)
        elif datatype == "int_list":
            print("在list里int总数为：", self.sum, "个数为：", self.cnt)
        self.sum = 0
        self.cnt = 0

    def average(self,datatype):
        if self.cnt==0:
            print(logging.warning("错误，除数为0"))
        else:
            self.val = self.sum / self.cnt
            if datatype == "int":
                print("int平均数为：",self.val,"int个数为：",self.cnt)
            elif datatype == "float":
                print("float平均数为：",self.val,"float个数为：",self.cnt)
            elif datatype == "int&float":
                print("int&float平均数为：", self.val, "个数为：", self.cnt)
            elif datatype == "float_tuple":
                print("在tuple里float平均数为：", self.val, "个数为：", self.cnt)
            elif datatype == "int_tuple":
                print("在tuple里int平均数为：", self.val, "个数为：", self.cnt)
            elif datatype == "float_list":
                print("在list里float平均数为：", self.val, "个数为：", self.cnt)
            elif datatype == "int_list":
                print("在list里int平均数为：", self.val ,"个数为：", self.cnt)
        self.sum = 0
        self.cnt = 0

#子结构类型，按照如下结构，可重嵌套多个结构，这里set和dict没弄，弄了也没写
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
                    "substruct":{
                        "datatype":list,
                        "struct":{
                            "intstruct": {"datatype":int,"range":(0, 1000)},
                            "floatstruct":{"datatype":float,"range":(0, 100)},
                            "strstruct": {"datatype":str,"range": string.ascii_uppercase, "len": 4},
                        }
                    }
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
            },
            "floatstruct2":{"datatype":float,"range":(0, 99)},
            "floatstruct3":{"datatype":float,"range":(0, 9999)},
            "intstruct2": {"datatype": int, "range": (0, 100)},
            "intstruct3": {"datatype": int, "range": (0, 1000000)},
        }
    },
    "floatstruct": {"datatype": float, "range": (0, 100)},
    "strstruct1": {"datatype":str,"range": string.ascii_letters, "len": 7},
}
nomaltype_dict = {
    "len":3,
    "intrange": (0, 1000),
    "floatrange": (0, 100),
    "strstruct": {"range": string.ascii_uppercase, "len": 4}
}
nomaltype_set = {
    "len":3,
    "intrange": (0, 1000),
    "floatrange": (0, 100),
    "strstruct": {"range": string.ascii_uppercase, "len": 4}
}

#基本数据结构
struct = {
    "intstruct": {"datatype": int, "range": (0, 999)},
    "floatstruct": {"datatype": float, "range": (0, 99)},
    "strstruct": {"datatype": str, "range": string.ascii_lowercase, "len": 5},
    "tuple": {"datatype":tuple, "struct": nomaltype_tup},
    "list": {"datatype": list, "struct": nomaltype_lst},
    # "dict": {"datatype": dict, "struct": nomaltype_dict},
    # "set": {"datatype": set, "struct": nomaltype_set}
}

dic = {"num": 5, "struct": struct}
foo=func(**dic)

#所有操作数如下
op_all=["int_sum","int_ave","float_sum","float_ave","int&float_sum","int&float_ave"]
op_tuple=["int_tuple_sum","int_tuple_ave","float_tuple_sum","float_tuple_ave"]
op_list=["int_list_sum","int_list_ave","float_list_sum","float_list_ave"]

finalop=op_all+op_list+op_tuple

foo.exportdata(op_all)
