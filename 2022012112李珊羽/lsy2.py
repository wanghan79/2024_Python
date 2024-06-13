import random

class RandomDataStructure:
    def __init__(self, depth=3, max_items=5):
        self.depth = depth
        self.max_items = max_items
        self.data = self.generate_random_data()

    def generate_random_data(self):
        if self.depth == 0:
            return random.randint(1, 100) if random.choice([True, False]) else random.uniform(1.0, 100.0)
        else:
            items = []
            for _ in range(random.randint(1, self.max_items)):
                items.append(self.generate_random_data())
            return items

    def calculate_sum_and_average(self):
        def recursive_sum_average(data):
            if isinstance(data, list):
                total_int, total_float, count = 0, 0, 0
                for item in data:
                    int_sum, float_sum, item_count = recursive_sum_average(item)
                    total_int += int_sum
                    total_float += float_sum
                    count += item_count
                return total_int, total_float, count
            else:
                if isinstance(data, int):
                    return data, 0, 1
                elif isinstance(data, float):
                    return 0, data, 1

        total_int, total_float, count = recursive_sum_average(self.data)
        average_int = total_int / max(1, count) if count > 0 else 0
        average_float = total_float / max(1, count) if count > 0 else 0
        return total_int, total_float, average_int, average_float

# 创建一个随机数据结构实例
rds = RandomDataStructure(depth=2, max_items=3)
# 计算总和和平均数
total_int, total_float, average_int, average_float = rds.calculate_sum_and_average()
print(f"总整数和: {total_int}, 总浮点数和: {total_float}")
print(f"平均整数: {average_int}, 平均浮点数: {average_float}")
