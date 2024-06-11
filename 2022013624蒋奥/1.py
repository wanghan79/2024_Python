import random
import string

# 生成随机数据的函数
def generate_random_data(structure):
    """
    该函数根据给定的数据结构生成随机数据

    参数：
    structure (dict)：包含数据类型和相关范围等信息的数据结构
    """
    result = []  # 用于存储生成的随机数据结果

    # 如果是字典类型
    if isinstance(structure, dict):
        data_type = structure['data_type']  # 获取数据类型
        subs = structure.get('subs', {})  # 获取子结构

        # 如果数据类型是元组
        if data_type == tuple:
            # 递归处理子结构并生成结果列表
            sub_results = [generate_random_data(sub) for sub in subs.values()]
            result.append(tuple(sub_results))  # 将子结果添加为元组
        elif data_type == list:
            # 递归处理子结构并生成结果列表
            sub_results = [generate_random_data(sub) for sub in subs.values()]
            result.append(list(sub_results))  # 将子结果添加为列表

        # 遍历子结构
        for key, sub_structure in subs.items():
            result.extend(generate_random_data(sub_structure))  # 扩展结果列表

    # 如果数据类型是整数、浮点数、字符串或布尔类型
    elif data_type in [int, float, str, bool]:
        # 对于整数类型
        if data_type == int:
            # 如果数据范围是列表且非空
            if isinstance(structure['data_range'], list) and structure['data_range']:
                result.append(random.choice(structure['data_range']))  # 从范围列表中随机选择并添加
            # 如果数据范围是长度为 2 的元组
            elif isinstance(structure['data_range'], tuple) and len(structure['data_range']) == 2:
                result.append(random.randint(*structure['data_range']))  # 生成范围内的随机整数并添加
        # 对于浮点数类型
        elif data_type == float:
            # 如果数据范围是长度为 2 的元组
            if isinstance(structure['data_range'], tuple) and len(structure['data_range']) == 2:
                result.append(random.uniform(*structure['data_range']))  # 生成范围内的随机浮点数并添加
        # 对于字符串类型
        elif data_type == str:
            # 如果数据范围是字符串或列表且指定了长度
            if isinstance(structure['data_range'], (str, list)) and 'len' in structure:
                result.append(''.join(random.choice(structure['data_range']) for _ in range(structure['len'])))  # 生成指定长度的随机字符串并添加
        # 对于布尔类型
        elif data_type == bool:
            result.append(random.choice([True, False]))  # 随机选择布尔值并添加
    return result  # 返回生成的随机数据结果

print(generate_random_data(example)) 