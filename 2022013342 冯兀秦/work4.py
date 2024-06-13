import random


# 这是一个生成随机数的生成器
def random_data_generator(num_items, min_value=0, max_value=100):
    for _ in range(num_items):
        yield random.randint(min_value, max_value)

    # 这不是一个真正的装饰器，而是一个封装函数，用于分析生成的数据


def analyze_data(func):
    def wrapper(*args, **kwargs):
        data_list = list(func(*args, **kwargs))
        mean = sum(data_list) / len(data_list)
        min_val = min(data_list)
        max_val = max(data_list)
        print(f"Mean: {mean}, Min: {min_val}, Max: {max_val}")
        return data_list

    return wrapper


# 使用@analyze_data会导致语法错误，因为analyze_data不是一个装饰器
# 但我们可以像下面这样使用它

def main():
    # 用户输入需要生成的数据组数
    num_groups = int(input("请输入需要生成的数据组数: "))

    # 示例：生成5组随机数据，每组包含10个随机数（0-100）
    for i in range(num_groups):
        # 使用封装函数来分析数据
        data = analyze_data(random_data_generator)(10)  # 传递参数给生成器
        print(f"Group {i + 1}: {data}")


if __name__ == "__main__":
    main()