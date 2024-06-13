import random
import string


def count_decorator(func):
    def wrapper(self, kwargs):
        result = func(self, kwargs)
        if kwargs['type'] in self.counts:
            self.counts[kwargs['type']] += 1
        return result

    return wrapper


class DataSampler:
    def __init__(self):
        self.random = random
        self.counts = {'int': 0, 'float': 0, 'str': 0, 'list': 0, 'tuple': 0}

    @count_decorator
    def data_sampling(self, kwargs):
        if kwargs['type'] == 'int':
            it = iter(kwargs['range'])
            yield self.random.randint(next(it), next(it))
        elif kwargs['type'] == 'float':
            it = iter(kwargs['range'])
            yield self.random.uniform(next(it), next(it))
        elif kwargs['type'] == 'str':
            if isinstance(kwargs['range'], str):
                yield self.random.choice(kwargs['range'])
            elif isinstance(kwargs['range'], int):
                yield ''.join(self.random.choices(string.ascii_letters, k=kwargs['range']))
        elif kwargs['type'] == 'list':
            elements = (self.data_sampling(sub_kwargs) for sub_key, sub_kwargs in kwargs['subs'].items())
            yield [next(element) for element in elements]
        elif kwargs['type'] == 'tuple':
            elements = (self.data_sampling(sub_kwargs) for sub_key, sub_kwargs in kwargs['subs'].items())
            yield tuple(next(element) for element in elements)

    def apply(self, num, struct):
        for _ in range(num):
            yield from self.data_sampling(struct)

    def sum_and_avg(self, num, struct):
        total_sum = 0
        count = 0

        for result in self.apply(num, struct):
            def recursive_sum_and_count(element):
                nonlocal total_sum, count
                if isinstance(element, (int, float)):
                    total_sum += element
                    count += 1
                elif isinstance(element, (list, tuple)):
                    for item in element:
                        recursive_sum_and_count(item)

            recursive_sum_and_count(result)

        avg = total_sum / count if count > 0 else 0
        return total_sum, avg

    def get_counts(self):
        return self.counts


para = {
    "num": 5,
    "struct": {
        "type": "list",
        "subs": {
            "element1": {
                "type": "int",
                "range": (0, 10)
            },
            "element2": {
                "type": "float",
                "range": (0.0, 1.0)
            },
            "element3": {
                "type": "str",
                "range": 5
            },
            "element4": {
                "type": "list",
                "subs": {
                    "sub_element1": {
                        "type": "int",
                        "range": (0, 5)
                    },
                    "sub_element2": {
                        "type": "str",
                        "range": 3
                    }
                }
            }
        }
    }
}

# 创建DataSampler实例并调用apply方法
sampler = DataSampler()
results = list(sampler.apply(**para))
print(results)

# 创建DataSampler实例并调用sum_and_avg方法
total_sum, avg = sampler.sum_and_avg(**para)
print("Total sum:", total_sum)
print("Avg:", avg)

# 打印各类型数据计数
print("Data counts:", sampler.get_counts())
