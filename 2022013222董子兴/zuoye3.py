import re
import random
import string
from functools import wraps

# 装饰器：计算总和或平均值
def compute_total_or_mean(operation="sum"):
    def outer_wrapper(function):
        @wraps(function)
        def inner_wrapper(text_data):
            # 执行原始函数以获取数字
            extracted_numbers = function(text_data)
            # 根据指定类型执行操作
            if extracted_numbers:
                results = {
                    "总和": sum(extracted_numbers),
                    "平均值": sum(extracted_numbers) / len(extracted_numbers) if len(extracted_numbers) > 0 else 0
                }
                if operation in results:
                    print(f"{operation.capitalize()}: {results[operation]}")
                if operation == "both":
                    for key, value in results.items():
                        print(f"{key.capitalize()}: {value}")
            return extracted_numbers
        return inner_wrapper
    return outer_wrapper

# 函数：从文本中提取数字
@compute_total_or_mean(operation="both")
def find_numbers(text):
    # 提取所有数字（整数和小数）
    return [float(num) for num in re.findall(r'\b\d+(?:\.\d*)?\b', text)]

# 函数：生成随机数据
def generate_random_data(settings):
    type_actions = {
        'int': lambda item: random.randint(item.get('min', 0), item.get('max', 100)),
        'float': lambda item: round(random.uniform(item.get('min', 0.0), item.get('max', 100.0)), 2),
        'string': lambda item: ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(item.get('length', 10))),
        'list': lambda item: [generate_random_data({'data': [item['element']]})[0] for _ in range(item.get('count', 5))],
        'tuple': lambda item: tuple([generate_random_data({'data': [item['element']]})[0] for _ in range(item.get('count', 2))]),
    }
    results = []
    for _ in range(10):  # 生成10次数据以获得更多样本
        for item in settings.get('data', []):
            action = type_actions.get(item['type'])
            if action:
                results.append(action(item))
    return results

# 示例配置字典
configuration = {
    'data': [
        {'type': 'int', 'min': 1, 'max': 100},
        {'type': 'float', 'min': 0.1, 'max': 1.0},
        {'type': 'string', 'length': 15},
        {'type': 'list', 'element': {'type': 'float', 'min': 0.1, 'max': 1.0}, 'count': 5},
        {'type': 'tuple', 'element': {'type': 'int', 'min': 1, 'max': 100}, 'count': 3},
    ]
}

# 生成随机数据并打印
random_data = generate_random_data(configuration)
print("生成的数据:", random_data)
random_data_text = ' '.join(map(str, random_data))  # 将数据转换为字符串

# 使用增强的装饰器函数计算总和和平均值
find_numbers(random_data_text)
