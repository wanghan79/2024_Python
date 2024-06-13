import random
import string
seed=int(input("输入一个种子："))
random.seed(seed)
types = [int, float, str]
num = 10
list_min = 1
list_max = 20
lists = []
for _ in range(num):
    count = random.randint(list_min, list_max)
    list0=[]
    for _ in range(count):
        type0 = random.choice(types)
        if type0 == int:
            list0.append(random.randint(-114,514))
        elif type0 == float:
            list0.append((random.uniform(-1.0,1.0)))
        elif type0 == str:
            str0=""
            for i in range(5):
                str0+=random.choice(string.ascii_letters)
            list0.append(str0)
    lists.append(list0)
for i, list1 in enumerate(lists):
    print(f"List {i + 1}: {list1}")
