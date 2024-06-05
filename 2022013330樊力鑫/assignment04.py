import random
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
                    yield random.randint(daterange[0], daterange[1])

                elif dataType == float:
                    daterange = kwargs['datarange']
                    yield random.uniform(daterange[0], daterange[1])

                elif dataType == str:
                    datarange = kwargs['datarange']
                    yield ''.join(random.choice(datarange) for _ in range(kwargs['len']))

                elif dataType == bool:
                    yield random.choice([True, False])

                elif dataType == list:
                    datarange = kwargs['datarange']
                    yield [random.randint(0, 100) for _ in range(datarange)]

                elif dataType == tuple:
                    subs = kwargs['subs']
                    yield tuple(next(self.data_sampling(**sub)) for sub in subs.values())

    def generate_data(self):
        data = next(self.data_sampling(**self.data_structure))
        self.result.append(data)
        return data

    def _extract_numbers(self, data):
        if isinstance(data, numbers.Number) and not isinstance(data, complex):
            return [data]
        elif isinstance(data, (list, tuple)):
            nums = []
            for item in data:
                nums.extend(self._extract_numbers(item))
            return nums
        return []

    def mean_number(self):
        nums = []
        for item in self.result:
            nums.extend(self._extract_numbers(item))
        if len(nums) == 0:
            return 0
        else:
            return sum(nums) / len(nums)

    def len_number(self):
        nums = []
        for item in self.result:
            nums.extend(self._extract_numbers(item))
        return len(nums)


times = int(input("times you want to sample:"))
data_process_instance = data_process()
for i in range(times):
    print(data_process_instance.generate_data())
    print("mean number of generated data:", data_process_instance.mean_number())
    print("nums of generated data:", data_process_instance.len_number())
