import random
import string

def Sat(process_func):
    def decorator(func):
        def wrapper(*args, **kwargs):

            results = func(*args, **kwargs)
            processed_results = process_func(results, **kwargs)

            return processed_results
        return wrapper
    return decorator

def dataSampling(kwargs):
    if kwargs['datatype'] == 'int':
        it = iter(kwargs['datarange'])
        return random.randint(next(it), next(it))
    elif kwargs['datatype'] == 'float':
        it = iter(kwargs['datarange'])
        return random.uniform(next(it), next(it))
    elif kwargs['datatype'] == 'str':
        if isinstance(kwargs['datarange'], str):
            return random.choice(kwargs['datarange'])
        elif isinstance(kwargs['datarange'], int):
            return ''.join(random.SystemRandom().choice(string.ascii_letters) for _ in range(kwargs['datarange']))
    elif kwargs['datatype'] in ('list', 'tuple'):
        elements = []
        for sub_key, sub_kwargs in kwargs['subs'].items():
            elements.append(dataSampling(sub_kwargs))
        if kwargs['datatype'] == 'list':
            return elements
        else:
            return tuple(elements)

def count_data(results):
    count = 0
    for result in results:
        if isinstance(result, (int, float)):
            count += 1
        elif isinstance(result, (list, tuple)):
            count += count_data(result)
    return count

def sum_data(results):
    total_sum = 0
    for result in results:
        if isinstance(result, (int, float)):
            total_sum += result
        elif isinstance(result, (list, tuple)):
            total_sum += sum_data(result)
    return total_sum

def mean_data(results):
    total_sum = sum_data(results)
    count = count_data(results)
    return total_sum / count if count else 0

def operation(results, **kwargs):
    type = kwargs.get('operation')
    list = []
    if type == 'both':
        list.append(sum_data(results))
        list.append(mean_data(results))
    elif type == 'sum':
        list.append(sum_data(results))
        list.append('do not need to calculate')
    elif type == 'mean':
        list.append('do not need to calculate')
        list.append(mean_data(results))
    elif type == 'none':
        list.append('do not need to calculate')
        list.append('do not need to calculate')
    return list

para = {"num": 5,
        "operation":"both",
        "struct": {
            "datatype": "tuple",
            "subs": {
                "sub1": {
                    "datatype": "tuple",
                    "subs": {
                        "sub1": {
                            "datatype": "int",
                            "datarange": (0, 100)
                        },
                        "sub2": {
                            "datatype": "str",
                            "datarange": "abcd"
                        }
                    }
                },
                "sub2": {
                    "datatype": "tuple",
                    "subs": {
                        "sub1": {
                            "datatype": "float",
                            "datarange": (0, 5000)
                        },
                        "sub2": {
                            "datatype": "int",
                            "datarange": (1, 200)
                        }
                    }
                },
                "sub3": {
                    "datatype": "str",
                    "datarange": "efgh"
                }
            }
        }
    }
def apply(**kwargs):
    results = []
    for i in range(kwargs['num']):
        result = dataSampling(kwargs['struct'])
        results.append(result)
    yield results

results=apply(**para)
for index,value in enumerate(results):
    for j,v in enumerate(value):
        print(f"random structure {j} :{v}")

@Sat(operation)
def apply(**kwargs):
    results = []
    for i in range(kwargs['num']):
        result = dataSampling(kwargs['struct'])
        results.append(result)
    return results


operationRes = apply(**para)

print(f"Sum: {operationRes[0]}\nMean: {operationRes[1]}")
