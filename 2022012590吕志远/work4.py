import random
import string


class randomCreate:

    def getLists(self, num, list_min, list_max, types):
        count = random.randint(list_min, list_max)
        list0 = []
        for _ in range(count):
            type0 = random.choice(types)
            if type0 == int:
                list0.append(self.getRandomInt())
            elif type0 == float:
                list0.append(self.getRandomFloat())
            elif type0 == str:
                list0.append(self.getRandomString())
        return list0

    def getRandomInt(self):
        return random.randint(0, 100)

    def getRandomFloat(self):
        return random.uniform(-1.0, 1.0)

    def getRandomString(self):
        str0 = ""
        for i in range(5):
            str0 += random.choice(string.ascii_letters)
        return str0
# 修饰器，用来让平均值的小数位始终显示.5
def check(func):
    def getAverCheck(self,list):
        aver = func(self,list)
        s = int(aver) + 0.5
        aver = s if aver > s else int(aver)
        return aver

    return getAverCheck
class AverAndSum():

    def Choose(self, choice, list):
        if (choice == "求和"):
            return self.getSum(list)
        elif (choice == "取平均值"):
            return self.getAver(list)

    @check
    def getAver(self, list):
        sum = self.getSum(list)
        aver = sum * 1.0 / len(list)
        return aver

    def getSum(self, list):
        sum = 0
        for i in range(len(list)):
            sum += list[i]
        return sum

    def check(func):
        def realCheck(**t):
            aver = func(**t)
            s = int(aver) + 0.5
            aver = s if aver > s else int(aver)
            return aver

        return realCheck
choice = ""
while (1):
    choice = str(input("输入“求和”或是“取平均值”："))
    if choice == "求和" or choice == "取平均值":
        break
    else:
        print("请输入正确指令")
seed = int(input("输入一个种子："))
random.seed(seed)
types = [int]
num = 10
list_min = 1
list_max = 20
lists = []
rc = randomCreate()
aas = AverAndSum()
for _ in range(num):
    lists.append(rc.getLists(num, list_min, list_max, types))
list2 = []
for i in range(num):
    list2.append(aas.Choose(choice, lists[i]))
#迭代器
for i, list1 in enumerate(lists):
    if (choice == "求和"):
        print(f"学生 {i + 1} 成绩: {list1},总和: {list2[i]}")
    elif (choice == "取平均值"):
        print(f"学生 {i + 1} 成绩: {list1},平均值: {list2[i]}")
