import random
import string
class randomCreate:

    def getLists(self,num,list_min,list_max,types):
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
        return random.randint(-114, 514)

    def getRandomFloat(self):
        return random.uniform(-1.0, 1.0)

    def getRandomString(self):
        str0 = ""
        for i in range(5):
            str0 += random.choice(string.ascii_letters)
        return str0

seed=int(input("输入一个种子："))
random.seed(seed)
types = [int, float, str]
num = 10
list_min = 1
list_max = 20
lists = []
rc=randomCreate()
for _ in range(num):
    lists.append(rc.getLists(num,list_min,list_max,types))
for i, list1 in enumerate(lists):
    print(f"List {i + 1}: {list1}")
