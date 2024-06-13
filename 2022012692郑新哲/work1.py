import random
import string


dataStructure = {"datatype":tuple,
               "subs": {
                   "sub1":{
                       "datatype":list,
                       "subs":{
                           # 学生姓名
                           "sub1":{
                               "datatype":str,
                               "datarange":string.ascii_letters
                           },
                           # 学生序号
                           "sub2":{
                               "datatype":int,
                               "datarange":(0,100)
                           }
                       }
                   },
                   "sub2": {
                       "datatype": list,
                       "subs": {
                           # 学生年龄
                           "sub1": {
                               "datatype": int,
                               "datarange": (18,24)
                           },
                           # 入学年份
                           "sub2": {
                               "datatype": int,
                               "datarange": (2020,2023)
                           }
                       }
                   },
                   "sub3": {
                       "datatype": list,
                       "subs": {
                           # 专业名称
                           "sub1": {
                               "datatype": str,
                               "datarange": string.ascii_letters
                           },
                           # 学生成绩
                           "sub2": {
                               "datatype": float,
                               "datarange":(0,5)
                           },
                       }
                   },
               }
}


def generate_random_data(data_structure):
    if data_structure["datatype"] == tuple:
        data = ()
    elif data_structure["datatype"] == list:
        data = []

    for key, value in data_structure["subs"].items():
        if "datarange" in value:
            if value["datatype"] == str:
                random_data = ''.join(random.choice(value["datarange"]) for _ in range(10))
            elif value["datatype"] == int:
                random_data = random.randint(value["datarange"][0], value["datarange"][1])
            elif value["datatype"] == float:
                random_data = round(random.uniform(value["datarange"][0], value["datarange"][1]), 2)
        else:
            random_data = generate_random_data(value)

        if isinstance(data, tuple):
            data += (random_data,)
        elif isinstance(data, list):
            data.append(random_data)

    return data


def generate_random_students(num_students):
    student_info_list = []
    for _ in range(num_students):
        student_info = generate_random_data(dataStructure)
        student_info_list.append(student_info)

    return student_info_list


random_students = generate_random_students(random.randint(1, 100))
print(random_students)
