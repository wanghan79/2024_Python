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


def data_sampling(**kwargs):
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
            result.append(data_sampling(**v))
        return tuple(result)
    elif typ == set:
        result = set()
        for k, v in inner.items():
            result.add(data_sampling(**v))
        return result
    elif typ == list:
        result = list()
        for k, v in inner.items():
            result.append(data_sampling(**v))
        return result
    else:
        result = dict()
        for k, v in inner.items():
            result[k] = data_sampling(**v)
        return typ(**result)


if __name__ == '__main__':
    print(data_sampling(**example))
