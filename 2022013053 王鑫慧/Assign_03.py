
import random
import numbers
import string

class DataProcess:
    def __init__(self):
        self.data_type_counts = {
            'int': 0,
            'float': 0,
            'str': 0,
            'bool': 0,
            'list': 0,
            'tuple': 0
        }
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
        self.processed_data = self.data_processing()  # Cache processed data

    def data_sampling(self, **kwargs):
        data_type = kwargs.get('dataType', int)
        datarange = kwargs.get('datarange')
        len_value = kwargs.get('len', 1)
        subs = kwargs.get('subs', {})

        if data_type == int:
            value = random.randint(*datarange)
        elif data_type == float:
            value = random.uniform(*datarange)
        elif data_type == str:
            value = ''.join(random.choice(datarange) for _ in range(len_value))
        elif data_type == bool:
            value = random.choice([True, False])
        elif data_type == list:
            value = [self.data_sampling(**subs['elem'])[1] for _ in range(datarange)]
        elif data_type == tuple:
            value = tuple(self.data_sampling(**sub_kwargs)[1] for sub_kwargs in subs.values())
        else:
            raise ValueError(f"Unsupported data type: {data_type}")

        self.data_type_counts[data_type.__name__] += 1

        return (data_type.__name__, value)

    def data_processing(self):
        processed_data = []
        for _ in range(random.randint(1, 5)):
            result = self.data_sampling(**self.data_structure)
            processed_data.append(result)
        return processed_data

    def mean_number(self):
        nums = self._extract_numbers(self.processed_data)
        return sum(nums) / len(nums) if nums else 0

    def len_number(self):
        nums = self._extract_numbers(self.processed_data)
        return len(nums)

    def sum_numbers(self):
        nums = self._extract_numbers(self.processed_data)
        return sum(nums)

    def _extract_numbers(self, data):
        nums = []
        for item in data:
            _, value = item
            nums.extend(self._extract_from_value(value))
        return nums

    def _extract_from_value(self, value):
        if isinstance(value, numbers.Number):
            return [value]
        elif isinstance(value, (list, tuple)):
            nums = []
            for elem in value:
                nums.extend(self._extract_from_value(elem))
            return nums
        return []

# Generating data
data_process_instance = DataProcess()
processed_data = data_process_instance.processed_data
for item in processed_data:
    print("每次随机生成的数据结构有", item)

print("数据类型的数字计数（这里的数据类型有一个叠加）:", data_process_instance.data_type_counts)
print("数据平均数是（包括int和float类型）:", data_process_instance.mean_number())
print("数据总和是（包括int和float类型）:", data_process_instance.sum_numbers())
