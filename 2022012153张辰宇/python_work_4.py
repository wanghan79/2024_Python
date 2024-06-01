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

def generate(**kwargs):
    """
    :param kwargs: DataType DataRange(two elem) [len]
    :return: result->list
    """
    validate_params(kwargs)
    result = []
    for k, v in kwargs.items():
        if k == 'int':
            for kk, vv in v.items():
                if kk == 'datarange':
                    range_l = vv[0]
                    range_r = vv[1]
                    result.append(random.randint(range_l, range_r))
        elif k == 'float':
            for kk, vv in v.items():
                if kk == 'datarange':
                    range_l = vv[0]
                    range_r = vv[1]
                    result.append(random.uniform(range_l, range_r))
        elif k == 'str':
            for kk, vv in v.items():
                if kk == 'datarange':
                    chars = vv
                elif kk == 'len':
                    str_len = vv
            result.append(''.join(random.choice(chars) for _ in range(str_len)))
        elif k == 'tuple':
            tmp = generate(**v)
            result.append(tuple(tmp))
        elif k == 'list':
            tmp = generate(**v)
            result.append(tmp)
        elif k == 'set':
            tmp = generate(**v)
            result.append(set(tmp))
    for x in result:
        yield x

parm = {
    'int': {'datarange': [1, 10]},
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
ans = generate(**parm)

def printf(obj):
    for x1 in obj:
        if type(x1).__name__ in ('int', 'str', 'float'):
            print(x1)
        else:
            printf(x1)

printf(ans)
