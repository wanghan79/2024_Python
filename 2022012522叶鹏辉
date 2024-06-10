import random
import string

# 本函数的功能是用随机数来填充完成给定的树形数据结构

# 数据结构如example所示，这里的数据结构用于测试各种情况下的输出

# 注意在输入data_range时必须为list或tuple而不是单独的数字或无法用下标访问的变量，否则会打印出报错信息
example = {
    "data_type": tuple,
    "subs": {
        "sub1": {"data_type": list,
                 # 这里用于测试datatype为list时的表现
                 "subs": {
                     "sub1": {
                         "data_type": int,
                         "data_range": [100]
                         # 这里的样例来测试range只有一个数时生成0到这个数
                     },

                     "sub2": {
                         "data_type": float,
                         "data_range": (0, 50)
                         # 这里的样例用于测试range为两个值时的输出
                     },
                     "sub3": {
                         "data_type": str,
                         "data_range": string.ascii_uppercase,
                         "len": 3
                         # 这里的样例用于测试字符串范围为大写字母表时的样例表现
                     },
                     "sub4": {
                         "data_type": int,
                         "data_range": [1, 2, 23, 4, 2, 34]
                         # 这里的样例来测试range为离散的情况
                     },
                 },
                 },
        "sub2": {"data_type": tuple,
                 "subs": {
                     "sub1": {
                         "data_type": int,
                         "data_range": (0, 100)
                     },
                     "sub2": {
                         "data_type": str,
                         "data_range": string.ascii_uppercase,
                         "len": 10
                     },
                     "sub3": {
                         "data_type": str,
                         "data_range": [123123],
                         # 这里处理字符串范围异常的情况
                         "len": 10
                     },
                     "sub4": {
                         "data_type": bool,
                         "data_range": []
                         # 测试bool 变量，注意range也要使用[]来输入
                     }

                 },
                 },
        "sub3": {
            "data_type": str,
            "data_range": "abc",
            # 这里测试字符串为普通字符串的情况
            "len": 10

        },

    }
}


def generating_data(**kwargs):
    datatype = kwargs.get('data_type')
    data_range = kwargs.get('data_range')
    subs = kwargs.get('subs')
    if datatype == int:
        if len(data_range) == 1:
            return random.randint(0, data_range[0])
        elif len(data_range) == 2:
            min_num = min(data_range[0], data_range[1])
            max_num = max(data_range[0], data_range[1])
            return random.randint(min_num, max_num)
        # 比较两者中的较大较小值避免报错
        else:
            random_index = random.randint(0, len(data_range) - 1)
            return data_range[random_index]
        # 若范围为一个数，返回0到这个数的随机数（当然要保证为正），若为两个数则返回，这两个数之间的值
    elif datatype == bool:
        if len(data_range) == 1:
            return data_range[0]
        else:
            return random.choice([True, False])
        # 如果bool变量的范围为1直接范围,如果没有设定则返回随机bool变量
    elif datatype == float:
        if len(data_range) == 1:
            return round(random.uniform(0, data_range[0]), 2)
        elif len(data_range) == 2:
            min_num = min(data_range[0], data_range[1])
            max_num = max(data_range[0], data_range[1])
            return round(random.uniform(min_num, max_num), 2)
        else:
            rnd_idx = random.randint(0, len(data_range) - 1)
            return data_range[rnd_idx]
        # 这里默认保留两位小数
    elif datatype == str:
        if isinstance(data_range, str):
            data_len = kwargs.get('len')
            return ''.join(random.choice(data_range) for _ in range(data_len))
        else:
            return "illegal data range!!! please make sure you input is str!!!"
        # 返回报错信息
    elif datatype == tuple:
        result = []
        for key, value in subs.items():
            result.append(generating_data(**value))
        return tuple(result)
    elif datatype == set:
        result = set()
        for key, value in subs.items():
            result.add(generating_data(**value))
        return result
    elif datatype == list:
        result = list()
        for key, value in subs.items():
            result.append(generating_data(**value))
        return result
    elif datatype == dict:
        result = dict()
        for key, value in subs.items():
            result[key] = generating_data(**value)
        return data_range(**result)
    else:
        return "illegal datatype !!! please check your input"
    # 对于这些类数组的容器数据类型，这里的处理方法都是遍历他的所以subs，然后递归调用generating_data函数
    # 接着把生成的subs们都添加到这一级的容器数据类型中再一并返回


print(generating_data(**example))
