import random
import string

class RandomDataGenerator:
    def __init__(self, num_tuples):
        self.num_tuples = num_tuples

    def generate_random_tuples(self):
        random_tuples = []
        int_sum = 0
        float_sum = 0
        for _ in range(self.num_tuples):
            random_string = ''.join(random.choices(string.ascii_letters, k=8))  # 生成长度为8的随机字符串
            random_int = random.randint(18, 100)  # 生成范围在18到100之间的随机整数
            random_float = round(random.uniform(0, 100), 2)  # 生成范围在0到100之间的随机浮点数，保留两位小数
            random_tuples.append((random_string, random_int, random_float))
            # 计算整数和与浮点数和
            int_sum += random_int
            float_sum += random_float
        # 计算整数平均值与浮点数平均值
        int_average = int_sum / self.num_tuples
        float_average = float_sum / self.num_tuples
        # 返回元组及类型统计结果
        return random_tuples, {"整数和": int_sum, "浮点数和": float_sum, "整数平均数": int_average, "浮点数平均数": float_average}

# 提示用户输入要生成的元组数量
num_tuples = int(input("请输入要生成的元组数量："))

# 创建 RandomDataGenerator 实例
data_generator = RandomDataGenerator(num_tuples)

# 生成随机元组
random_tuples, stats = data_generator.generate_random_tuples()

# 打印生成的随机元组
for i, t in enumerate(random_tuples, 1):
    print(f"Tuple {i}: {t}")

# 打印类型统计结果
print("\n类型统计结果:")
for key, value in stats.items():
    print(f"{key}: {value}")
