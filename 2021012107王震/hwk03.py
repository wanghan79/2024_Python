import random
import string
import statistics


def flatten_and_filter(data):
    for item in data:
        if isinstance(item, (int, float)):
            yield item
        elif isinstance(item, (list, tuple)):
            yield from flatten_and_filter(item)


def data_sampling(specs):
    result = []
    for key, spec in specs.items():
        if key in ['int', 'float']:
            if key == 'int':
                result.append(random.randint(*spec['datarange']))
            elif key == 'float':
                result.append(random.uniform(*spec['datarange']))
        elif key == 'str':
            chars = spec['datarange']
            length = spec.get('len', 1)
            result.append(''.join(random.choice(chars) for _ in range(length)))
        elif key == 'tuple':
            tuple_elements = [data_sampling({k: v}) for k, v in spec.items() if k != 'datarange']
            result.append(tuple_elements)
        elif key == 'list':
            list_elements = [data_sampling({k: v}) for k, v in spec.items() if k != 'datarange']
            result.append([element for sublist in list_elements for element in sublist])
    return result


def data_screening(num, **specs):
    screened_data = []
    for _ in range(num):
        sampled_data = data_sampling(specs)
        flattened_data = list(flatten_and_filter(sampled_data))
        print("生成数据为:", sampled_data)
        screened_data.append(flattened_data)
    return screened_data


def data_figuring(data_sets):
    all_data = []
    for data_set in data_sets:
        all_data.extend(data_set)
    print("可参与运算的数据为:", all_data)

    while True:
        print("\n请选择要处理的数据类型: 整数类型（int）, 浮点数类型（float）, 或两者一起处理（both)。")
        data_type = input("请输入 'int', 'float', 'both', 或输入 'e' 直接退出: ").strip().lower()
        if data_type == 'e':
            print("已成功退出！")
            break

        int_data = [item for item in all_data if isinstance(item, int)]
        float_data = [item for item in all_data if isinstance(item, float)]
        selected_data = int_data if data_type == 'int' else \
            float_data if data_type == 'float' else \
                (int_data + float_data if data_type == 'both' else None)

        if selected_data is None:
            print("无效, 请重新选择。")
            continue
        print("\n请选择要进行的运算: 求和（sum), 求均值（ave）, 求方差（var）。")
        operation = input("请输入 'sum', 'ave', 'var', 或输入 'e' 直接退出: ").strip().lower()
        if operation == 'e':
            print("已成功退出！")
            break

        if operation not in ['sum', 'ave', 'var']:
            print("无效, 请重新选择。")
            continue

        result = sum(selected_data) if operation == 'sum' else \
            statistics.mean(selected_data) if selected_data else 0 if operation == 'ave' else \
                statistics.variance(selected_data) if len(selected_data) > 1 else 0

        print(f"所选数据的 {operation} 为: {result}")


# 使用示例
struct = {
    'int': {'datarange': [1, 10]},
    'float': {'datarange': [1.0, 10.0]},
    'tuple': {
        'int': {'datarange': [1, 50]},
        'str': {'datarange': string.ascii_uppercase, 'len': 5}
    },
    'list': {
        'int': {'datarange': [1, 30]},
        'str': {'datarange': string.ascii_lowercase, 'len': 8},
        'float': {'datarange': [1.0, 10.0]}
    }
}

data_sets = data_screening(3, **struct)
data_figuring(data_sets)
