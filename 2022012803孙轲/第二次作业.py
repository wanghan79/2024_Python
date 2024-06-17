import random


class RandomGenerate:
    def __init__(self, **kwargs):
        self.mydict = kwargs
        self.result = []

    def if_int(self, **kwargs):
        for k, v in kwargs.items():
            pass
        return random.randint(v[0], v[1])

    def if_float(self, **kwargs):
        for k, v in kwargs.items():
            pass
        return random.uniform(v[0], v[1])

    def if_str(self, **kwargs):
        for k, v in kwargs.items():
            if k == 'datarange':
                chars = v
            elif k == 'len':
                str_len = v
        return ''.join(random.choice(chars) for _ in range(str_len))

    def if_tuple(self, **v):
        return tuple(self.generate(**v))

    def if_set(self, **v):
        return set(self.generate(**v))

    def if_list(self, **v):
        return list(self.generate(**v))

    def generate(self, **kwargs):
        result = []
        for k, v in kwargs.items():
            if k == 'int':
                result.append(self.if_int(**v))
            elif k == 'float':
                result.append(self.if_float(**v))
            elif k == 'str':
                result.append(self.if_str(**v))
            elif k == 'tuple':
                result.append(self.if_tuple(**v))
            elif k == 'list':
                result.append(self.if_list(**v))
            elif k == 'set':
                result.append(self.if_set(**v))
        return result

    def get(self):
        return self.generate(**self.mydict)


chars = []
for i in range(32, 127):
    chars.append(chr(i))
parm = {'list': {'int': {'datarange': [99, 1000]}, 'float': {'datarange': [0.0001, 999.9991]},
                 'str': {'datarange': 'sunke', 'len': 12},
                 'tuple': {'int': {'datarange': [-99, 0]}, 'str': {'datarange': chars, 'len': 18}}},
        'set': {'float': {'datarange': [-88.1001, 99.1]}}}
ans = RandomGenerate(**parm)
print(ans.get())

