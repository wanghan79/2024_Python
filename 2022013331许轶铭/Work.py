import random
import string

def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def outer(func):
    def inner(*args, **kwargs):
        sum = 0
        ans = func(*args, **kwargs)
        if type(ans) is list:
            index = 0
            while index < len(ans):
                sum += ans[index]
                index += 1
            avg = sum / len(ans)
            print(ans, sum, avg)
        else:
            print(ans)
    return inner

class Data:
    datatype = None
    rangel = None
    ranger = None
    num = None
    def __init__(self, datatype, rangel, ranger, num):
        self.datatype = datatype
        self.rangel = int(rangel)
        self.ranger = int(ranger)
        self.num = int(num)

    @outer
    def Random(self):
        ans = []
        if datatype == 'int':
            index = 1
            while index <= self.num:
                randnumber = random.randint(self.rangel, self.ranger)
                ans.insert(index - 1, randnumber)
                index += 1
            return ans
        elif datatype == 'float':
            index = 1
            while index <= self.num:
                randnumber = random.uniform(self.rangel, self.ranger)
                ans.insert(index - 1, randnumber)
                index += 1
            return ans
        elif datatype == 'str':
            ansstr = generate_random_string(self.num)
            return ansstr
        else:
            ansstr = "The datatype is wrong"
            return ansstr

datatype = input()
rangel = input()
ranger = input()
num = input()
data = Data(datatype, rangel, ranger, num)
data.Random()
