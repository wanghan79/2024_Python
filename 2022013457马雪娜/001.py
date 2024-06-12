import random
import string


def generate_random_data(n):
    data = []

    for i in range(n):
        random_data = {}

        # 生成随机字符串
        random_string = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 10)))
        random_data['random_string'] = random_string

        # 生成随机整数
        random_integer = random.randint(1, 100)
        random_data['random_integer'] = random_integer

        # 生成随机浮点数
        random_float = round(random.uniform(1.0, 100.0), 2)
        random_data['random_float'] = random_float

        # 生成随机列表
        random_list = [
            random.randint(1, 100),  # 随机整数
            round(random.uniform(1.0, 100.0), 2),  # 随机浮点数
            ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 10)))  # 随机字符串
        ]
        random_data['random_list'] = random_list

        data.append((i + 1, random_data))  # 添加序号

    return data


n = int(input("请输入一个整数 n："))
random_data = generate_random_data(n)

for index, data in random_data:
    print(f"{index}: {data}")
