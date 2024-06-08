import random
import string

def dataSampling(**kwargs):
    if kwargs['datatype'] == 'int':
        it = iter(kwargs['datarange'])
        return random.randint(next(it), next(it))
    elif kwargs['datatype'] == 'float':
        it = iter(kwargs['datarange'])
        return random.uniform(next(it), next(it))
    elif kwargs['datatype'] == 'str':
        if isinstance(kwargs['datarange'], tuple) and len(kwargs['datarange']) == 2:
            return ''.join(random.choices(string.ascii_letters, k=kwargs['datarange'][1]))
        else:
            return ''.join(random.choices(string.ascii_letters, k=kwargs['datarange']))
    elif kwargs['datatype'] in ('list', 'tuple'):
        elements = []
        for _ in range(kwargs.get('num', 1)):
            sub_elements = {}
            for sub_key, sub_kwargs in kwargs['subs'].items():
                sub_elements[sub_key] = dataSampling(**sub_kwargs)
            elements.append(sub_elements)
        if kwargs['datatype'] == 'list':
            return elements
        else:
            return tuple(elements)

def countDecorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        count_result = {}
        if isinstance(result, list):
            for item in result:
                for key, value in item.items():
                    count_result[key] = count_result.get(key, 0) + 1
        elif isinstance(result, dict):
            for key, value in result.items():
                count_result[key] = count_result.get(key, 0) + 1
        return result, count_result
    return wrapper

@countDecorator
def structDataSampling(para):
    result = {}
    result['num'] = para['num']
    result['data'] = []
    for _ in range(para['num']):
        data = {}
        for key, value in para['struct']['subs'].items():
            if isinstance(value, dict):
                data[key] = dataSampling(**value)
            else:
                data[key] = value
        result['data'].append(data)
    return result


para = {
    "num": 1,
    "struct": {
        "datatype": "list",
        "subs": {
            "int_data": {"datatype": "int", "datarange": [1, 100]},
            "float_data": {"datatype": "float", "datarange": [0.0, 1.0]},
            "list_data": {"datatype": "list", "subs": {"int_data": {"datatype": "int", "datarange": [1,47,68]}, "str_data": {"datatype": "str", "datarange": 10}}}     }
    }
}


result, count_result = structDataSampling(para)
print("Generated Data:", result)
print("Count Result:", count_result)


