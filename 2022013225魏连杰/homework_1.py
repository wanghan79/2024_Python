# 随机数生成
import random
def myRandom(datatype, datarange, num, strlen=8):
    result = []
    for _ in range(num):
        if datatype == int:
            result.append(random.randint(datarange[0], datarange[1]))
        elif datatype == float:
            result.append(random.uniform(datarange[0], datarange[1]))
        elif datatype == str:
            item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
            result.append(item)
        else:
            raise ValueError("Unsupported data type. Supported types are int, float, and str.")
    return result

# 示例调用
# 生成10个范围在0到99之间的整数
print(myRandom(int, (0, 99), 10))
# 生成5个范围在1.0到10.0之间的浮点数
print(myRandom(float, (1.0, 10.0), 5))
# 生成3个长度为8的随机字符串，字符范围是0到9
print(myRandom(str, "abcdefj", 3))