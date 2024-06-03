import random

def random_generator(min_value, max_value, num):
    """
    生成器函数，用于生成一系列在指定范围内的随机整数。

    生成器行为:
    每次迭代此生成器时，将返回一个新的随机整数，直到返回了指定数量的随机数为止。


    """
    for _ in range(num):
        yield random.randint(min_value, max_value)

# 获取用户输入
min_value = int(input("请输入随机数的最小值："))
max_value = int(input("请输入随机数的最大值："))
num = int(input("请输入要生成的随机数的数量："))

# 创建随机数生成器对象
random_nums = random_generator(min_value, max_value, num)

# 通过迭代生成器获取并打印随机数
for num in random_nums:
    print(num)