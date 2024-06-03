import random


class RandomData():
    def __init__(self, **kwargs):
        self.mydict = kwargs
        self.result = []

    def randomInt(self, datarange):
        return random.randint(datarange[0], datarange[1])

    def randomfloat(self, range):
        return random.uniform(range[0], range[1])

    def randomstr(self, datarange, str_len):
        return ''.join(random.choice(datarange) for _ in range(str_len))

    def randomlist(self, **kwargs):
        ans = []
        ans.append(self.generate(**kwargs))
        return ans

    def randomtuple(self, **kwargs):
        ans = []
        ans.append(self.generate(**kwargs))
        return tuple(ans)

    def generate(self, **kwargs):
        ans = []
        for k, v in kwargs.items():
            if k == 'int':
                ans.append(self.randomInt(v['datarange']))
            elif k == 'float':
                ans.append(self.randomfloat(v['datarange']))
            elif k == 'str':
                ans.append(self.randomstr(v['datarange'], v['len']))
            elif k == 'list':
                ans.append(self.randomlist(**v))
            elif k == 'tuple':
                ans.append(self.randomtuple(**v))
        return ans

    def get(self):
        self.result = self.generate(**self.mydict)
        return self.result


parm = {'int': {'datarange': [0, 10]}, 'str': {'datarange': 'liupeiyan', 'len': 10},
        'tuple': {'int': {'datarange': [0, 10]}, 'str': {'datarange': 'liupeiyan', 'len': 10}}}
R = RandomData(**parm)
print(R.get())

