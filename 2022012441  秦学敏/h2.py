import random
import string


def extract_strings(data):
    strings = []
    if isinstance(data, str):
        strings.append(data)
    elif isinstance(data, (list, tuple, set)):
        for item in data:
            strings.extend(extract_strings(item))
    elif isinstance(data, dict):
        for item in data.values():
            strings.extend(extract_strings(item))
    return strings


def extract_integers(data):
    integers = []
    if isinstance(data, int):
        integers.append(data)
    elif isinstance(data, (list, tuple, set)):
        for item in data:
            integers.extend(extract_integers(item))
    elif isinstance(data, dict):
        for item in data.values():
            integers.extend(extract_integers(item))
    return integers


def transform_strings(strings, transformation):
    if transformation == 'uppercase':
        return [s.upper() for s in strings]
    elif transformation == 'lowercase':
        return [s.lower() for s in strings]
    else:
        raise ValueError(f"Invalid transformation. Please choose either 'uppercase' or 'lowercase'.")


def generate_data_sample(data_structure):
    sample = {}
    for key, value in data_structure.items():
        if key == 'int':
            sample[key] = random.randint(value['datarange'][0], value['datarange'][1])
        elif key == 'str':
            # 使用 string.ascii_lowercase 或者其他合适的字符串集合
            sample[key] = ''.join(random.choices(string.ascii_lowercase, k=value['len']))
        elif key in ('tuple', 'list', 'set', 'dict'):
            sample[key] = generate_data_sample(value)
    return sample


def generate_random_data(data_specs):
    return [generate_data_sample(data_specs['structure']) for _ in range(data_specs['num'])]


def calculate_data(operation, integers):
    if operation == 'sum':
        return sum(integers)
    elif operation == 'average':
        return sum(integers) / len(integers) if integers else 0
    else:
        raise ValueError(f"Invalid operation. Please choose either 'sum' or 'average'.")


if __name__ == '__main__':
    data_specs = {
        'num': 5,
        'structure': {
            'dict': {
                'str_key': {'str': {'datarange': string.ascii_lowercase, 'len': 5}},
                'list_of_strs': {
                    'list': {
                        'str': {'datarange': string.ascii_lowercase, 'len': 10}
                    }
                },
                'int': {'datarange': [1, 100]}
            }
        }
    }

    # 生成随机数
    random_data = generate_random_data(data_specs)

    # 提取整数（但在这个特定的 data_specs 中，我们并没有直接生成整数列表）
    integers = extract_integers(random_data)
    print(random_data)

    # 计算整数的和（如果 integers 列表中有数据）
    if integers:
        sum_result = calculate_data('sum', integers)
        print("Sum:", sum_result)

        # 计算整数的平均值（如果 integers 列表中有数据）
    if integers:
        average_result = calculate