import string
import random
from functools import wraps


class DataSampler:
    def __init__(self):
        pass

    def data_Sampling(self, **kwargs):
        result = []
        dataType = kwargs.get('dataType')
        if dataType is None:
            return "Error"

        if dataType == 'int':
            dataRange = kwargs.get('datarange')
            result.append(random.randint(*dataRange))

        elif dataType == 'float':
            dataRange = kwargs.get('datarange')
            result.append(random.uniform(*dataRange))

        elif dataType == 'str':
            dataRange = kwargs.get('datarange')
            length = kwargs.get('len', 1)
            result.append(''.join(random.choice(dataRange) for _ in range(length)))

        elif dataType == 'bool':
            result.append(random.choice([True, False]))

        elif dataType == 'list':
            subs = kwargs.get('subs')
            if isinstance(subs, dict):
                result.append([self.data_Sampling(**sub) for sub in subs.values()])
            else:
                length = subs
                result.append([random.randint(0, 100) for _ in range(length)])

        elif dataType == 'tuple':
            subs = kwargs.get('subs')
            result.append(tuple(self.data_Sampling(**sub) for sub in subs.values()))

        return result

    def generate_data(self, data_structure, count):
        for _ in range(count):
            print(self.data_Sampling(**data_structure))

# 使用封装的程序
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

def datastructure_calculator(calc_type):
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

                print(f"生成随机数: {data}")

            if calc_type == 'sum' or calc_type == 'both':
                print("所有整数和为:", all_int_sum)
                print("所有浮点数和为:", all_float_sum)

            if calc_type == 'ave' or calc_type == 'both':
                all_int_average = all_int_sum / all_int_count if all_int_count > 0 else 0
                all_float_average = all_float_sum / all_float_count if all_float_count > 0 else 0
                print("所有整数平均数为:", all_int_average)
                print("所有浮点数平均数为:", all_float_average)

            return random_datas

        return wrapper

    return decorator


@datastructure_calculator('sum')
def main(n, calc_type, **kwargs):
    sampler = DataSampler()
    random_datas = [sampler.data_Sampling(**data_structure) for _ in range(n)]
    return random_datas


if __name__ == "__main__":
    n = int(input("请输入要生成的随机数据结构的数量："))
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
    calc_type = input("请输入计算类型（sum, ave, both）,非此三者将不进行任何操作：")
    random_datas = main(n, calc_type, **data_structure)