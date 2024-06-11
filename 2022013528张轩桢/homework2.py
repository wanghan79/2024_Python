import random
import string


def generate_structure(**kwargs):
    if 'datatype' not in kwargs:
        raise ValueError("数据结构定义中缺少'datatype'字段")

    datatype = kwargs['datatype']
    subs = kwargs.get('subs', None)

    if datatype == 'int':
        return random.randint(*kwargs['datarange'])
    elif datatype == 'float':
        return round(random.uniform(*kwargs['datarange']), 2)
    elif datatype == 'str':
        length = random.randint(*kwargs['datarange'])
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    elif datatype == 'list':
        return [generate_structure(**sub) for sub in subs.values()]
    elif datatype == 'tuple':
        return tuple(generate_structure(**sub) for sub in subs.values())
    else:
        raise ValueError(f"不支持的数据类型: {datatype}")


def collect_numbers(data, **kwargs):
    int_sum = kwargs.get('int_sum', 0)
    int_count = kwargs.get('int_count', 0)
    float_sum = kwargs.get('float_sum', 0)
    float_count = kwargs.get('float_count', 0)

    if isinstance(data, int):
        int_sum += data
        int_count += 1
    elif isinstance(data, float):
        float_sum += data
        float_count += 1
    elif isinstance(data, (list, tuple)):
        for item in data:
            int_sum, int_count, float_sum, float_count = collect_numbers(item, int_sum=int_sum, int_count=int_count,
                                                                         float_sum=float_sum, float_count=float_count)
    return int_sum, int_count, float_sum, float_count


def main():
    n = int(input("请输入要生成的随机数据结构的数量："))
    all_int_sum = 0
    all_int_count = 0
    all_float_sum = 0
    all_float_count = 0

    for i in range(n):
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
        random_data = generate_structure(**data_structure)

        all_int_sum, all_int_count, all_float_sum, all_float_count = collect_numbers(random_data, int_sum=all_int_sum,
                                                                                     int_count=all_int_count,
                                                                                     float_sum=all_float_sum,
                                                                                     float_count=all_float_count)

        print(f"随机数据结构{i + 1}:", random_data)

    all_int_average = all_int_sum / all_int_count if all_int_count > 0 else 0
    all_float_average = all_float_sum / all_float_count if all_float_count > 0 else 0

    print("所有整数和为:", all_int_sum)
    print("所有浮点数和为:", all_float_sum)
    print("所有整数平均数为:", all_int_average)
    print("所有浮点数平均数为:", all_float_average)


if __name__ == "__main__":
    main()
