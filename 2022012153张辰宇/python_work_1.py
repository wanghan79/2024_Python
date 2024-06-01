import random
import string

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

def data_sample(**kwargs):
    """
    :param kwargs: DataType DataRange(two elem) [len]
    :return: result->list
    """
    validate_params(kwargs)
    result = []

    for dtype, settings in kwargs.items():
        if dtype == 'int':
            range_l, range_r = settings['datarange']
            result.append(random.randint(range_l, range_r))
        elif dtype == 'float':
            range_l, range_r = settings['datarange']
            result.append(random.uniform(range_l, range_r))
        elif dtype == 'str':
            chars = settings['datarange']
            str_len = settings['len']
            result.append(''.join(random.choice(chars) for _ in range(str_len)))
        elif dtype == 'tuple':
            result.append(tuple(data_sample(**settings)))
        elif dtype == 'list':
            result.append(data_sample(**settings))
        elif dtype == 'set':
            result.append(set(data_sample(**settings)))
    
    return result

# Example parameters to generate diverse data
parm = {
    'tuple': {
        'int': {'datarange': [1, 100]},
        'list': {
            'int': {'datarange': [1, 50]},
            'float': {'datarange': [1.0, 100.0]},
            'str': {'datarange': string.ascii_letters + string.digits, 'len': 10},
            'tuple': {'str': {'datarange': string.ascii_lowercase, 'len': 15}}
        }
    }
}

ans = data_sample(**parm)
print(ans)
