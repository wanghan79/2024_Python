# class MyClass(object):
#     classVar = 456
#
#     def __init__(self,index):
#         self.memVar = index
#         self.memlist= list()
#
#     def memberFunction(self): #固定，可变，默认，关键字
#         print("This is a member function in MyClass")
#
#     def __privateFunction(self):
#         print("This is a private function in MyClass")
#
#     def __copy__(self):
#         print("This is a inherate function in MyClass")
#         #super(MyClass,self).__copy__()
#
#     def __str__(self):
#         #super().__str__()
#         return "MyClass"
#
#     def __del__(self):
#         pass
#
#     def __eq__(self, other):
#         pass
#
#     def __hash__(self):
#         return self.memVar
#
#     @staticmethod
#     def staticFunction():
#         print("This is a static function in MyClass")
#
#     @classmethod
#     def classFunction(cls):
#         print("This is a class function in MyClass")
#
# if __name__ =="__main__":
#     mc1 = MyClass(1)
#     mc2 = MyClass(1)
#     print(MyClass.classVar)
#     print(mc1.memVar)
#     print(mc2.memVar)
#     MyClass.classVar = 567
#     print(mc1.classVar)
#     print(mc2.classVar)
#
#     mc1.memberFunction()
#     mc1.staticFunction()
#     mc1.classFunction()
#
#     MyClass.memberFunction(mc1) == mc1.memberFunction()
#     MyClass.staticFunction()
#
#     # mc1 = TestClass()
#     # mc2 = TestClass()
#     aset = {mc1, mc2}
#     print(mc1.__hash__())
#     print(id(mc1))
#     print(mc2.__hash__())
#     mc3 = mc1
#     print(mc2.__hash__())
#     print(aset)
#
#
#
import random

class ClassTest(object):
    my_dict = {
        'tuple': {
            'int': {
                'datarange': [1, 10]
            },
            'float': {
                'datarange': [100, 1000]
            },
            'list': {
                'int': {
                    'datarange': [1, 50]
                },
                'float': {
                    'datarange': [1, 10]
                },
                'str': {
                    'datarange': "abcefghijklmnopqrstuvwxyz",
                    "datalength": 6
                },
                'tuple': {
                    'str': {
                        'datarange': "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                        "datalength": 6
                    }
                }
            }
        }
    }

    @staticmethod
    def get_random(**kwargs):
        result = []
        for key, value in kwargs.items():
            if key == 'tuple':
                result.append(tuple(ClassTest.get_random(**value)))
            elif key == 'list':
                result.append(list(ClassTest.get_random(**value)))
            elif key == 'set':
                result.append(set(ClassTest.get_random(**value)))
            elif key == 'int':
                a, b = value['datarange']
                result.append(random.randint(a, b))
            elif key == 'float':
                a, b = value['datarange']
                result.append(random.uniform(a, b))
            elif key == 'str':
                datarange = value["datarange"]
                datalength = value["datalength"]
                result.append(''.join(random.choice(datarange) for _ in range(datalength)))
            else:
                print("This is an undefined type")
                result.append("********")
        return result

    @staticmethod
    def getSample(**kwargs):
        dc = dict()
        for k, v in kwargs.items():
            if k == 'num':
                num = v
            else:
                dc[k] = v
        result = []
        result.append(ClassTest.get_random(**dc))
        return result

    def compute_operation(self, data, operation):
        total_sum = 0
        count = 0
        if isinstance(data, list) or isinstance(data, tuple):
            for item in data:
                sub_total = self.compute_operation(item, operation)
                total_sum += sub_total
                count += 1
        elif isinstance(data, int):
            total_sum += data
            count += 1

        if operation == 1:  # 求和
            return total_sum
        elif operation == 2:  # 求平均
            if count == 0:
                return 0
            return total_sum / count





if __name__ == '__main__':
    N = int(input("Please scan in the number of random samples you need:"))
    test = ClassTest()
    for i in range(N):
        result_data = ClassTest.getSample(**ClassTest.my_dict)
        print("Generated Random Data",i,":")
        print(result_data)

        total_sum = test.compute_operation(result_data, 1)  # 求和操作
        print("Total Sum of 'int' Values in Random Data:", total_sum)

        average = test.compute_operation(result_data, 2)  # 求平均操作
        print("Average of 'int' Values in Random Data:", average)
        print('\n')




