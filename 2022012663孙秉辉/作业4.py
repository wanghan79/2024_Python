import random
def generate_random(value):
    if isinstance(value, dict):
        for key, inner_value in value.items():
            if key == 'int':
                a, b = inner_value['datarange']
                yield random.randint(a, b)
            elif key == 'float':
                a, b = inner_value['datarange']
                yield random.uniform(a, b)
            elif key == 'str':
                yield ''.join(random.choice(inner_value['datarange']) for _ in range(inner_value['len']))
            elif key == 'list':
                yield list(generate_random(inner_value))
            elif key == 'set':
                yield set(generate_random(inner_value))
            elif key == 'tuple':
                yield tuple(generate_random(inner_value))

def getRandom(**kwargs):
    for _ in range(kwargs['num']):
        yield list(generate_random(kwargs))

my_dict = {
    'num': 10,
    'int': {'datarange': (5, 10)},
    'float': {'datarange': (0, 100.0)},
    'str': {'datarange': 'avbshcmg', 'len': 10},
    'list': {'int': {'datarange': (0, 10)},
             'list': {'str': {'datarange': 'abcde', 'len': 4},
                      'float': {'datarange': (10.2, 29.3)}
                      },
             'tuple': {'float': {'datarange': (0, 1)},
                       'int': {'datarange': (5, 7)}
                       }
             }
}

for data in getRandom(**my_dict):
    print(data)
