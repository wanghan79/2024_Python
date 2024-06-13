import random
import string


class GenerateRandom:

    def __init__(self):
        pass

    def generateRandomData(self , *args , **kwargs):

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
            resultList.append(getData(**kwargs))
        return resultList

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

demo = GenerateRandom()
print(demo.generateRandomData(myInput(),**dataStructure))