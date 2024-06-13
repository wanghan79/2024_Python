
import random
import string


def dataSampling(kwargs):
    if kwargs['type'] == 'int':
        it = iter(kwargs['range'])
        return random.randint(next(it), next(it))
    elif kwargs['type'] == 'float':
        it = iter(kwargs['range'])
        return random.uniform(next(it), next(it))
    elif kwargs['type'] == 'str':
        if isinstance(kwargs['range'], str):
            return random.choice(kwargs['range'])
        elif isinstance(kwargs['range'], int):
            return ''.join(random.SystemRandom().choice(string.ascii_letters) for _ in range(kwargs['range']))
    elif kwargs['type'] in ('list', 'tuple'):
        elements = [dataSampling(sub_kwargs) for sub_key, sub_kwargs in kwargs['subs'].items()]
        return elements if kwargs['type'] == 'list' else tuple(elements)

def apply(**kwargs):
    results = []
    for i in range(kwargs['num']):
        result = dataSampling(kwargs['struct'])
        results.append(result)
    return results


para = {
    "num": 5,
    "struct": {
        "type": "list",
        "subs": {
            "element1": {
                "type": "int",
                "range": (0, 10)
            },
            "element2": {
                "type": "float",
                "range": (0.0, 1.0)
            },
            "element3": {
                "type": "str",
                "range": 5
            }
        }
    }
}

print(apply(**para))
