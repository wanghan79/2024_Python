from functools import wraps
import random
import time

class RandomDataGenerator:
    def __init__(self):
        pass

    def get_random(self, **kwargs):
        result = []
        for key, value in kwargs.items():
            if key == 'tuple':
                result.append(tuple(self.get_random(**value)))
            elif key == 'list':
                result.append(list(self.get_random(**value)))
            elif key == 'set':
                result.append(set(self.get_random(**value)))
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

if __name__ == "__main__":
    gen = RandomDataGenerator()
    my_dict = {'tuple': {'int': {'datarange': [1, 10]},
                         'list': {
                             'int': {'datarange': [1, 10]},
                             'float': {'datarange': [1, 10]},
                             'str': {'datarange': "gfzxcv", "datalength": 6},
                             'tuple': {'str': {'datarange': "gfzxcv", "datalength": 6}},
                             'tuple': {'int': {'datarange': [1, 10]},
                                       'list': {
                                           'int': {'datarange': [1, 10]},
                                           'float': {'datarange': [1, 10]},
                                           'str': {'datarange': "gfzxcv", "datalength": 6},
                                           'tuple': {'str': {'datarange': "gfzxcv", "datalength": 6}}
                                       }}
                         }}
    }
    print(gen.get_random(**my_dict))
