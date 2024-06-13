import random
import string


def data_sampling_decorator(func):
    def wrapper(*args, **kwargs):
        results = func(*args, **kwargs)
        decorated_results = []
        for group in results:
            decorated_group = []
            for data, data_type in group:
                if isinstance(data, int):
                    decorated_data = f'整数数据：{data}'
                elif isinstance(data, float):
                    decorated_data = f'浮点数数据：{data:.2f}'
                elif isinstance(data, str):
                    decorated_data = f'字符串数据："{data}"'
                elif isinstance(data, list):
                    if all(isinstance(item, (int, float)) for item in data):
                        sum_value = sum(data)
                        avg_value = sum_value / len(data)
                        decorated_data = f'列表数据：{data},和为：{sum_value:.2f},均值为：{avg_value:.2f}'
                    else:
                        decorated_data = f'列表数据：{data},无法求和和均值'
                decorated_group.append(decorated_data)
            decorated_results.append(decorated_group)
        return decorated_results

    return wrapper


@data_sampling_decorator
def structDataSampling(num, struct):
    """
    根据给定的结构和数量生成随机数据。

    :param num: 生成的数据组数
    :param struct: 数据结构，一个字典，其中键是数据类型，值是包含数据范围和其他选项的字典
    :return: 包含格式化数据的列表
    """
    type_mapping = {int: '整型', float: '浮点型', str: '字符串型'}  # 添加类型映射
    results = []
    for _ in range(num):
        group = []
        for element_type, element_options in struct.items():
            data_range = element_options.get('data_range', None)  # 保持键名的一致性
            if element_type == int:
                random_number = random.randint(data_range[0], data_range[1])
                group.append((random_number, '整型'))
            elif element_type == float:
                random_number = random.uniform(data_range[0], data_range[1])
                group.append((random_number, '浮点型'))  # 使用映射或直接字符串
            elif element_type == str:
                str_length = element_options.get('len', 10)
                random_string = ''.join(random.choices(string.ascii_letters, k=str_length))  # 修复字符串生成
                group.append((random_string, '字符串型'))
                # 处理其他可能的数据类型...
        results.append(group)
    return results


# 示例
struct = {
    int: {'data_range': (1, 100)},
    float: {'data_range': (0.1, 1.0)},
    str: {'data_range': None, 'len': 5},
}
data = structDataSampling(3, struct)
print(data)