import random
import string

def addLogging(decPara):
    def decorator(func):
        def wrapper(**kwargs):
            if decPara == "zcy":
                print("%s is running" % func.__name__)
            return func(**kwargs)
        return wrapper
    return decorator

def validate_params(params):
    for dtype, settings in params.items():
        if dtype in ['int', 'float']:
            if 'datarange' not in settings or not isinstance(settings['datarange'], list) or len(settings['datarange']) != 2:
                raise ValueError(f"Invalid datarange for {dtype}")
        elif dtype == 'str':
            if 'datarange' not in settings or not isinstance(settings['datarange'], str):
                raise ValueError(f"Invalid datarange for {dtype}")
            if 'len' not in settings or not isinstance(settings['len'], int):
                raise ValueError("Invalid length for str")
        elif dtype in ['tuple', 'list', 'set']:
            validate_params(settings)
        else:
            raise ValueError(f"Unsupported data type: {dtype}")

@addLogging('zcy')
def data_sample(**kwargs):
    """
    :param kwargs: DataType DataRange(two elem) [len]
    :return: result->list
    """
    validate_params(kwargs)
    result = []

    for k, v in kwargs.items():
        if k == 'int':
            range_l, range_r = v['datarange']
            result.append(random.randint(range_l, range_r))
        elif k == 'float':
            range_l, range_r = v['datarange']
            result.append(random.uniform(range_l, range_r))
        elif k == 'str':
            chars = v['datarange']
            str_len = v['len']
            result.append(''.join(random.choice(chars) for _ in range(str_len)))
        elif k == 'tuple':
            result.append(tuple(data_sample(**v)))
        elif k == 'list':
            result.append(data_sample(**v))
        elif k == 'set':
            result.append(set(data_sample(**v)))
    
    return result

# Example parameters to generate diverse data
parm = {
    'tuple': {
        'int': {'datarange': [1, 20]},
        'list': {
            'int': {'datarange': [1, 10]},
            'float': {'datarange': [1.0, 10.0]},
            'str': {'datarange': string.ascii_letters + string.digits, 'len': 19},
            'tuple': {'str': {'datarange': string.ascii_lowercase, 'len': 10}}
        }
    }
}

result = data_sample(**parm)
print(result)
