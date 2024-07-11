# import random
# import string

# DictStruct = {
#     "data_type": tuple,
#     "subs": {
#         "sub1": {
#             "data_type": list,
#             "subs": {
#                 "sub1": {
#                     "data_type": int,
#                     "data_range": (0, 100)
#                 },
#                 "sub2": {
#                     "data_type": str,
#                     "data_range": string.ascii_uppercase,
#                     "len": 10
#                 }
#             }
#         },
#         "sub2": {
#             "data_type": tuple,
#             "subs": {
#                 "sub1": {
#                     "data_type": float,
#                     "data_range": (0, 5000)
#                 },
#                 "sub2": {
#                     "data_type": int,
#                     "data_range": (1, 200)
#                 }
#             }
#         },
#         "sub3": {
#             "data_type": str,
#             "data_range": string.ascii_uppercase,
#             "len": 10
#         }
#     }
# }

# def generate_random_data(data_spec):
#     result = {}
#     for key, value in data_spec.items():
#         if key == "data_type":
#             continue  # 跳过根节点的 "data_type" 键

#         if value["data_type"] == int:
#             result[key] = random.randint(*value["data_range"])
#         elif value["data_type"] == float:
#             result[key] = random.uniform(*value["data_range"])
#         elif value["data_type"] == str:
#             result[key] = ''.join(random.choice(value["data_range"]) for _ in range(value.get("len", 10)))
#         elif value["data_type"] == list:
#             result[key] = [generate_random_data(value["subs"]["sub1"]) for _ in range(random.randint(1, 10))]
#         elif value["data_type"] == tuple:
#             result[key] = tuple(generate_random_data(value["subs"]))
#         elif value["data_type"] == dict:
#             result[key] = generate_random_data(value["subs"])
#         elif value["data_type"] == set:
#             result[key] = {generate_random_data(value["subs"]["sub1"]) for _ in range(random.randint(1, 5))}

#     return result

# print(generate_random_data(DictStruct))

# import random
# import string

# DictStruct = {
#     "TypeSub": tuple,
#     "Sub": {
#         "TypeSub": list,
#         "Sub": {
#             "sub1": {
#                 "TypeSub": int,
#                 "Sub": (0, 100)
#             },
#             "sub2": {
#                 "TypeSub": str,
#                 "Sub": string.ascii_uppercase,
#                 "lenth": 10
#             }
#         }
#     }
# }

# def generate_random(data_spec):
#     result = {}
#     for key, value in data_spec.items():
#         if key == "TypeSub":
#             continue
        
#         if value["TypeSub"] == int:
#             result[key] = random.randint(*value["Sub"])
#         elif value["TypeSub"] == float:
#             result[key] = random.uniform(*value["Sub"])
#         elif value["TypeSub"] == str:
#             result[key] = ''.join(random.choice(value["Sub"]) for _ in range(value.get("lenth", 10)))
#         elif value["TypeSub"] == list:
#             result[key] = [generate_random(value["Sub"]["sub1"]) for _ in range(random.randint(1, 10))]
#         elif value["TypeSub"] == tuple:
#             result[key] = tuple(generate_random(value["Sub"]))
#         elif value["TypeSub"] == dict:
#             result[key] = generate_random(value["Sub"])
#         elif value["TypeSub"] == set:
#             result[key] = {generate_random(value["Sub"]["sub1"]) for _ in range(random.randint(1, 5))}
    
#     return result

# print(generate_random(DictStruct))

import random
import string

class Class:
    def __init__(self, name, number, ID):
        self.name = name
        self.number = number
        self.ID = ID

    def __repr__(self):
        return f"Class name:{self.name} number:{self.number} ID:{self.ID}"

def generate_random_data(structure):
    data_type = structure["data_type"]
    
    if data_type == int:
        return random.randint(*structure["data_range"])
    elif data_type == str:
        return ''.join(random.choices(structure["data_range"], k=structure["len"]))
    elif data_type == list:
        return [generate_random_data(sub_structure) for sub_structure in structure["subs"].values()]
    elif data_type == tuple:
        return tuple(generate_random_data(sub_structure) for sub_structure in structure["subs"].values())
    elif data_type == Class:
        subs = structure["subs"]
        return Class(
            generate_random_data(subs["name"]),
            generate_random_data(subs["number"]),
            generate_random_data(subs["ID"])
        )
    else:
        raise ValueError(f"Unsupported data type: {data_type}")

# 定义数据结构
# example = {
#     "data_type": tuple,
#     "subs": {
#         "sub1": {"data_type": list,
#                  "subs": {
#                      "sub1": {
#                          "data_type": int,
#                          "data_range": (0, 1000)
#                      },
#                      "sub2": {
#                          "data_type": str,
#                          "data_range": string.ascii_uppercase,
#                          "len": 10
#                      }
#                  },
#                  },
#         "sub2": {"data_type": tuple,
#                  "subs": {
#                      "sub1": {
#                          "data_type": int,
#                          "data_range": (0, 1000)
#                      },
#                      "sub2": {
#                          "data_type": str,
#                          "data_range": string.ascii_uppercase,
#                          "len": 10
#                      }
#                  },
#                  },
#         "sub3": {
#             "data_type": str,
#             "data_range": string.ascii_lowercase,
#             "len": 5
#         },
#         "sub4": {
#             "data_type": list,
#             "subs": {
#                 "subs": {
#                     "data_type": Class,
#                     "subs": {
#                         "name": {
#                             "data_type": str,
#                             "data_range": "2024计算机",
#                             "len": 10
#                         },
#                         "number": {
#                             "data_type": int,
#                             "data_range": (0, 100)
#                         },
#                         "ID": {
#                             "data_type": int,
#                             "data_range": (0, 100)
#                         }
#                     }
#                 }
#             }
#         }
#     }
# }

DictStuct={
    "TypeSub":tuple,
    "Subs":{
        "sub1":{
            "TypeSub":list,
            "Subs":{
                "sub1":{
                    "TypeSub":int,
                    "data_range":(0,100)
                },
                "sub2":{
                    "TypeSub":str,
                    "data_range":string.ascii_uppercase,
                    "lenth":10
                }
            },
        },
        "sub2":{
            "TypeSub":tuple,
            "Subs":{
                "TypeSub":float,
                "data_range":(0,5000),
                "TypeSub":int,
                "data_range":(1,200)
            },
        },
        "sub3":{
            "TypeSub":str,
            "data_range":string.ascii_uppercase,
            "lenth":10
        }
    }
}

# 生成随机数据
random_data = generate_random_data(DictStuct)
print(random_data)
