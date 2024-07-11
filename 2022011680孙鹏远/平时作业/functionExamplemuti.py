#我自己先写的
# import random
# def dataSampling(datatype,datarange,num,strlen=8):
#     result=set()
#     resultMuti=set()
#     resultMutiList=list()
#     for index in range(0,num):
#         if datatype is int:
#             it = iter(datarange)
#             item=random.randint(next(it),next(it))
#             result.add(item)
#             continue
#         elif datatype is float:
#             it = iter(datarange)
#             item=random.uniform(next(it),next(it))
#             result.add(item)
#             continue
#         elif datatype is str:
#             item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
#             result.add(item)
#             continue
#         elif datatype is list:
#             resultMuti.add(dataSampling(str,datarange[0],1))
#             resultMuti.add(dataSampling(int,datarange[0],1))
#             resultMuti.add(dataSampling(float,datarange[0],1))
#             resultMutiList.append(list(resultMuti))
#             resultMuti.clear()
#         elif datatype is tuple:
#             continue
#         else:
#             continue
#     if(resultMutiList):
#         return result
#     else:
#         return resultMutiList

# dataSampling(list,["abcdefghijklmnopqrstuvwxyz",[0,18],[0.0,100.0]],20)




# GPT生的
# import random

# def generate_random_value(value_type, depth=1, count=1, min_value=None, max_value=None):
#     if depth == 0:
#         if value_type == int:
#             return random.randint(min_value, max_value)
#         elif value_type == float:
#             return random.uniform(min_value, max_value)
#         else:
#             return None

#     if value_type == list:
#         return [generate_random_value(int, depth-1, count, min_value, max_value) for _ in range(count)]
#     else:
#         return generate_random_value(value_type, depth-1, count, min_value, max_value)

# # 生成一个包含随机整数的多层嵌套列表
# random_list = generate_random_value(int, depth=3, count=3, min_value=1, max_value=100)
# print(random_list)



# 引导
# 试了好几次，按照老师指导和其他同学作业，重新设计了输入数据的结构
# import random
# import string

# DictStuct={
#     "TypeSub":tuple,
#     "Subs":{
#         "sub1":{
#             "TypeSub":list,
#             "Subs":{
#                 "sub1":{
#                     "TypeSub":int,
#                     "data_range":(0,100)
#                 },
#                 "sub2":{
#                     "TypeSub":str,
#                     "data_range":string.ascii_uppercase,
#                     "lenth":10
#                 }
#             },
#         },
#         "sub2":{
#             "TypeSub":tuple,
#             "Subs":{
#                 "sub1":{
#                     "TypeSub":float,
#                     "data_range":(0,5000)
#                 },
#                 "sub2":{
#                     "TypeSub":int,
#                     "data_range":(1,200)
#                 }
#             }
#         },
#         "sub3":{
#             "TypeSub":str,
#             "data_range":string.ascii_uppercase,
#             "lenth":10
#         }
#     }
# }

# # 遍历字典

# def generateRandom(**kwargs):
#     result=dict()
#     for key, value in kwargs.items():
#         # 如果TypeSub节点类型为int float str这些单层无嵌套类型，则向当前层尾部根据Sub添加随机数或内容
#         if value["TypeSub"] is int:
#             result[key] = random.randint(*value["Sub"])
#         elif value["TypeSub"] is float:
#             result[key] = random.uniform(*value["Sub"])
#         elif value["TypeSub"] is str:
#             result[key] = ''.join(random.SystemRandom().choice(value["Sub"]) for _ in range(random.randint(1, len(value["Sub"]))))
#         # 如果TypeSub节点类型为list tuple dict set这些嵌套类型，则向当前层尾部添加一层该类型的空list或tuple或dict或set
#         elif value["TypeSub"] is list:
#             result.append(list(generateRandom(**value["Sub"])))
#         elif value["TypeSub"] is tuple:
#             result.append(tuple(generateRandom(**value["Sub"])))
#         elif value["TypeSub"] is dict:
#             result.append(dict(generateRandom(**value["Sub"])))
#         elif value["TypeSub"] is set:
#             result.append(set(generateRandom(**value["Sub"])))
#         # else:
#         #     result.append(...)

#         # result[key] = generateRandom(**value["Sub"])
    
#     return result


# print(generateRandom(**DictStuct))

# 该段python代码想要generateRandom(DictStuct)函数想要接收可能有多层嵌套的字典数据并遍历其中的每层每一个节点，并根据其中的内容生成随机数包含在相同结构的嵌套结构中。

import random
import string

# 用户自定数据类型Class
class Class:
    def __init__(self, name , ID , Howloud=None, number="-1"):
        self.name = name
        self.ID = ID
        self.Howloud = Howloud
        self.number = number

    def __repr__(self):
        return f"Class name:{self.name} number:{self.number} ID:{self.ID} Howloud{self.Howloud}/......"
    
class Voice:
    def __init__(self,db,smell):
        self.db = db
        self.smell = smell
    
    def __repr__(self):
        return f"######Voice db:{self.db} smell:{self.smell} ******"

def generate_random_data(**structure):
    data_type = structure["TypeSub"]
    
    if data_type == int:
        return random.randint(*structure["datarange"])
    elif data_type == float:
        return random.uniform(*structure["datarange"])
    elif data_type == str:
        return ''.join(random.choices(structure["datarange"], k=structure["lenth"]))
    elif data_type == list:
        return [generate_random_data(**sub_structure) for sub_structure in structure["Subs"].values()]
    elif data_type == tuple:
        return tuple(generate_random_data(**sub_structure) for sub_structure in structure["Subs"].values())
    # elif data_type == Class:
    #     subs = structure["Subs"]
    #     return Class(generate_random_data(subs))
    else:
        # raise ValueError(f"Unsupported data type: {data_type}")

        # 若自定义数据类型的为嵌套类型
        return data_type(**{k: generate_random_data(**v) for k, v in structure["Subs"].items()})
        # 若自定义数据类型的不为嵌套类型
        # 

# 定义数据结构
DictStuct={
    "TypeSub":tuple,
    "Subs":{
        "Sociaty":{
            "TypeSub":list,
            "Subs":{
                "Level":{
                    "TypeSub":int,
                    "datarange":(0,100)
                },
                "SociatyNickName":{
                    "TypeSub":str,
                    "datarange":string.ascii_uppercase,
                    "lenth":10
                }
            },
        },
        "Location":{
            "TypeSub":tuple,
            "Subs":{
                "North_Latitude":{
                    "TypeSub":float,
                    "datarange":(0,90)
                },
                "Height":{
                    "TypeSub":int,
                    "datarange":(1,200)
                }
            }
        },
        "Description":{
            "TypeSub":str,
            "datarange":string.ascii_uppercase,
            "lenth":10
        },
        "UserDefinedtest":{
            "TypeSub": list,
            "Subs": {
                "Sub1": {
                    "TypeSub": Class,
                    "Subs": {
                        "name": {
                            "TypeSub": str,
                            "datarange": "呐哼h啊a",
                            "lenth": 10
                        },
                        "Howloud": {
                            "TypeSub": Voice,
                            "Subs":{
                                "db":{
                                    "TypeSub":int,
                                    "datarange": (-114514,114515)
                                },
                                "smell":{
                                    "TypeSub":str,
                                    "datarange": "smelly",
                                    "lenth": 6
                                }
                            }
                        },
                        "ID": {
                            "TypeSub": int,
                            "datarange": (0, 100)
                        }
                    }
                },
                "Sub2": {
                    "TypeSub": Class,
                    "Subs": {
                        "name": {
                            "TypeSub": str,
                            "datarange": "2024计算机",
                            "lenth": 10
                        },
                        "number": {
                            "TypeSub": int,
                            "datarange": (0, 4)
                        },
                        "ID": {
                            "TypeSub": int,
                            "datarange": (0, 100)
                        }
                    }
                }
            }
        }
    }
}

# 生成随机数据
random_data = generate_random_data(**DictStuct)
print(random_data)