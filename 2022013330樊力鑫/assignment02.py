import random
import warnings
import numbers
import string


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

    def mean_number(self):
        nums = [x for x in self.result if isinstance(x, numbers.Number) and not isinstance(x, complex)]
        if len(nums) == 0:
            return 0
        else:
            return sum(nums) / len(nums)

    def len_number(self):
        nums = nums = [x for x in self.result if isinstance(x, numbers.Number) and not isinstance(x, complex)]
        return len(nums)


times = int(input("times you want to sample:"))
data_process = data_process()
for i in range(times):
    print(data_process.data_sampling(**data_process.data_structure))
print("mean number of generated data:", data_process.mean_number())
print("nums of generated data:", data_process.len_number())