import random


# 第一种输出
# def dataSampling(**kwargs):
#     for _ in range(kwargs.get('num', 1)):
#         result = []
#         for key, value in kwargs.items():
#             if key == 'tuple':
#                 result.append(tuple(dataSampling(**value)))
#             elif key == 'list':
#                 result.append(list(dataSampling(**value)))
#             elif key == 'set':
#                 result.append(set(dataSampling(**value)))
#             elif key == 'int':
#                 a, b = value['datarange']
#                 result.append(random.randint(a, b))
#             elif key == 'float':
#                 a, b = value['datarange']
#                 result.append(random.uniform(a, b))
#             elif key == 'str':
#                 result.append(''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len'])))
#         yield result
# 输出形式：[10, ([1, [[15, 18.54138583134793, 'ncrnnmrimn']], (['nlfif'],)],)]

# 调整生成器输出的结构
def dataSampling(**kwargs):
    for _ in range(kwargs.get('num', 1)):
        result = []
        for key, value in kwargs.items():
            if key == 'int':
                a, b = value['datarange']
                result.append(random.randint(a, b))
            elif key == 'tuple':
                sub_result = []
                for sub_key, sub_value in value.items():
                    if sub_key == 'int':
                        a, b = sub_value['datarange']
                        sub_result.append(random.randint(a, b))
                    elif sub_key == 'list':
                        list_result = []
                        for list_key, list_value in sub_value.items():
                            if list_key == 'int':
                                a, b = list_value['datarange']
                                list_result.append(random.randint(a, b))
                            elif list_key == 'float':
                                a, b = list_value['datarange']
                                list_result.append(random.uniform(a, b))
                            elif list_key == 'str':
                                list_result.append(''.join(
                                    random.SystemRandom().choice(list_value['datarange']) for _ in
                                    range(list_value['len'])))
                        sub_result.append(list_result)
                    elif sub_key == 'tuple':
                        sub_tuple_result = []
                        for tuple_key, tuple_value in sub_value.items():
                            if tuple_key == 'str':
                                sub_tuple_result.append(''.join(
                                    random.SystemRandom().choice(tuple_value['datarange']) for _ in
                                    range(tuple_value['len'])))
                        sub_result.append(tuple(sub_tuple_result))
                result.append(tuple(sub_result))
        yield result


# 输出形式：[11, (9, [11, 16.84337551902997, 'mninncnmnr'], ('nicfn',))]


my_dict = {
    'num': 10,
    'int': {'datarange': (5, 15)},
    'tuple': {
        'int': {'datarange': (0, 10)},
        'list': {
            'int': {'datarange': (10, 15)},
            'float': {'datarange': (15, 20)},
            'str': {'datarange': 'cinmr', 'len': 10}
        },
        'tuple': {'str': {'datarange': 'ciflskfnmr', 'len': 5}}
    }
}

generator = dataSampling(**my_dict)

for _ in range(my_dict['num']):
    sample = next(generator)
    print(sample)
