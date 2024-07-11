import random
def dataSampling(datatype,datarange,num,strlen=8):
    result=set()
    for index in range(0,num):
        if datatype is int:
            it = iter(datarange)
            item=random.randint(next(it),next(it))
            result.add(item)
            continue
        elif datatype is float:
            it = iter(datarange)
            item=random.uniform(next(it),next(it))
            result.add(item)
            continue
        elif datatype is str:
            item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
            result.add(item)
            continue
        else:
            continue
    return result

# 调用函数生成整型数据
int_data = dataSampling(int, (1, 100), 5)
print("生成的整型数据集合：", int_data)

# 调用函数生成浮点型数据
float_data = dataSampling(float, (1.0, 100.0), 5)
print("生成的浮点型数据集合：", float_data)

# 调用函数生成字符串数据
str_data = dataSampling(str, 'abcdefghijklmnopqrstuvwxyz', 5, 6)
print("生成的字符串数据集合：", str_data)

#重复
conflictdata=dataSampling(int,(1,5),10)
print("重复的",conflictdata)