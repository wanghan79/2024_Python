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
        return f"Class name:{self.name} number:{self.number} ID:{self.ID} Howloud:{self.Howloud} "
    
class Voice:
    def __init__(self,db,smell):
        self.db = db
        self.smell = smell
    
    def __repr__(self):
        return f"Voice db:{self.db} smell:{self.smell}"

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
    elif data_type == dict:
        return {key: generate_random_data(**sub_structure) for key, sub_structure in structure["Subs"].items()}
        # return dict(generate_random_data(**sub_structure) for sub_structure in structure["Subs"].values())
    elif data_type == set:
        return {generate_random_data(**sub_structure) for sub_structure in structure["Subs"].values()}
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
            "TypeSub":dict,
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
            "TypeSub":set,
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
# print(type(random_data[0]))