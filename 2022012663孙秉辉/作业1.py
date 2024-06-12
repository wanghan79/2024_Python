import random
def getRandom(**kwargs):
    result = []
    for key, value in kwargs.items():
        if key == 'int':
            a, b = value['datarange']
            result.append(random.randint(a, b))
        elif key == 'float':
            a, b = value['datarange']
            result.append(random.uniform(a, b))
        elif key == 'str':
            result.append(''.join(random.SystemRandom().choice(value['datarange'])for _ in range(value['len'])))
        elif key == 'tuple':
            result.append(tuple(getRandom(**value)))
        elif key == 'list':
            result.append(list(getRandom(**value)))
        elif key == 'set':
            result.append(set(getRandom(**value)))
    return result

my_dict = {
    'num': 10,
    'int': {'datarange': (5, 10)},
    'float': {'datarange': (0, 100.0)},
    'str': {'datarange': 'avbshcmg', 'len': 10},
    'list': {'int': {'datarange': (0, 10)},
             'list': {'str': {'datarange': 'abcde','len': 4},
                      'float': {'datarange': (10.2, 29.3)}
                      },
             'tuple': {'float': {'datarange': (0, 1)},
                       'int': {'datarange': (5, 7)}
                       }
             }
}
for i in range(my_dict['num']):
    print(getRandom(**my_dict))
