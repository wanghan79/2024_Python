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

def data_sampling(**kwargs):
    def sample_int(data_range):
        if len(data_range) == 1:
            return data_range[0]
        else:
            return random.choice(data_range) if len(data_range) > 2 else random.randint(*data_range)

    def sample_bool(data_range):
        return data_range[0] if len(data_range) == 1 else random.random() < 0.5

    def sample_float(data_range):
        if len(data_range) == 1:
            return data_range[0]
        else:
            return random.uniform(*data_range) if len(data_range) == 2 else random.choice(data_range)

    def sample_str(data_range, length):
        return ''.join(random.choice(data_range) for _ in range(length)) if isinstance(data_range, str) else random.choice(data_range)

    def sample_col(col_type, items):
        return col_type(data_sampling(**v) for v in items.values())

    typ = kwargs.get('data_type')
    data_range = kwargs.get('data_range')
    subs = kwargs.get('subs')
    length = kwargs.get('len')

    if typ is int:
        return sample_int(data_range)
    elif typ is bool:
        return sample_bool(data_range)
    elif typ is float:
        return sample_float(data_range)
    elif typ is str:
        return sample_str(data_range, length)
    elif typ is tuple:
        return sample_col(tuple, subs)
    elif typ is set:
        return sample_col(set, subs)
    elif typ is list:
        return sample_col(list, subs)
    else:
        return typ(**{k: data_sampling(**v) for k, v in subs.items()})


if __name__ == '__main__':
    print(data_sampling(**example))