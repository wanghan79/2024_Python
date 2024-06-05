import re
import random
import string
from functools import wraps

# sum_or_average 装饰器
def sum_or_average(operation="sum"):
    def decorator(func):
        @wraps(func)
        def wrapper(data):
            # 调用原始函数获取结果
            numbers = func(data)
            # 根据操作类型输出结果
            if numbers:  # 确保列表不为空
                if operation in ["sum", "both"]:
                    print(f"Sum: {sum(numbers)}")
                if operation in ["average", "both"]:
                    print(f"Average: {sum(numbers) / len(numbers)}")
            return numbers  # 返回原始函数的结果
        return wrapper
    return decorator

# sum 函数
@sum_or_average(operation="both")
def extract_numbers(data):
    # 从字符串中提取所有数字（整数和小数）
    return [float(num) for num in re.findall(r'\b\d+(?:\.\d*)?\b', data)]

# data_sampling 函数
def data_sampling(config):
    results = []
    for item in config.get('data', []):
        if item['type'] == 'int':
            value = random.randint(item.get('min', 0), item.get('max', 100))
        elif item['type'] == 'float':
            value = round(random.uniform(item.get('min', 0.0), item.get('max', 100.0)), 2)
        elif item['type'] == 'string':
            length = item.get('length', 10)
            value = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
        elif item['type'] == 'list':
            element = data_sampling({'data': [item['element']]})[0]
            value = [element for _ in range(item.get('count', 5))]
        elif item['type'] == 'tuple':
            element = data_sampling({'data': [item['element']]})[0]
            value = (element,) * item.get('count', 2)  # 创建一个元组
        else:
            continue  # 忽略未知类型
        results.append(value)
    return results

# 示例配置字典
config = {
    'data': [
        {'type': 'int', 'min': 1, 'max': 100},
        {'type': 'float', 'min': 0.1, 'max': 0.5},
        {'type': 'string', 'length': 10},
        {'type': 'list', 'element': {'type': 'float', 'min': 0.1, 'max': 0.5}, 'count': 3},
        {'type': 'tuple', 'element': {'type': 'int', 'min': 1, 'max': 100}, 'count': 2},
    ]
}

# 运行示例
sampled_data = data_sampling(config)
sampled_data_str = ' '.join(map(str, sampled_data))  # 将数据转换为字符串

# 调用装饰器函数，计算和与平均值
extract_numbers(sampled_data_str)  # 计算和与平均值