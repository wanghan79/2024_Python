import random
import time


# 原始的 data_sample_inner 函数
def data_sample_inner(**kwargs):
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
            tmp = data_sample_inner(**v)
            result.append(tuple(tmp))
        elif k == 'list':
            tmp = data_sample_inner(**v)
            result.append(tmp)
        elif k == 'set':
            tmp = data_sample_inner(**v)
            result.append(set(tmp))
    return result


# 原始的 data_sample 函数
def data_sample(**kwargs):
    global num
    dc = dict()
    for k, v in kwargs.items():
        if k == 'num':
            num = v
        else:
            dc[k] = v
    result = []
    for _ in range(int(num)):
        result.append(data_sample_inner(**dc))
    return result


# 装饰器定义
def my_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print("Function is about to execute with arguments:", args, kwargs)

        result = func(*args, **kwargs)

        end_time = time.time()
        print(f"Function {func.__name__} executed in {end_time - start_time} seconds")
        return result

    return wrapper


# 使用装饰器
@my_decorator
def data_sample_decorated(**kwargs):
    return data_sample(**kwargs)


if __name__ == '__main__':
    # 使用装饰后的函数
    print(data_sample_decorated(num=5,
                                tuple={'int': {'datarange': [1, 10]},
                                       'list': {'int': {'datarange': [1, 10]},
                                                'float': {'datarange': [1.0, 10.0]},
                                                'str': {'datarange': 'asdfghjkl', 'len': 8},
                                                'tuple': {'str': {'datarange': 'qwertyuiop', 'len': 5}}}}
                                ))