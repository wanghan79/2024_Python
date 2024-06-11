import random
import string
from functools import wraps


def generate_structure(**kwargs):
    if 'datatype' not in kwargs:
        raise ValueError("数据结构定义中缺少'datatype'字段")

    datatype = kwargs['datatype']
    subs = kwargs.get('subs', None)

    if datatype == 'int':
        return random.randint(*kwargs.get('datarange', (0, 100)))
    elif datatype == 'float':
        return round(random.uniform(*kwargs.get('datarange', (0, 1.0))), 2)
    elif datatype == 'str':
        length = random.randint(*kwargs.get('datarange', (1, 10)))
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    elif datatype == 'list':
        return [generate_structure(**sub) for sub in subs.values()]
    elif datatype == 'tuple':
        return tuple(generate_structure(**sub) for sub in subs.values())
    else:
        raise ValueError(f"不支持的数据类型: {datatype}")


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

            if calc_type == 'average' or calc_type == 'both':
                all_int_average = all_int_sum / all_int_count if all_int_count > 0 else 0
                all_float_average = all_float_sum / all_float_count if all_float_count > 0 else 0
                print("所有整数平均数为:", all_int_average)
                print("所有浮点数平均数为:", all_float_average)

            return random_datas

        return wrapper

    return decorator


@datastructure_calculator('')
def main(n, calc_type, **kwargs):
    random_datas = [generate_structure(**kwargs) for _ in range(n)]
    return random_datas


if __name__ == "__main__":
    n = int(input("请输入要生成的随机数据结构的数量："))
    data_structure = {
        'datatype': 'tuple',
        'subs': {
            'sub1': {
                'datatype': 'list',
                'subs': {
                    'sub1': {
                        'datatype': 'int',
                        'datarange': (0, 100)
                    },
                    'sub2': {
                        'datatype': 'str',
                        'datarange': (1, 10)
                    }
                }
            },
            'sub2': {
                'datatype': 'tuple',
                'subs': {
                    'sub1': {
                        'datatype': 'float',
                        'datarange': (0, 5000)
                    },
                    'sub2': {
                        'datatype': 'int',
                        'datarange': (1, 200)
                    }
                }
            },
            'sub3': {
                'datatype': 'str',
                'datarange': (1, 5)
            }
        }
    }
    calc_type = input("请输入计算类型（sum, average, both, no）：")
    random_datas = main(n, calc_type, **data_structure)