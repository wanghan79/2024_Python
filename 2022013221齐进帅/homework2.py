import random
import string


class Class:
    def __init__(self, name, number, ID):
        self.name = name
        self.number = number
        self.ID = ID

    def __repr__(self):
        return f'Class name:{self.name} age:{self.number} ID:{self.ID}'

example = {
    "data_type": tuple,
    "subs": {
        "sub1": {"data_type": list,
                 "subs": {
                     "sub1": {
                         "data_type": int,
                         "data_range": (0, 1000)
                     },
                     "sub2": {
                         "data_type": str,
                         "data_range": string.ascii_uppercase,
                         "len": 10
                     }
                 },
                 },
        "sub2": {"data_type": tuple,
                 "subs": {
                     "sub1": {
                         "data_type": int,
                         "data_range": (0, 1000)
                     },
                     "sub2": {
                         "data_type": str,
                         "data_range": string.ascii_uppercase,
                         "len": 10
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
                "subs": {
                    "data_type": Class,
                    "subs": {
                        "name": {
                            "data_type": str,
                            "data_range": "2024计算机",
                            "len": 10
                        },
                        "number": {
                            "data_type": int,
                            "data_range": (0, 100)
                        },
                        "ID": {
                            "data_type": int,
                            "data_range": (0, 100)
                        }
                    }
                }
            }
        }
    }
}

class DataSampler:
    def __init__(self):
        self.int_sum = 0
        self.float_sum = 0
        self.count_int = 0
        self.count_float = 0

    def sample_int(self, data_range):
        if len(data_range) == 1:
            return data_range[0]
        else:
            return random.choice(data_range) if len(data_range) > 2 else random.randint(*data_range)

    def sample_bool(self, data_range):
        return data_range[0] if len(data_range) == 1 else random.random() < 0.5

    def sample_float(self, data_range):
        if len(data_range) == 1:
            return data_range[0]
        else:
            return random.uniform(*data_range) if len(data_range) == 2 else random.choice(data_range)

    def sample_str(self, data_range, length):
        return ''.join(random.choice(data_range) for _ in range(length)) if isinstance(data_range, str) else random.choice(data_range)

    def sample_col(self, col_type, items):
        return col_type(self.data_sampling(**v) for v in items.values())

    def data_sampling(self, **kwargs):
        typ = kwargs.get('data_type')
        data_range = kwargs.get('data_range')
        subs = kwargs.get('subs')
        length = kwargs.get('len')

        if typ is int:
            result = self.sample_int(data_range)
            self.int_sum += result
            self.count_int += 1
            return result
        elif typ is bool:
            return self.sample_bool(data_range)
        elif typ is float:
            result = self.sample_float(data_range)
            self.float_sum += result
            self.count_float += 1
            return result
        elif typ is str:
            return self.sample_str(data_range, length)
        elif typ is tuple:
            return self.sample_col(tuple, subs)
        elif typ is set:
            return self.sample_col(set, subs)
        elif typ is list:
            return self.sample_col(list, subs)
        else:
            return typ(**{k: self.data_sampling(**v) for k, v in subs.items()})

    def cal_avg(self):
        int_avg = self.int_sum / self.count_int if self.count_int > 0 else 0
        float_avg = self.float_sum / self.count_float if self.count_float > 0 else 0
        return {'int_avg': int_avg, 'float_avg': float_avg}


if __name__ == '__main__':
    sampler = DataSampler()
    result = sampler.data_sampling(**example)
    print(result)
    averages = sampler.cal_avg()
    print(averages)