import random
import time

def generate_int(datarange):
    return random.randint(datarange[0], datarange[1])

def generate_float(datarange):
    return random.uniform(datarange[0], datarange[1])

def generate_str(datarange, length):
    return ''.join(random.choice(datarange) for _ in range(length))

def data_sample_inner(**kwargs):
    result = []
    for k, v in kwargs.items():
        if k == 'int':
            result.append(generate_int(v['datarange']))
        elif k == 'float':
            result.append(generate_float(v['datarange']))
        elif k == 'str':
            result.append(generate_str(v['datarange'], v['len']))
        elif k == 'tuple':
            tmp = data_sample_inner(**v)
            result.append(tuple(tmp))
        elif k == 'list':
            tmp = data_sample_inner(**v)
            result.append(tmp)
        elif k == 'set':
            tmp = data_sample_inner(**v)
            result.append(set(tmp))
    return result

def data_sample(num, **kwargs):
    result = []
    for _ in range(num):
        result.append(data_sample_inner(**kwargs))
    return result

def my_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print("Function is about to execute with arguments:", args, kwargs)

        result = func(*args, **kwargs)

        end_time = time.time()
        print(f"Function {func.__name__} executed in {end_time - start_time} seconds")
        return result

    return wrapper

@my_decorator
def data_sample_decorated(num, **kwargs):
    return data_sample(num, **kwargs)

if __name__ == '__main__':
    # 使用装饰后的函数
    sample = data_sample_decorated(
        num=5,
        tuple={
            'int': {'datarange': [1, 10]},
            'list': {
                'int': {'datarange': [1, 10]},
                'float': {'datarange': [1.0, 10.0]},
                'str': {'datarange': 'asdfghjkl', 'len': 8},
                'tuple': {'str': {'datarange': 'qwertyuiop', 'len': 5}}
            }
        }
    )
    print(sample)
