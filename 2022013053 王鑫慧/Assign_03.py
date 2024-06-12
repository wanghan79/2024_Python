import random
import numbers
import string

# 装饰器函数，用于计数数据类型
def count_data_types(func):
    def wrapper(self, *args, **kwargs):
        # 重置计数
        self.data_type_counts = {
            'int': 0,
            'float': 0,
            'str': 0,
            'bool': 0,
            'list': 0,
            'tuple': 0
        }

        # 调用原始方法
        result = func(self, *args, **kwargs)

        # 遍历结果并计数每种数据类型
        for item in result:
            self._count_item_type(item[1])

        return result
    return wrapper

class DataProcess:
    def __init__(self):
        self.result = []
        self.data_type_counts = {}
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

    def _count_item_type(self, item):
        if isinstance(item, int):
            self.data_type_counts['int'] += 1
        elif isinstance(item, float):
            self.data_type_counts['float'] += 1
        elif isinstance(item, str):
            self.data_type_counts['str'] += 1
        elif isinstance(item, bool):
            self.data_type_counts['bool'] += 1
        elif isinstance(item, list):
            self.data_type_counts['list'] += 1
            for sub_item in item:
                self._count_item_type(sub_item)
        elif isinstance(item, tuple):
            self.data_type_counts['tuple'] += 1
            for sub_item in item:
                self._count_item_type(sub_item)

    def _generate_data(self, data_structure):
        data_type = data_structure.get('dataType')
        datarange = data_structure.get('datarange')
        len_value = data_structure.get('len', 1)
        subs = data_structure.get('subs', {})

        if data_type == int:
            value = random.randint(*datarange)
        elif data_type == float:
            value = random.uniform(*datarange)
        elif data_type == str:
            value = ''.join(random.choice(datarange) for _ in range(len_value))
        elif data_type == bool:
            value = random.choice([True, False])
        elif data_type == list:
            value = [self._generate_data(subs['elem']) for _ in range(datarange)]
        elif data_type == tuple:
            value = tuple(self._generate_data(subs[sub_key]) for sub_key in subs)
        else:
            raise ValueError(f"Unsupported data type: {data_type}")

        # 在生成数据时计数
        self._count_item_type(value)

        return value

    @count_data_types
    def data_sampling(self, **kwargs):
        self.result.clear()  # 清除之前的结果
        value = self._generate_data(kwargs)
        self.result.append((type(value).__name__, value))
        return self.result

    def mean_number(self):
        nums = self._extract_numbers(self.result)
        return sum(nums) / len(nums) if nums else 0

    def len_number(self):
        nums = self._extract_numbers(self.result)
        return len(nums)

    def sum_numbers(self):
        nums = self._extract_numbers(self.result)
        return sum(nums)

    def _extract_numbers(self, data):
        nums = []
        for item in data:
            value = item[1]
            if isinstance(value, numbers.Number) and not isinstance(value, complex):
                nums.append(value)
            elif isinstance(value, (list, tuple)):
                nums.extend(self._extract_numbers([(None, sub_value) for sub_value in value]))
        return nums

# Generating data
data_process_instance = DataProcess()
times = random.randint(1, 5)
for _ in range(times):
    print("每次随机生成的数据结构有", data_process_instance.data_sampling(**data_process_instance.data_structure))
print("数据平均数是（包括int和float类型）:", data_process_instance.mean_number())
print("数据总和是（包括int和float类型）", data_process_instance.sum_numbers())
print("数据类型的数字计数:", data_process_instance.data_type_counts)
