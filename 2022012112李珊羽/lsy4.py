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

class RandomDataStructureGenerator:
    def __init__(self, max_depth=3, max_items=5):
        self.max_depth = max_depth
        self.max_items = max_items

    def generate_random_data(self):
        if random.randint(0, self.max_depth) == 0:
            if random.choice([True, False]):
                return random.randint(1, 100)
            else:
                return random.uniform(1.0, 100.0)
        else:
            items = []
            for _ in range(random.randint(1, self.max_items)):
                items.append(self.generate_random_data())
            return items

    def __iter__(self):
        return self

    def __next__(self):
        return RandomDataStructure(self.generate_random_data())

class RandomDataStructure:
    def __init__(self, data):
        self.data = data

    @calculate_average
    def get_averages(self):
        pass

# 创建一个生成器来生成随机数据结构
generator = RandomDataStructureGenerator(max_depth=3, max_items=5)

# 使用生成器并计算每组数据的平均值
for rds in generator:
    int_average, float_average = rds.get_averages()
    print(f"数据结构: {rds.data}")
    print(f"整数的平均值: {int_average}")
    print(f"浮点数的平均值: {float_average}")
    print("---")
