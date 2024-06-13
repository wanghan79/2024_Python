import random

# 定义生成数据样本的内层函数
def data_sample_inner(**kwargs):
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
        elif k in ['tuple', 'list', 'set']:
            tmp = data_sample_inner(**v)
            if k == 'tuple':
                result.append(tuple(tmp))
            elif k == 'list':
                result.append(tmp)
            elif k == 'set':
                result.append(set(tmp))
    return result

# 定义生成器函数 data_sample_generator
def data_sample_generator(num=1, **kwargs):
    for _ in range(num):
        yield data_sample_inner(**kwargs)

# 测试迭代器
if __name__ == '__main__':
    # 创建迭代器，并遍历生成数据样本
    iterator = data_sample_generator(
        num=5,
        tuple={
            'int': {'datarange': [1, 10]},
            'list': {
                'int': {'datarange': [1, 10]},
                'float': {'datarange': [1.0, 10.0]},
                'str': {'datarange': 'asdfghjkl', 'len': 8},
                'tuple': {
                    'str': {'datarange': 'qwertyuiop', 'len': 5}
                }
            }
        }
    )

    # 遍历迭代器，打印每个样本
    for sample in iterator:
        print(sample)
