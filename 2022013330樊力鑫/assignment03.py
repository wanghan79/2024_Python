import random
import warnings
import numbers
import string
from functools import wraps


def validate_input(func):
    @wraps(func)
    def wrapper(self, **kwargs):
        dataType = kwargs.get('dataType')
        if dataType not in [int, float, str, bool, list, tuple]:
            raise ValueError("Unsupported data type")
        if dataType == int or dataType == float:
            daterange = kwargs.get('datarange')
            if not isinstance(daterange, tuple) or len(daterange) != 2:
                raise ValueError("datarange should be a tuple of two numbers")
        elif dataType == str:
            datarange = kwargs.get('datarange')
            length = kwargs.get('len')
            if not isinstance(datarange, str):
                raise ValueError("datarange should be a string")
            if not isinstance(length, int) or length <= 0:
                raise ValueError("len should be a positive integer")
        return func(self, **kwargs)
    return wrapper


def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__} executed with result: {result}")
        return result
    return wrapper


class data_process():
    def __init__(self):
        self.result = []
        self.data_structure = {
            "dataType": tuple,
            "subs": {
                "sub1": {
                    "dataType": str,
                    "datarange": string.ascii_letters,
                    "len": 5
                },
                "sub2": {
                    "dataType": tuple,
                    "subs": {
                        "sub1": {
                            "dataType": int,
                            "datarange": (0, 100),
                        },
                        "sub2": {
                            "dataType": list,
                            "datarange": 5,
                        },
                    },
                },
            },
        }

    @log_execution
    @validate_input
    def data_sampling(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'dataType':
                dataType = value
                if dataType == int:
                    daterange = kwargs['datarange']
                    self.result.append(random.randint(daterange[0], daterange[1]))

                elif dataType == float:
                    daterange = kwargs['datarange']
                    self.result.append(random.uniform(daterange[0], daterange[1]))

                elif dataType == str:
                    datarange = kwargs['datarange']
                    self.result.append(''.join(random.choice(datarange) for _ in range(kwargs['len'])))

                elif dataType == bool:
                    self.result.append(random.choice([True, False]))

                elif dataType == list:
                    datarange = kwargs['datarange']
                    self.result.append([random.randint(0, 100) for _ in range(datarange)])

                elif dataType == tuple:
                    subs = kwargs['subs']
                    self.result.append(tuple(self.data_sampling(**sub) for sub in subs.values()))

        return self.result

    @log_execution
    def mean_number(self):
        nums = [x for x in self.result if isinstance(x, numbers.Number) and not isinstance(x, complex)]
        if len(nums) == 0:
            return 0
        else:
            return sum(nums) / len(nums)

    @log_execution
    def len_number(self):
        nums = [x for x in self.result if isinstance(x, numbers.Number) and not isinstance(x, complex)]
        return len(nums)


times = int(input("times you want to sample:"))
data_process_instance = data_process()
for i in range(times):
    print(data_process_instance.data_sampling(**data_process_instance.data_structure))
    print("mean number of generated data:", data_process_instance.mean_number())
    print("nums of generated data:", data_process_instance.len_number())
