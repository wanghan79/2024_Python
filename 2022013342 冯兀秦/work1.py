import string
import random


def data_Sampling(**kwargs):
    result = []
    if 'dataType' in kwargs:
        data_type = kwargs['dataType']
        if data_type == int:
            int_range = kwargs.get('int_range', (0, 100))  # 默认整数范围为0到100
            result.append(random.randint(int_range[0], int_range[1]))

        elif data_type == float:
            float_range = kwargs.get('float_range', (0.0, 1.0))  # 默认浮点数范围为0.0到1.0
            result.append(random.uniform(float_range[0], float_range[1]))

        elif data_type == str:
            characters = kwargs.get('characters', string.ascii_letters)  # 默认字符集为所有ASCII字母
            length = kwargs.get('length', 10)  # 默认字符串长度为10
            result.append(''.join(random.choices(characters, k=length)))

        elif data_type == bool:
            result.append(random.choice([True, False]))

        elif data_type == list:
            item_count = kwargs.get('item_count', 5)  # 默认列表项数量为5
            list_range = kwargs.get('list_range', (0, 100))  # 默认列表项范围为0到100
            result.append([random.randint(list_range[0], list_range[1]) for _ in range(item_count)])

        elif data_type == tuple:
            subs = kwargs.get('subs', {})  # 子元素定义
            result.append(tuple(data_Sampling(**sub_kwargs) for sub_kwargs in subs.values()))

    return result


# 示例嵌套字典，定义了如何生成元组数据
data_structure = {
    'dataType': tuple,
    'subs': {
        'sub1': {
            'dataType': str,
            'characters': string.ascii_letters + string.digits,  # 使用字母和数字
            'length': 5
        },
        'sub2': {
            'dataType': tuple,
            'subs': {
                'sub1': {
                    'dataType': int,
                    'int_range': (0, 10),  # 指定整数范围
                },
                'sub2': {
                    'dataType': list,
                    'item_count': 3,  # 指定列表项数量
                    'list_range': (50, 100)  # 指定列表项范围
                },
            },
        },
    },
}

# 询问用户需要生成的数据组数
times = int(input("请输入需要生成的数据组数："))

# 循环生成数据
for _ in range(times):
    print(data_Sampling(**data_structure))