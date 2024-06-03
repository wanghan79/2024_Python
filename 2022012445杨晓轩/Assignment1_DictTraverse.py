import random

def dataSamping(**kwargs):
    result = []
    # 初始化一个空列表，用来存储结果
    for key, value in kwargs.items():
        # 遍历键值对
        if key == 'int':
            a, b = value['datarange']
            result.append(random.randint(a, b))
        elif key == 'float':
            a, b = value['datarange']
            result.append(random.uniform(a, b))
        elif key == 'str':
            datarange = value["datarange"]
            datalength = value["datalength"]
            result.append(''.join(random.choice(datarange)for _ in range(datalength)))
        elif key == 'tuple':
            result.append(tuple(dataSamping(**value)))
        elif key == 'set':
            result.append(set(dataSamping(**value)))
        elif key == 'list':
            result.append(list(dataSamping(**value)))
    return result


# 定义一个包含字典参数的示例字典
my_dict = {'tuple': {'int': {'datarange': [1, 10]},
                         'list': {
                             'int': {'datarange': [1, 10]},
                             'float': {'datarange': [1, 10]},
                             'str': {'datarange': "gfzxcv", "datalength": 6},
                             'tuple': {'str': {'datarange': "gfzxcv", "datalength": 6},
                                       'int': {'datarange': [1, 100]}}
                         },
                         'set': {
                             'int': {'datarange': [1, 10]},
                             'float': {'datarange': [1, 10]},
                             'str': {'datarange': "gfzxcv", "datalength": 6}
                         }
                         },
               'int': {'datarange': [1, 10]}
               }

if __name__ == '__main__':
    num = int(input("请输入一个整数num,表示想要生成的字典数目: \n")) # 指定生成的字典数量
    for i in range(1, num + 1):
        data_values = dataSamping(**my_dict)
        print("\nGenerated Data", i, ":")
        print(data_values)
