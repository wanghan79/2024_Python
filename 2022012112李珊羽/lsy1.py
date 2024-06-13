import random
import string


def generate_random_structure(max_depth=3, current_depth=0):
    """
    递归生成随机数结构。

    :param max_depth: 最大的递归深度。
    :param current_depth: 当前的递归深度。
    :return: 嵌套字典结构的随机数。
    """
    if current_depth >= max_depth:
        # 达到最大深度，返回一个随机数
        return random.random()

    # 生成一个随机字符串作为键
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    # 递归生成值，可能是嵌套字典或随机数
    value = generate_random_structure(max_depth, current_depth + 1)

    # 生成另一个键值对，增加结构的复杂性
    another_key = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    another_value = random.randint(1, 100)  # 举例使用随机数作为另一个值

    # 返回嵌套字典
    return {
        key: value,
        another_key: another_value
    }


# 示例：生成一个最大深度为3的随机数结构
random_structure = generate_random_structure()
print(random_structure)
