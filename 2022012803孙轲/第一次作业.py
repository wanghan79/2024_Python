import random


def data_sample(**kwargs):
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
            result.append(list(tmp))
        elif k == 'set':
            tmp = data_sample(**v)
            result.append(set(tmp))
    return result


chars = []
for i in range(32, 127):
    chars.append(chr(i))
parm = {'list': {'int': {'datarange': [99, 1000]}, 'float': {'datarange': [0.0001, 999.9991]},
                 'str': {'datarange': 'sunke', 'len': 12},
                 'tuple': {'int': {'datarange': [-99, 0]}, 'str': {'datarange': chars, 'len': 18}}},
        'set': {'float': {'datarange': [-88.1001, 99.1]}}}
ans = data_sample(**parm)
print(ans)
