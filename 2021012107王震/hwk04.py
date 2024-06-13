import random
import string
import statistics


def flatten_and_filter(data):
    for item in data:
        if isinstance(item, (int, float)):
            yield item
        elif isinstance(item, (list, tuple)):
            yield from flatten_and_filter(item)


def _sample_element(key, specs):
    if key == 'int':
        return random.randint(*specs['datarange'])
    elif key == 'float':
        return random.uniform(*specs['datarange'])
    elif key == 'str':
        chars = specs['datarange']
        length = specs.get('len', 0)
        return ''.join(random.choice(chars) for _ in range(length))
    elif key == 'tuple':
        return tuple(_sample_element(k, v) for k, v in specs.items())
    elif key == 'list':
        return [_sample_element('int', specs['int']), _sample_element('str', specs['str']),
                _sample_element('float', specs['float'])]


def data_sampling(specs):
    return [_sample_element(key, specs[key]) for key in specs]


def data_screening(num, specs):
    for _ in range(num):
        sampled_data = data_sampling(specs)
        flattened_data = list(flatten_and_filter(sampled_data))
        print("生成数据为:", sampled_data)
        yield flattened_data


def data_figuring(data_sets):
    flattened_data = [item for sublist in data_sets for item in sublist]
    print("可参与运算的数据为:", flattened_data)

    while True:
        print("\n请选择要处理的数据类型: 整数类型（int）, 浮点数类型（float）, 或两者一起处理（both)。")
        data_type = input("请输入 'int', 'float', 'both' 参与运算, 或输入 'e' 直接退出: ").strip().lower()
        if data_type == 'e':
            print("已成功退出！")
            break

        int_data = [item for item in flattened_data if isinstance(item, int)]
        float_data = [item for item in flattened_data if isinstance(item, float)]

        if data_type == 'int':
            selected_data = int_data
        elif data_type == 'float':
            selected_data = float_data
        elif data_type == 'both':
            selected_data = int_data + float_data
        else:
            print("无效, 请重新选择。")
            continue
        print("\n请选择要进行的运算: 求和（sum), 求均值（ave）, 求方差（var）。")
        operation = input("请输入运算 'sum', 'ave', 'var', 或输入 'e' 直接退出: ").strip().lower()
        if operation == 'e':
            print("已成功退出！")
            break

        if operation == 'sum':
            result = sum(selected_data)
        elif operation == 'ave':
            result = statistics.mean(selected_data) if selected_data else 0
        elif operation == 'var':
            result = statistics.variance(selected_data) if len(selected_data) > 1 else 0
        else:
            print("无效, 请重新选择。")
            continue

        print(f"所选数据的 {operation} 为: {result}")


# 使用示例
if __name__ == "__main__":
    struct = {
        'int': {'datarange': [1, 10]},
        'float': {'datarange': [1.0, 10.0]},
        'tuple': {
            'int': {'datarange': [1, 20]},
            'str': {'datarange': string.ascii_uppercase, 'len': 5}
        },
        'list': {
            'int': {'datarange': [1, 50]},
            'str': {'datarange': string.ascii_lowercase, 'len': 8},
            'float': {'datarange': [1.0, 10.0]}
        }
    }

    data_sets = list(data_screening(2, struct))
    data_figuring(data_sets)


