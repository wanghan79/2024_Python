import random
import string
from functools import wraps


def calculate_statistics(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        int_sum, int_count, float_sum, float_count = 0, 0, 0.0, 0

        def calculate(data):
            nonlocal int_sum, int_count, float_sum, float_count
            if type(data) == int:
                # 这里其实还有个小插曲，这里我最开始写的是isinstance(data,int),结果data_sum和int_count 都多了1
                # 结果发现bool居然在这也会返回true，没想到bool居然是int的子类，震惊了
                # print(data)
                int_sum += data
                int_count += 1
            elif isinstance(data, float):
                float_sum += data
                float_count += 1
            elif isinstance(data, (list, tuple, set)):
                for item in data:
                    calculate(item)
            elif isinstance(data, dict):
                for value in data.values():
                    calculate(value)

        calculate(data)

        int_avg = int_sum / int_count if int_count > 0 else 0
        float_avg = float_sum / float_count if float_count > 0 else 0

        #print(int_count)
        print(f"int 类型的总和是 ： {int_sum}, Int 类型的平均值是: {int_avg}")
        print(f"Float 类型的总和是: {float_sum}, Float 类型的平均值是: {float_avg}")

        return data

    return wrapper


class generator:
    def __init__(self, **kwarg):
        self.result = self.generating_data(**kwarg)


    def generating_data(self, **kwargs):
        datatype = kwargs.get('data_type')
        data_range = kwargs.get('data_range')
        subs = kwargs.get('subs')
        if datatype == int:
            if len(data_range) == 1:
                return random.randint(0, data_range[0])
            elif len(data_range) == 2:
                min_num = min(data_range[0], data_range[1])
                max_num = max(data_range[0], data_range[1])
                return random.randint(min_num, max_num)
            else:
                random_index = random.randint(0, len(data_range) - 1)
                return data_range[random_index]
        elif datatype == bool:
            if len(data_range) == 1:
                return data_range[0]
            else:
                return random.choice([True, False])
        elif datatype == float:
            if len(data_range) == 1:
                return round(random.uniform(0, data_range[0]), 2)
            elif len(data_range) == 2:
                min_num = min(data_range[0], data_range[1])
                max_num = max(data_range[0], data_range[1])
                return round(random.uniform(min_num, max_num), 2)
            else:
                rnd_idx = random.randint(0, len(data_range) - 1)
                return data_range[rnd_idx]
        elif datatype == str:
            if isinstance(data_range, str):
                data_len = kwargs.get('len')
                return ''.join(random.choice(data_range) for _ in range(data_len))
            else:
                return "illegal data range!!! please make sure you input is str!!!"
        elif datatype == tuple:
            result = []
            for key, value in subs.items():
                result.append(self.generating_data(**value))
            return tuple(result)
        elif datatype == set:
            result = set()
            for key, value in subs.items():
                result.add(self.generating_data(**value))
            return result
        elif datatype == list:
            result = list()
            for key, value in subs.items():
                result.append(self.generating_data(**value))
            return result
        elif datatype == dict:
            result = dict()
            for key, value in subs.items():
                result[key] = self.generating_data(**value)
            return data_range(**result)
        else:
            return "illegal datatype !!! please check your input"

    @calculate_statistics
    def putout(self):
        return self.result


if __name__ == "__main__":
    example = {
        "data_type": tuple,
        "subs": {
            "sub1": {"data_type": list,
                     "subs": {
                         "sub1": {
                             "data_type": int,
                             "data_range": [100]
                         },
                         "sub2": {
                             "data_type": float,
                             "data_range": (0, 50)
                         },
                         "sub3": {
                             "data_type": str,
                             "data_range": string.ascii_uppercase,
                             "len": 3
                         },
                         "sub4": {
                             "data_type": int,
                             "data_range": [1, 2, 23, 4, 2, 34]
                         },
                     },
                     },
            "sub2": {"data_type": tuple,
                     "subs": {
                         "sub1": {
                             "data_type": int,
                             "data_range": (0, 100)
                         },
                         "sub2": {
                             "data_type": str,
                             "data_range": string.ascii_uppercase,
                             "len": 10
                         },
                         "sub3": {
                             "data_type": str,
                             "data_range": [123123],
                             "len": 10
                         },
                         "sub4": {
                             "data_type": bool,
                             "data_range": []
                         },
                         "sub5": {
                             "data_type": float,
                             "data_range": (0, 100)
                         },

                     },
                     },
            "sub3": {
                "data_type": str,
                "data_range": "abc",
                "len": 10

            },

        }
    }
    G = generator(**example)
    print(G.putout())
