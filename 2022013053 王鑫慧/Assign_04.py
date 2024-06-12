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

    def data_sampling(self, data_structure):
        def generate_data(data_type, datarange, len_value, subs):
            if data_type == int:
                value = random.randint(*datarange)
            elif data_type == float:
                value = random.uniform(*datarange)
            elif data_type == str:
                value = ''.join(random.choice(datarange) for _ in range(len_value))
            elif data_type == bool:
                value = random.choice([True, False])
            elif data_type == list:
                if isinstance(datarange, int):  # Check if datarange is an integer
                    value = [generate_data(subs['elem']['dataType'], subs['elem'].get('datarange'), 1,
                                           subs['elem'].get('subs', {})) for _ in range(datarange)]
                else:
                    value = [
                        generate_data(sub['dataType'], sub.get('datarange'), sub.get('len', 1), sub.get('subs', {})) for
                        sub in datarange]
            elif data_type == tuple:
                value = tuple(
                    generate_data(sub['dataType'], sub.get('datarange'), sub.get('len', 1), sub.get('subs', {})) for sub
                    in subs.values())
            else:
                raise ValueError(f"Unsupported data type: {data_type}")

            self.data_type_counts[data_type.__name__] += 1

            return (data_type.__name__, value)

        yield generate_data(data_structure['dataType'], data_structure.get('datarange'), data_structure.get('len', 1), data_structure.get('subs', {}))

    def data_processing(self):
        processed_data = []
        for _ in range(random.randint(1, 5)):
            for data in self.data_sampling(self.data_structure):
                processed_data.append(data)
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
        for _, value in data:
            nums.extend(self._extract_from_value(value))
        return nums

    def _extract_from_value(self, value):
        stack = [value]
        nums = []
        while stack:
            current = stack.pop()
            if isinstance(current, numbers.Number):
                nums.append(current)
            elif isinstance(current, (list, tuple)):
                stack.extend(current)
        return nums

# Generating data
data_process_instance = DataProcess()
processed_data = data_process_instance.processed_data
for item in processed_data:
    print("每次随机生成的数据结构有", item)

print("数据类型的数字计数（这里的数据类型有一个叠加）:", data_process_instance.data_type_counts)
print("数据平均数是（包括int和float类型）:", data_process_instance.mean_number())
print("数据总和是（包括int和float类型）:", data_process_instance.sum_numbers())
