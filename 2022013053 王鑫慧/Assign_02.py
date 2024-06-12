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
                            "subs": {
                                "elem": {
                                    "dataType": float,
                                    "datarange": (0.0, 100.0)
                                }
                            }
                        },
                        "sub3": {
                            "dataType": float,
                            "datarange": (0.0, 10.0),
                        },

                    }
                }
            }
        }

    def data_sampling(self, data_type, **kwargs):
        for key, value in kwargs.items():
            if key == 'dataType':
                dataType = value
                if dataType == int:
                    daterange = kwargs['datarange']
                    value = random.randint(daterange[0], daterange[1])
                    self.result.append((dataType.__name__, value))

                elif dataType == float:
                    daterange = kwargs['datarange']
                    value = random.uniform(daterange[0], daterange[1])
                    self.result.append((dataType.__name__, value))

                elif dataType == str:
                    datarange = kwargs['datarange']
                    value = ''.join(random.choice(datarange) for _ in range(kwargs['len']))
                    self.result.append((dataType.__name__, value))

                elif dataType == bool:
                    value = random.choice([True, False])
                    self.result.append((dataType.__name__, value))

                elif dataType == list:
                    datarange = kwargs['datarange']
                    value = [random.randint(0, 100) for _ in range(datarange)]
                    self.result.append((dataType.__name__, value))

                elif dataType == tuple:
                    subs = kwargs['subs']
                    sub_result = tuple(self.data_sampling(sub_data_type, **sub_kwargs) for sub_data_type, sub_kwargs in subs.items())
                    self.result.append((dataType.__name__, sub_result))

        return self.result

    def mean_number(self):
        nums = [x[1] for x in self.result if isinstance(x[1], numbers.Number) and not isinstance(x[1], complex)]
        if len(nums) == 0:
            return 0
        else:
            return sum(nums) / len(nums)

    def len_number(self):
        nums = [x[1] for x in self.result if isinstance(x[1], numbers.Number) and not isinstance(x[1], complex)]
        return len(nums)

    def sum_numbers(self):
        total_sum = 0
        for item_type, item_value in self.result:
            if item_type in ['int', 'float']:
                total_sum += item_value
        return total_sum

# Generating data
data_process_instance = data_process()

times = random.randint(1, 5)
for _ in range(times):
    print("生成的随机数据结构：",data_process_instance.data_sampling(None, **data_process_instance.data_structure))
print("数据平均数是（包括int和float类型）:", data_process_instance.mean_number())
print("数据和是（包括int和float类型）", data_process_instance.sum_numbers())
