import random
import string


class RandomData:
    def __init__(self, **kwargs):
        self.mydict = kwargs
        self.result = []
        self.validate_params(self.mydict)

    def validate_params(self, params):
        for dtype, settings in params.items():
            if dtype in ['int', 'float']:
                if 'datarange' not in settings or not isinstance(settings['datarange'], list) or len(settings['datarange']) != 2:
                    raise ValueError(f"Invalid datarange for {dtype}")
            elif dtype == 'str':
                if 'datarange' not in settings or not isinstance(settings['datarange'], str):
                    raise ValueError(f"Invalid datarange for {dtype}")
                if 'len' not in settings or not isinstance(settings['len'], int):
                    raise ValueError("Invalid length for str")
            elif dtype in ['tuple', 'list']:
                self.validate_params(settings)
            else:
                raise ValueError(f"Unsupported data type: {dtype}")

    def randomInt(self, datarange):
        return random.randint(datarange[0], datarange[1])

    def randomFloat(self, datarange):
        return random.uniform(datarange[0], datarange[1])

    def randomStr(self, datarange, str_len):
        return ''.join(random.choice(datarange) for _ in range(str_len))

    def randomList(self, **kwargs):
        return [self.generate(**kwargs)]

    def randomTuple(self, **kwargs):
        return tuple(self.generate(**kwargs))

    def generate(self, **kwargs):
        ans = []
        for k, v in kwargs.items():
            if k == 'int':
                ans.append(self.randomInt(v['datarange']))
            elif k == 'float':
                ans.append(self.randomFloat(v['datarange']))
            elif k == 'str':
                ans.append(self.randomStr(v['datarange'], v['len']))
            elif k == 'list':
                ans.append(self.randomList(**v))
            elif k == 'tuple':
                ans.append(self.randomTuple(**v))
        return ans

    def get(self):
        self.result = self.generate(**self.mydict)
        return self.result


parm = {
    'int': {'datarange': [0, 100]},
    'float': {'datarange': [0.0, 100.0]},
    'str': {'datarange': string.ascii_letters + string.digits, 'len': 10},
    'tuple': {
        'int': {'datarange': [0, 50]},
        'str': {'datarange': string.ascii_lowercase, 'len': 15}
    }
}

R = RandomData(**parm)
print(R.get())
