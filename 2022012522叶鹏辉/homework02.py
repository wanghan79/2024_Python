import random
import string

# 这里创建一个generator类，用户将所需要的数据结构传入这个类的构造函数，最后调用类的output方法即可
# 用户不需要了解类内的细节，只需要初始化他，并调用putout函数即可
class generator():
    def __init__(self, **kwarg):
        self.result = self.generating_data(**kwarg)

    def generating_data(self, **kwargs):
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
                result.append(self.generating_data(**value))
            return tuple(result)
        elif datatype == set:
            result = set()
            for key, value in subs.items():
                result.add(self.generating_data(**value))
            return result
        elif datatype == list:
            result = list()
            for key, value in subs.items():
                result.append(self.generating_data(**value))
            return result
        elif datatype == dict:
            result = dict()
            for key, value in subs.items():
                result[key] = self.generating_data(**value)
            return data_range(**result)
        else:
            return "illegal datatype !!! please check your input"
        # 对于这些类数组的容器数据类型，这里的处理方法都是遍历他的所以subs，然后递归调用generating_data函数
        # 接着把生成的subs们都添加到这一级的容器数据类型中再一并返回

    def putout(self):
        return self.result
    # 类封装完毕，下面展示的都是用户视角了


if __name__ == "__main__":
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
    G = generator(**example)
    print(G.putout())
    # 这里就是用户需要操作的了，初始化事例G，然后打印output的返回值
