import random
import string
import time


def calculate_execution_time(func):
    """
    装饰器，用于计算函数执行时间。
    
    :param func: 被装饰的函数
    :return: 包含执行时间的函数结果
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = list(func(*args, **kwargs))
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return result
    return wrapper


def generate_random_data(data_structure):
    """
    根据定义的数据结构生成随机数据。
    通过yield逐步输出生成的数据。
    
    :param data_structure: 预定义的数据结构，包含整数、浮点数和字符串
    :return: 填充了随机数据的结构
    """
    if isinstance(data_structure, int):
        # 生成随机整数
        yield random.randint(0, 100)
    elif isinstance(data_structure, float):
        # 生成随机浮点数
        yield round(random.uniform(0.0, 100.0), 2)
    elif isinstance(data_structure, str):
        # 生成随机字符串
        length = random.randint(5, 15)  # 随机长度在5到15之间
        yield ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    elif isinstance(data_structure, list):
        # 递归生成列表中的每个元素
        generated_list = []
        for _ in range(random.randint(1, 10)):
            element_generator = generate_random_data(data_structure[0])
            element = next(element_generator)
            generated_list.append(element)
        yield generated_list
    elif isinstance(data_structure, dict):
        # 递归生成字典中的每个值
        generated_dict = {}
        for key, value in data_structure.items():
            value_generator = generate_random_data(value)
            generated_dict[key] = next(value_generator)
        yield generated_dict
    else:
        raise ValueError("Unsupported data structure")


@calculate_execution_time
def analyze_data(data, operation='sum'):
    """
    对生成的数据进行统计分析。
    通过yield逐步输出统计结果。
    
    :param data: 包含随机数据的复杂嵌套结构
    :param operation: 操作类型，'sum'表示求和，'average'表示求平均数
    :return: 整数之和、浮点数之和或整数的平均值
    """
    int_sum = 0
    float_sum = 0.0
    int_count = 0

    def recursive_analyze(data):
        nonlocal int_sum, float_sum, int_count
        
        if isinstance(data, int):
            int_sum += data
            int_count += 1
            yield {'type': 'int', 'value': data}
        elif isinstance(data, float):
            float_sum += data
            yield {'type': 'float', 'value': data}
        elif isinstance(data, (list, tuple)):
            for item in data:
                yield from recursive_analyze(item)
        elif isinstance(data, dict):
            for key, value in data.items():
                yield from recursive_analyze(value)

    for result in recursive_analyze(data):
        yield result
    
    if operation == 'sum':
        yield {
            'int_sum': int_sum,
            'float_sum': float_sum,
        }
    elif operation == 'average':
        int_average = int_sum / int_count if int_count > 0 else None
        yield {
            'int_average': int_average
        }
    else:
        raise ValueError("Unsupported operation")


# 示例数据结构
data_structure = {
    'id': 0,  # 整数
    'name': '',  # 字符串
    'scores': [0.0],  # 浮点数列表
    'details': {
        'age': 0,  # 整数
        'height': 0.0,  # 浮点数
        'tags': ['']  # 字符串列表
    }
}

# 生成随机数据
print("生成的随机数据：")
random_data = {}
for data in generate_random_data(data_structure):
    random_data.update(data)
    print(data)

# 统计分析 - 求和
print("\n求和统计分析结果：")
for sum_result in analyze_data(random_data, operation='sum'):
    print(sum_result)

# 统计分析 - 求平均数
print("\n求平均数统计分析结果：")
for average_result in analyze_data(random_data, operation='average'):
    print(average_result)
