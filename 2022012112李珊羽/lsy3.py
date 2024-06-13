import random

def calculate_average(method):
    def wrapper(self):
        int_values = []
        float_values = []

        def gather_values(data):
            if isinstance(data, list):
                for item in data:
                    gather_values(item)
            elif isinstance(data, int):
                int_values.append(data)
            elif isinstance(data, float):
                float_values.append(data)

        gather_values(self.data)
        int_average = sum(int_values) / max(1, len(int_values)) if int_values else 0
        float_average = sum(float_values) / max(1, len(float_values)) if float_values else 0
        return int_average, float_average

    return wrapper

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

    @calculate_average
    def get_averages(self):
        pass

# 创建一个随机数据结构实例
rds = RandomDataStructure(depth=2, max_items=3)
# 获取整数和浮点数的平均值
int_average, float_average = rds.get_averages()
print(f"整数的平均值: {int_average}")
print(f"浮点数的平均值: {float_average}")
