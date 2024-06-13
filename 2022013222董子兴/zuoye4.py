import random
import string

# 定义数据结构
data_structure = {
    'type': 'tuple',
    'contents': {
        'part1': {
            'type': 'set',
            'contents': {
                'section1': {
                    'type': 'int',
                    'limits': (0, 100)
                },
                'section2': {
                    'type': 'str',
                    'limits': (0, 10)  # 字符串长度
                }
            }
        },
        'part2': {
            'type': 'list',
            'contents': {
                'section1': {
                    'type': 'float',
                    'limits': (0.0, 5000.0)
                },
                'section2': {
                    'type': 'int',
                    'limits': (1, 200)
                }
            }
        },
        'part3': {
            'type': 'str',
            'limits': (0, 5)  # 字符串长度
        }
    }
}

def create_data(**config):
    if config['type'] == 'tuple':
        return tuple(create_data(**item) for item in config['contents'].values())
    elif config['type'] == 'list':
        return [create_data(**item) for item in config['contents'].values()]
    elif config['type'] == 'set':
        return set(create_data(**item) for item in config['contents'].values())
    elif config['type'] == 'int':
        return random.randint(*config['limits'])
    elif config['type'] == 'float':
        return random.uniform(*config['limits'])
    elif config['type'] == 'str':
        return ''.join(random.choices(string.ascii_uppercase, k=config['limits'][1]))

def create_data_series(structure, num):
    for _ in range(num):
        yield create_data(**structure)

def perform_operations(data, choice):
    if choice == "sum":
        result = calculate_sum(data)
        print("总和:", result)
    elif choice == "average":
        result = calculate_average(data)
        print("均值:", result)
    elif choice == "both":
        sum_result = calculate_sum(data)
        average_result = calculate_average(data)
        print("总和:", sum_result, "均值:", average_result)
    elif choice == "no":
        print("未进行任何操作")
    else:
        print("选择的操作无效")

def calculate_sum(data):
    if isinstance(data, (int, float)):
        return data
    elif isinstance(data, (list, tuple, set)):
        return sum(calculate_sum(item) for item in data)
    return 0

def calculate_average(data):
    total = calculate_sum(data)
    count = calculate_count(data)
    return total / count if count > 0 else 0

def calculate_count(data):
    if isinstance(data, (int, float)):
        return 1
    elif isinstance(data, (list, tuple, set)):
        return sum(calculate_count(item) for item in data)
    return 0

if __name__ == '__main__':
    num_data = int(input("请输入要生成数据的数量:"))
    operation_type = input("请输入要执行的操作（sum, average, both, no）:")
    for sample in create_data_series(data_structure, num_data):
        print(sample)
        perform_operations(sample, operation_type)
