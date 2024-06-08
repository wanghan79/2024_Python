import random
import string

def dataSampling(**kwargs):
    if kwargs['datatype'] == 'int':
        it = iter(kwargs['datarange'])
        yield random.randint(next(it), next(it))
    elif kwargs['datatype'] == 'float':
        it = iter(kwargs['datarange'])
        yield random.uniform(next(it), next(it))
    elif kwargs['datatype'] == 'str':
        if isinstance(kwargs['datarange'], tuple) and len(kwargs['datarange']) == 2:
            yield ''.join(random.choices(string.ascii_letters, k=random.randint(*kwargs['datarange'])))
        else:
            yield ''.join(random.choices(string.ascii_letters, k=kwargs['datarange']))
    elif kwargs['datatype'] in ('list', 'tuple'):
        elements = []
        for _ in range(kwargs.get('num', 1)):
            sub_elements = {}
            for sub_key, sub_kwargs in kwargs['subs'].items():
                sub_elements[sub_key] = next(dataSampling(**sub_kwargs))
            elements.append(sub_elements)
        if kwargs['datatype'] == 'list':
            yield elements
        else:
            yield tuple(elements)

def structDataSampling(para):
    result = {}
    result['num'] = para['num']
    result['data'] = []
    for _ in range(para['num']):
        data = {}
        for key, value in para['struct']['subs'].items():
            if isinstance(value, dict):
                data[key] = next(dataSampling(**value))
            else:
                data[key] = value
        result['data'].append(data)
    yield result

para = {
    "num": 1,
    "struct": {
        "datatype": "list",
        "subs": {
            "int_data": {"datatype": "int", "datarange": [1, 100]},
            "float_data": {"datatype": "float", "datarange": [0.0, 1.0]},
            "list_data": {
                "datatype": "list",
                "subs": {
                    "int_data": {"datatype": "int", "datarange": [1, 47]},
                    "str_data": {"datatype": "str", "datarange": (5, 10)}
                }
            }
        }
    }
}

result = next(structDataSampling(para))
print(result)
