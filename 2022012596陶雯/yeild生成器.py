import random
import string

def generate_random_tuples(num_tuples):
    int_sum = 0
    float_sum = 0
    for _ in range(num_tuples):
        random_string = ''.join(random.choices(string.ascii_letters, k=8))  # 生成长度为8的随机字符串
        random_int = random.randint(18, 100)  # 生成范围在18到100之间的随机整数
        random_float = round(random.uniform(0, 100), 2)  # 生成范围在0到100之间的随机两位小数浮点数，保留两位小数
        # 计算整数和与浮点数和
        int_sum += random_int
        float_sum += random_float
        yield random_string, random_int, random_float

    # 计算整数平均值与浮点数平均值,并保留两位小数
    int_average = round(int_sum / num_tuples, 2)
    float_average = round(float_sum / num_tuples, 2)
    # 返回类型统计结果
    yield {"整数和": int_sum, "浮点数和": float_sum, "整数平均数": int_average, "浮点数平均数": float_average}

# 提示用户输入要生成的元组数量
num_tuples = int(input("请输入要生成的元组数量："))

# 生成随机元组
generator = generate_random_tuples(num_tuples)

# 使用生成器逐步生成随机元组并打印
for i, t in enumerate(generator, 1):
    if isinstance(t, dict):
        # 打印类型统计结果
        print("\n类型统计结果:")
        for key, value in t.items():
            print(f"{key}: {value}")
    else:
        # 打印生成的随机元组
        print(f"Tuple {i}: {t}")
