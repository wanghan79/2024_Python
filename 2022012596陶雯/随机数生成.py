import random
import string

def generate_random_tuple():
    random_string = ''.join(random.choices(string.ascii_letters, k=8))  # 生成长度为8的随机字符串作为id
    random_int = random.randint(18, 100)  # 生成范围在18到100之间的随机整数作为年龄
    random_float = round(random.uniform(0, 100), 2)  # 生成范围在0到100之间的随机两位小数浮点数作为成绩
    return (random_string, random_int, random_float)

def generate_multiple_random_tuples(num_tuples):
    return [generate_random_tuple() for _ in range(num_tuples)]

# 输入要生成的元组数量
num_tuples_to_generate = int(input("请输入要随机生成的元组数："))

# 生成指定数量的元组
random_tuples = generate_multiple_random_tuples(num_tuples_to_generate)

# 打印生成的元组
for i, t in enumerate(random_tuples, 1):
    print(f"Tuple {i}: {t}")
