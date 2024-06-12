import string
import random
from functools import wraps

class DataSamplerWrapper:
    def __init__(self):
        pass

    def sample_data(self, **kwargs):
        result = []
        data_type = kwargs.get('dataType')
        if data_type is None:
            return "Error"

        if data_type == 'int':
            data_range = kwargs.get('datarange')
            result.append(random.randint(*data_range))

        elif data_type == 'float':
            data_range = kwargs.get('datarange')
            result.append(random.uniform(*data_range))

        elif data_type == 'str':
            data_range = kwargs.get('datarange')
            length = kwargs.get('len', 1)
            result.append(''.join(random.choice(data_range) for _ in range(length)))

        elif data_type == 'bool':
            result.append(random.choice([True, False]))

        elif data_type == 'list':
            subs = kwargs.get('subs')
            if isinstance(subs, dict):
                result.append([self.sample_data(**sub) for sub in subs.values()])
            else:
                length = subs
                result.append([random.randint(0, 100) for _ in range(length)])

        elif data_type == 'tuple':
            subs = kwargs.get('subs')
            result.append(tuple(self.sample_data(**sub) for sub in subs.values()))

        return result

    def generate_data(self, data_structure, count):
        for _ in range(count):
            print(self.sample_data(**data_structure))

def collect_numbers(data, int_sum=0, int_count=0, float_sum=0, float_count=0):
    if isinstance(data, int):
        int_sum += data
        int_count += 1
    elif isinstance(data, float):
        float_sum += data
        float_count += 1
    elif isinstance(data, (list, tuple)):
        for item in data:
            int_sum, int_count, float_sum, float_count = collect_numbers(item, int_sum, int_count, float_sum,
                                                                         float_count)
    return int_sum, int_count, float_sum, float_count

def data_calculator_wrapper(calc_type):
    def decorator(func):
        @wraps(func)
        def wrapper(n, calc_type, **kwargs):
            all_int_sum = 0
            all_int_count = 0
            all_float_sum = 0.0
            all_float_count = 0

            random_datas = func(n, calc_type, **kwargs)

            for data in random_datas:
                int_sum, int_count, float_sum, float_count = collect_numbers(data)

                all_int_sum += int_sum
                all_int_count += int_count
                all_float_sum += float_sum
                all_float_count += float_count

                print(f"Generated data: {data}")

            if calc_type == 'sum' or calc_type == 'both':
                print("Sum of all integers:", all_int_sum)
                print("Sum of all floats:", all_float_sum)

            if calc_type == 'ave' or calc_type == 'both':
                all_int_average = all_int_sum / all_int_count if all_int_count > 0 else 0
                all_float_average = all_float_sum / all_float_count if all_float_count > 0 else 0
                print("Average of all integers:", all_int_average)
                print("Average of all floats:", all_float_average)

            return random_datas

        return wrapper

    return decorator

@data_calculator_wrapper('sum')
def main(n, calc_type, **kwargs):
    sampler = DataSamplerWrapper()
    random_datas = [sampler.sample_data(**data_structure) for _ in range(n)]
    return random_datas

if __name__ == "__main__":
    n = int(input("Enter the number of random data structures to generate: "))
    data_structure = {
        "dataType": "tuple",
        "subs": {
            "sub1": {
                "dataType": "list",
                "subs": {
                    "sub1": {
                        "dataType": "int",
                        "datarange": (0, 100)
                    },
                    "sub2": {
                        "dataType": "str",
                        "datarange": string.ascii_letters,
                        "len": 5
                    }
                }
            },
            "sub2": {
                "dataType": "tuple",
                "subs": {
                    "sub1": {
                        "dataType": "float",
                        "datarange": (0, 5000)
                    },
                    "sub2": {
                        "dataType": "int",
                        "datarange": (1, 200)
                    }
                }
            },
            "sub3": {
                "dataType": "str",
                "datarange": string.ascii_letters,
                "len": 3,
            }
        }
    }
    calc_type = input("Enter the calculation type (sum, ave, both), no action will be performed if not one of these three: ")
    random_datas = main(n, calc_type, **data_structure)
