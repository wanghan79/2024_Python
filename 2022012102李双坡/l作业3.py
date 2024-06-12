import random
import string
import time

def calculate_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"函数 {func.__name__} 执行时间: {execution_time} 秒")
        return result
    return wrapper

def generate_random_data(data_structure):
    """
    根据定义的数据结构生成随机数据。
    
    :param data_structure: 预定义的数据结构，包含整数、浮点数和字符串
    :return: 填充了随机数据的结构
    """
    if isinstance(data_structure, int):
        # 生成随机整数
        return random.randint(0, 100)
    elif isinstance(data_structure, float):
        # 生成随机浮点数
        return round(random.uniform(0.0, 100.0), 2)
    elif isinstance(data_structure, str):
        # 生成随机字符串
        length = random.randint(5, 15)  # 随机长度在5到15之间
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    elif isinstance(data_structure, list):
        # 递归生成列表中的每个元素
        return [generate_random_data(data_structure[0]) for _ in range(random.randint(1, 10))]
    elif isinstance(data_structure, dict):
        # 递归生成字典中的每个值
        return {key: generate_random_data(value) for key, value in data_structure.items()}
    else:
        raise ValueError("Unsupported data structure")

@calculate_execution_time
def analyze_data(data, operation='sum'):
    """
    对生成的数据进行统计分析。
    
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
        elif isinstance(data, float):
            float_sum += data
        elif isinstance(data, (list, tuple)):
            for item in data:
                recursive_analyze(item)
        elif isinstance(data, dict):
            for key, value in data.items():
                recursive_analyze(value)

    recursive_analyze(data)
    
    if operation == 'sum':
        return {
            'int_sum': int_sum,
            'float_sum': float_sum,
        }
    elif operation == 'average':
        int_average = int_sum / int_count if int_count > 0 else None
        return {
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
random_data = generate_random_data(data_structure)
print("生成的随机数据：")
print(random_data)

# 统计分析 - 求和
sum_stats = analyze_data(random_data, operation='sum')
print("\n求和统计分析结果：")
print(f"整数之和: {sum_stats['int_sum']}")
print(f"浮点数之和: {sum_stats['float_sum']}")

# 统计分析 - 求平均数
average_stats = analyze_data(random_data, operation='average')
print("\n求平均数统计分析结果：")
print(f"整数的平均值: {average_stats['int_average']}")
