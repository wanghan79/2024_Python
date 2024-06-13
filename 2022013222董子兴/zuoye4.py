import random
import string
from functools import wraps

# 装饰器：计算总和和平均值
def calculate_sum_and_average(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        if data:
            total_sum, total_count = sum_and_count(data)
            average = total_sum / total_count if total_count > 0 else 0
            print(f"总和: {total_sum}, 平均值: {average}")
        return data

    def sum_and_count(data):
        total_sum = 0
        total_count = 0
        for item in data:
            if isinstance(item, (int, float)):
                total_sum += item
                total_count += 1
            elif isinstance(item, (tuple, list)):
                for sub_item in item:
                    if isinstance(sub_item, (int, float)):
                        total_sum += sub_item
                        total_count += 1
        return total_sum, total_count

    return wrapper

class DataSampler:
    def __init__(self):
        pass

    @calculate_sum_and_average
    def data_sampling(self, datatype, datarange, num, strlen=8):
        """
        生成指定条件的随机数据集。

        :param datatype: 数据类型（int, float, str）
        :param datarange: 数据范围
        :param num: 数据点数量
        :param strlen: 字符串长度（生成字符串时使用）
        :return: 生成的数据集
        """
        def data_generator():
            for _ in range(num):
                if datatype is int:
                    it = iter(datarange)
                    yield random.randint(next(it), next(it))
                elif datatype is float:
                    it = iter(datarange)
                    yield random.uniform(next(it), next(it))
                elif datatype is str:
                    yield ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(strlen))

        result = set(data_generator())
        print(f"生成的{datatype.__name__}类型数据: {result}")
        return result

    @calculate_sum_and_average
    def list_sampling(self, data_type, num_list, name, id_range, grade_range, strlen=8):
        """
        生成指定数据的列表或元组。

        :param data_type: 容器类型（list, tuple）
        :param num_list: 数据条目数量
        :param name: 名字可能的字符
        :param id_range: ID范围
        :param grade_range: 成绩范围
        :param strlen: 名字的长度
        :return: 生成的数据条目集
        """
        def list_generator():
            for _ in range(num_list):
                item_name = ''.join(random.SystemRandom().choice(name) for _ in range(strlen))
                it = iter(id_range)
                item_id = random.randint(next(it), next(it))
                it = iter(grade_range)
                item_grade = random.uniform(next(it), next(it))

                if data_type is list:
                    yield [item_name, item_id, item_grade]
                elif data_type is tuple:
                    yield (item_name, item_id, item_grade)

        result = set(list_generator())
        print(f"生成的{data_type.__name__}类型数据: {result}")
        return result

# 使用DataSampler类实例化
sampler = DataSampler()

# 生成随机数据示例
random_data_int = sampler.data_sampling(int, (1, 100), 10)
random_data_float = sampler.data_sampling(float, (0.1, 0.9), 5)
