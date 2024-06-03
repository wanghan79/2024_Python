import random


def data_sample(**kwargs):
    """
    :param kwargs: DataType DataRange(two elem) [len]
    :return: result->list
    """
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
            tmp = data_sample(**v)
            result.append(tuple(tmp))
        elif k == 'list':
            tmp = data_sample(**v)
            result.append(tmp)
        elif k == 'set':
            tmp = data_sample(**v)
            result.append(set(tmp))
    return result

parm = {'tuple': {'int': {'datarange': [1, 20]},
                                             'list': {'int': {'datarange': [1, 10]},
                                                      'float': {'datarange': [1, 10]},
                                                      'str': {'datarange': 'lpylpylpy', 'len': 19},
                                                      'tuple': {'str': {'datarange': 'liupeiyan', 'len': 10}}}}}
ans =data_sample(**parm)
print(ans)