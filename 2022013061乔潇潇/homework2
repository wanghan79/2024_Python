import random
import string


class DataSampler:
    def __init__(self):
        self.random = random

    def data_sampling(self, kwargs):
        if kwargs['type'] == 'int':
            it = iter(kwargs['range'])
            return self.random.randint(next(it), next(it))
        elif kwargs['type'] == 'float':
            it = iter(kwargs['range'])
            return self.random.uniform(next(it), next(it))
        elif kwargs['type'] == 'str':
            if isinstance(kwargs['range'], str):
                return self.random.choice(kwargs['range'])
            elif isinstance(kwargs['range'], int):
                return ''.join(self.random.choices(string.ascii_letters, k=kwargs['range']))
        elif kwargs['type'] in ('list', 'tuple'):
            elements = [self.data_sampling(sub_kwargs) for sub_key, sub_kwargs in kwargs['subs'].items()]
            return elements if kwargs['type'] == 'list' else tuple(elements)

    def apply(self, num, struct):
        results = []
        for i in range(num):
            result = self.data_sampling(struct)
            results.append(result)
        return results

    def sum_and_avg(self, num, struct):
        results = self.apply(num, struct)
        total_sum = 0
        count = 0
        for result in results:
            if isinstance(result, (int, float)):
                total_sum += result
                count += 1
            elif isinstance(result, (list, tuple)):
                for item in result:
                    if isinstance(item, (int, float)):
                        total_sum += item
                        count += 1

        avg = total_sum / count if count > 0 else 0
        return total_sum, avg


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

# 创建DataSampler实例并调用sum_and_avg方法
sampler = DataSampler()
print(sampler.apply(**para))
total_sum, avg = sampler.sum_and_avg(**para)
print("Total sum:", total_sum)
print("Avg:", avg)
