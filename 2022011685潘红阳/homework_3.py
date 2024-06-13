import random
import string

def generateRandomData(func):
    def wrapper(*args , **kwargs):
        resultList = list()

        def getData(**kwargs):
            result = list()
            for key, value in kwargs['subs'].items():
                if value['datatype'] is int:
                    it = iter(value['datarange'])
                    item = random.randint(next(it), next(it))
                elif value['datatype'] is float:
                    it = iter(value['datarange'])
                    item = random.uniform(next(it), next(it))
                elif value['datatype'] is str:
                    item = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(0, 10))
                elif value['datatype'] is tuple:
                    list_tuple = getData(**value)
                    item = tuple(list_tuple)
                elif value['datatype'] is list:
                    item = getData(**value)
                elif value['datatype'] is set:
                    list_set = getData(**value)
                    item = set(list_set)
                else:
                    getData(**value)
                result.append(item)
            return kwargs['datatype'](result)

        for i in range(args[0]):
            data = getData(**kwargs)
            resultList.append(data)
            print(data)
        print(func(resultList))
    return wrapper

@generateRandomData
def func(list):
    print("请输入需要的操作：")
    print("1.整数求和")
    print("2.浮点数求和")
    print("3.整数求平均值")
    print("4.浮点数求平均值")
    choice = int(input())
    if choice == 1:
        return getIntSum(list)
    elif choice == 2:
        return getFloatSum(list)
    elif choice == 3:
        return getIntAverage(list)
    elif choice == 4:
        return getFloatAverage(list)

def getIntSum(list):
    sum = 0
    for i in range(len(list)):
        for j in range(len(list[i])):
            for k in range(len(list[i][j])):
                if isinstance(list[i][j][k] , int):
                    sum = sum + list[i][j][k]
    return sum

def getIntAverage(list):
    sum = 0
    count = 0
    for i in range(len(list)):
        for j in range(len(list[i])):
            for k in range(len(list[i][j])):
                if isinstance(list[i][j][k], int):
                    sum = sum + list[i][j][k]
                    count = count + 1
    return sum / count

def getFloatSum(list):
    sum = 0
    for i in range(len(list)):
        for j in range(len(list[i])):
            for k in range(len(list[i][j])):
                if isinstance(list[i][j][k], float):
                    sum = sum + list[i][j][k]
    return sum

def getFloatAverage(list):
    sum = 0
    count = 0
    for i in range(len(list)):
        for j in range(len(list[i])):
            for k in range(len(list[i][j])):
                if isinstance(list[i][j][k], float):
                    sum = sum + list[i][j][k]
                    count = count + 1
    return sum / count

dataStructure = {"datatype":tuple,
                 "subs":{
                     "sub1":{
                       "datatype":list,
                         "subs":{
                              "sub1":{
                                  "datatype":int,
                                  "datarange":(0,100)
                              },
                              "sub2":{
                                  "datatype":str,
                                  "datarange":string.ascii_uppercase
                              }
                         },
                     },
                      "sub2":{
                          "datatype":tuple,
                          "subs":{
                               "sub1":{
                                   "datatype":float,
                                   "datarange":(0,5000)
                               },
                              "sub2":{
                                  "datatype":int,
                                  "datarange":(1,200)
                              },
                          },
                      },
                     "sub3":{
                         "datatype":str,
                         "datarange":string.ascii_uppercase
                     }
                 }
}

def myInput():
    print("请输入需要获取的组数: ")
    count = int(input())
    return count

func(myInput() , **dataStructure)
