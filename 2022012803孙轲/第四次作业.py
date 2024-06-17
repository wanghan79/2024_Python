import random


def count_and_sum(iterable):
    total_count = 0
    total_sum = 0

    for item in iterable:
        if isinstance(item, (int, float)):
            total_count += 1
            total_sum += item
        elif isinstance(item, (list, tuple, set)):
            sub_count, sub_sum = count_and_sum(item)
            total_count += sub_count
            total_sum += sub_sum

    return total_count, total_sum


def loggin(message=None):
    def decorator(func):
        def inner(**kwargs):
            result = func(**kwargs)
            count, sum = count_and_sum(result)
            print(message)
            print(f'整型与浮点型数的个数是{count},它们的和是{sum}')
            return result

        return inner

    return decorator


@loggin("#hi")
def data_sample_(**kwargs):
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

    return data_sample(**kwargs)


def iter_(num):
    for _ in range(num):
        yield data_sample_(**parm)


chars = []
for i in range(32, 127):
    chars.append(chr(i))
parm = {'list': {'int': {'datarange': [99, 1000]}, 'float': {'datarange': [0.0001, 999.9991]},
                 'str': {'datarange': 'sunke', 'len': 12},
                 'tuple': {'int': {'datarange': [-99, 0]}, 'str': {'datarange': chars, 'len': 18}}},
        'set': {'float': {'datarange': [-88.1001, 99.1]}}}

if __name__ == '__main__':
    num = 100
    for _ in range(num):
        print(next(iter_(num)))
