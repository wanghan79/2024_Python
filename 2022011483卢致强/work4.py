import random
import string
from functools import wraps

#装饰器，用于计算数据类型和统计信息
def calculate_statistics(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        #调用原方法生成数据
        data = func(self, *args, **kwargs)
        
        int_sum, int_count, float_sum, float_count = 0, 0, 0.0, 0

        def calculate(data):
            nonlocal int_sum, int_count, float_sum, float_count
            
            if isinstance(data, int):
                int_sum += data
                int_count += 1
            elif isinstance(data, float):
                float_sum += data
                float_count += 1
            #如果数据是列表、元组或集合，递归统计其中的元素
            elif isinstance(data, (list, tuple, set)):
                for item in data:
                    calculate(item)
            #如果数据是字典，递归统计其值
            elif isinstance(data, dict):
                for value in data.values():
                    calculate(value)

        # 调用递归函数进行统计
        calculate(data)

        #计算平均值并打印统计结果
        int_avg = int_sum / int_count if int_count > 0 else 0
        float_avg = float_sum / float_count if float_count > 0 else 0
        print(f"整数类型的总和是: {int_sum}, 平均值是: {int_avg:.2f}")
        print(f"浮点数类型的总和是: {float_sum}, 平均值是: {float_avg:.2f}")

        return data

    return wrapper

class RandomGenerator:
    def __init__(self, seed=None):
        random.seed(seed)

    # @calculate_statistics
    # def generate_random_variable(self, data_types, num_variables):
    #     # 根据数据类型生成num_variables个随机数
    #     for _ in range(num_variables):
    #         random_type = random.choice(data_types)
    #         if random_type == int:
    #             yield self.random_integer()
    #         elif random_type == float:
    #             yield self.random_float()
    #         elif random_type == str:
    #             yield self.random_string()
    #         else:
    #             raise ValueError("不支持的类型")

    def random_integer(self):
        #随机整数
        return random.randint(1, 100)

    def random_float(self):
        #随机浮点数
        return random.uniform(0.0, 1.0)

    def random_string(self):
        #随机字符串
        return ''.join(random.choice(string.ascii_letters) for _ in range(5))

    def generate_random_lists(self, data_types, num_lists, items_per_list_min, items_per_list_max):
        # 生成包含随机数据的列表集合
        random_lists = []
        for _ in range(num_lists):
            items_count = random.randint(items_per_list_min, items_per_list_max)
            random_list = [self.generate_random_variable(data_types) for _ in range(items_count)]
            random_lists.append(random_list)
        return random_lists

    def sum_and_average_of_list(self, lst):
        #计算列表的和与平均值
        values = [item for item in lst if isinstance(item, (int, float))]
        sum_result = sum(values)
        average_result = sum_result / len(values) if values else None
        return sum_result, average_result

    def process_lists(self, lists):
        results = []
        for i, lst in enumerate(lists):
            sum_result, average_result = self.sum_and_average_of_list(lst)
            results.append((i, sum_result, average_result))
            if average_result is not None:
                print(f"列表 {i+1}: 总和 = {sum_result}, 平均数 = {average_result:.2f}")
            else:
                print(f"列表 {i+1} 包含非数值类型，无法计算和与平均")
        return results

    def generate_random_data_generator(self, data_types, total_items):
        """
        生成一个可迭代对象，逐个生成随机数据。
        :param data_types: 随机数据的数据类型列表。
        :param total_items: 要生成的随机数据总数。
        :return: 一个生成器，逐个产生随机数据。
        """
        for _ in range(total_items):
            # 根据数据类型生成随机数
            random_type = random.choice(data_types)
            if random_type == int:
                yield self.random_integer()
            elif random_type == float:
                yield self.random_float()
            elif random_type == str:
                yield self.random_string()
            else:
                raise ValueError("不支持的类型")

if __name__ == "__main__":
    rng = RandomGenerator(seed=42)

    data_types = [int, float, str]
    total_items = 20  # 假设我们想要生成20个随机数据

    # 使用生成器生成并打印随机数据
    random_data_generator = rng.generate_random_data_generator(data_types, total_items)
    for item in random_data_generator:
        print(item)
