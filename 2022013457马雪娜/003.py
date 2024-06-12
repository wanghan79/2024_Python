import random
import string

def calculate_sum_and_average(func):
    def wrapper(n):
        data = func(n)
        for index, d in enumerate(data, 1):
            d['integer_sum'] = d['random_integer'] + sum(d['random_list'][:1])  # 计算整数的和
            d['float_sum'] = d['random_float'] + sum(d['random_list'][1:2])  # 计算浮点数的和
            d['integer_average'] = (d['random_integer'] + sum(d['random_list'][:1])) / 2  # 计算整数的平均值
            d['float_average'] = (d['random_float'] + sum(d['random_list'][1:2])) / 2  # 计算浮点数的平均值
            print(f"Dictionary {index}: {d}")
        return data
    return wrapper

@calculate_sum_and_average
def generate_random_data(n):
    data = []
    for _ in range(n):
        random_string = ''.join(random.choices(string.ascii_letters, k=5))
        random_integer = random.randint(1, 100)
        random_float = round(random.uniform(1.0, 100.0), 2)
        random_list = [random.randint(1, 100), round(random.uniform(1.0, 100.0), 2), ''.join(random.choices(string.ascii_letters, k=5))]
        data.append({'random_string': random_string, 'random_integer': random_integer, 'random_float': random_float, 'random_list': random_list})
    return data

n = int(input("请输入一个整数 n："))
random_data = generate_random_data(n)
