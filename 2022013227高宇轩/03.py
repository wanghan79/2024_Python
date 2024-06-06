import random
from functools import wraps


# 定义装饰器函数，用于计算结果列表的和
def sum_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return sum(result)  # 返回结果列表的和

    return wrapper


# 定义装饰器函数，用于计算结果列表的平均值
def average_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return sum(result) / len(result)  # 返回结果列表的平均值

    return wrapper


# 定义数据生成类
class DataSampling(object):
    # 使用sum_decorator装饰器，计算数据和
    @sum_decorator
    def data_sampling_sum(self, **kwargs):
        return self.data_sampling(**kwargs)

    # 使用average_decorator装饰器，计算数据平均值
    @average_decorator
    def data_sampling_average(self, **kwargs):
        return self.data_sampling(**kwargs)

    # 生成数据的方法
    def data_sampling(self, **kwargs):
        typ = kwargs.get('data_type')  # 获取数据类型
        data_range = kwargs.get('data_range')  # 获取数据范围
        inner = kwargs.get('subs')  # 获取内部数据

        # 根据数据类型生成数据
        if typ == int:
            if len(data_range) == 1:
                return [data_range[0]]
            elif len(data_range) == 2:
                range_l = data_range[0]
                range_r = data_range[1]
                return [random.randint(range_l, range_r)]
            else:
                rnd_idx = random.randint(0, len(data_range) - 1)
                return [data_range[rnd_idx]]
        elif typ == bool:
            if len(data_range) == 1:
                return [data_range[0]]
            else:
                return [random.random() < 0.5]
        elif typ == float:
            if len(data_range) == 1:
                return [data_range[0]]
            elif len(data_range) == 2:
                range_l = data_range[0]
                range_r = data_range[1]
                return [random.uniform(range_l, range_r)]
            else:
                rnd_idx = random.randint(0, len(data_range) - 1)
                return [data_range[rnd_idx]]
        elif typ == str:
            if isinstance(data_range, str):
                data_len = kwargs['len']
                return [''.join(random.choice(data_range) for _ in range(data_len))]
            else:
                rnd_idx = random.randint(0, len(data_range) - 1)
                return [data_range[rnd_idx]]
        elif typ == tuple:
            result = []
            for k, v in inner.items():
                result.extend(self.data_sampling(**v))
            return [tuple(result)]
        elif typ == set:
            result = set()
            for k, v in inner.items():
                result.add(self.data_sampling(**v)[0])
            return [result]
        elif typ == list:
            result = list()
            for k, v in inner.items():
                result.extend(self.data_sampling(**v))
            return [result]
        else:
            result = dict()
            for k, v in inner.items():
                result[k] = self.data_sampling(**v)[0]
            return [typ(**result)]


sampling = DataSampling()
# 计算随机数的和
result_sum = sampling.data_sampling_sum(data_type=int, data_range=[1, 10], subs={})
print("Sum of random numbers:", result_sum)

# 计算随机数的平均值
result_average = sampling.data_sampling_average(data_type=int, data_range=[1, 10], subs={})
print("Average of random numbers:", result_average)
