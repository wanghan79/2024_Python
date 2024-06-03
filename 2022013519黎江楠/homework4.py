import queue
import random
import string


class Student:
    def __init__(self, name, age, whereyougo):
        self.name = name
        self.age = age
        self.whereyougo = whereyougo

    def __str__(self):
        return f'Student name:{self.name} age:{self.age} goto:{self.whereyougo}'

    def __repr__(self):
        return f'Student name:{self.name} age:{self.age} goto:{self.whereyougo}'


example = {
    "data_type": tuple,
    "subs": {
        "sub1": {"data_type": list,
                 "subs": {
                     "sub1": {
                         "data_type": int,
                         "data_range": (0, 100)
                     },
                     "sub2": {
                         "data_type": str,
                         "data_range": string.ascii_uppercase,
                         "len": 5
                     }
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
                         "len": 5
                     }
                 },
                 },
        "sub3": {
            "data_type": str,
            "data_range": string.ascii_lowercase,
            "len": 5
        },
        "sub4": {
            "data_type": list,
            "subs": {
                "sub1": {
                    "data_type": Student,
                    "subs": {
                        "name": {
                            "data_type": str,
                            "data_range": "QWERTY",
                            "len": 10
                        },
                        "age": {
                            "data_type": int,
                            "data_range": (0, 100)
                        },
                        "whereyougo": {
                            "data_type": str,
                            "data_range": ("Chongqing", "Sichuan", "Hubei", "Jilin", "Heilongjiang", "Shaanxi")
                        }
                    }
                },
                "sub2": {
                    "data_type": dict,
                    "subs": {
                        "home_land": {
                            "data_type": str,
                            "data_range": "Wanzhou, Chongqing",
                            "len": 5
                        },
                        "live_land": {
                            "data_type": str,
                            "data_range": "Changchun, Jilin",
                            "len": 5
                        },
                        "favourite_number": {
                            "data_type": int,
                            "data_range": (0, 100)
                        },
                        "interesting_number": {
                            "data_type": float,
                            "data_range": (100, 200)
                        }
                    }
                }
            }
        }
    }
}


def do_operation(*args):
    def decorator(func):
        def wrapper(self, **kwargs):
            result = func(self, **kwargs)
            for ops in args:
                ops.init_func()
            qu = queue.Queue(0)
            qu.put(result)
            while not qu.empty():
                frt = qu.get()
                for ops in args:
                    ops.midway_func(frt)
                if isinstance(frt, (int, float, str, bool)):
                    continue
                try:
                    # 处理一般的可迭代对象
                    if isinstance(frt, dict):
                        raise TypeError
                    for item in frt:
                        qu.put(item)
                except TypeError as e:
                    # 处理跟字典类似的(k,v)对象和字典
                    if not isinstance(frt, dict):
                        frt = frt.__dict__
                    for _, v in frt.items():
                        qu.put(v)
            ans = dict()
            for ops in args:
                key = ops.__class__.__name__ + str(ops.type_set)
                ans[key] = ops.final_func()
            return ans

        return wrapper

    return decorator


class DataOperation:
    def __init__(self, *calculate_types):
        if len(calculate_types) == 0:
            raise RuntimeError("缺少参数。需要放置至少一个类型。")
        self.type_set = set()
        for calculate_type in calculate_types:
            self.type_set.add(calculate_type)

    def init_func(self):
        pass

    def midway_func(self, item):
        pass

    def final_func(self):
        pass


class GetAverage(DataOperation):
    def __init__(self, *calculate_types):
        super().__init__(*calculate_types)
        self.nb_sum = 0.0
        self.nb_count = 0.0

    def init_func(self):
        self.nb_sum = 0.0
        self.nb_count = 0.0

    def midway_func(self, item):
        if type(item) in self.type_set:
            self.nb_sum += float(item)
            self.nb_count += 1

    def final_func(self):
        return self.nb_sum / self.nb_count


class GetSum(DataOperation):
    def __init__(self, *calculate_types):
        super().__init__(*calculate_types)
        self.nb_sum = 0.0

    def init_func(self):
        self.nb_sum = 0.0

    def midway_func(self, item):
        if type(item) in self.type_set:
            self.nb_sum += float(item)

    def final_func(self):
        return self.nb_sum


class DataSamplingOperation:
    def __init__(self, num, **kwargs):
        self.data_struct = kwargs.copy()
        self.num = num

    def __iter__(self):
        for _ in range(self.num):
            result = self.data_sampling(**self.data_struct)
            yield result

    @do_operation(GetAverage(int, float), GetSum(int, float))
    def data_sampling(self, **kwargs):
        def _data_sampling(**kwargs):
            typ = kwargs.get('data_type')
            data_range = kwargs.get('data_range')
            inner = kwargs.get('subs')
            if typ == int:
                if len(data_range) == 1:
                    return data_range[0]
                elif len(data_range) == 2:
                    range_l = data_range[0]
                    range_r = data_range[1]
                    return random.randint(range_l, range_r)
                else:
                    rnd_idx = random.randint(0, len(data_range) - 1)
                    return data_range[rnd_idx]
            elif typ == bool:
                if len(data_range) == 1:
                    return data_range[0]
                else:
                    return random.random() < 0.5
            elif typ == float:
                if len(data_range) == 1:
                    return data_range[0]
                elif len(data_range) == 2:
                    range_l = data_range[0]
                    range_r = data_range[1]
                    return random.uniform(range_l, range_r)
                else:
                    rnd_idx = random.randint(0, len(data_range) - 1)
                    return data_range[rnd_idx]
            elif typ == str:
                if isinstance(data_range, str):
                    data_len = kwargs['len']
                    return ''.join(random.choice(data_range) for _ in range(data_len))
                else:
                    rnd_idx = random.randint(0, len(data_range) - 1)
                    return data_range[rnd_idx]
            elif typ == tuple:
                result = []
                for k, v in inner.items():
                    result.append(_data_sampling(**v))
                return tuple(result)
            elif typ == set:
                result = set()
                for k, v in inner.items():
                    result.add(_data_sampling(**v))
                return result
            elif typ == list:
                result = list()
                for k, v in inner.items():
                    result.append(_data_sampling(**v))
                return result
            else:
                result = dict()
                for k, v in inner.items():
                    result[k] = _data_sampling(**v)
                return typ(**result)

        return _data_sampling(**kwargs)


if __name__ == '__main__':
    dso = DataSamplingOperation(100, **example)
    for val in dso:
        print(val)
