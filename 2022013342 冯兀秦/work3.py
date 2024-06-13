import random
import string


def data_generator(func):
    def wrapper(self, data_structure, num_samples=1, **kwargs):
        for _ in range(num_samples):
            result = {}
            for root_name, root_spec in data_structure.items():
                if 'dataType' in root_spec:
                    data_type = root_spec['dataType']
                    kwargs = root_spec.get('kwargs', {})
                    if data_type == int:
                        daterange = kwargs.get('daterange', (0, 100))
                        result[root_name] = random.randint(daterange[0], daterange[1])
                    elif data_type == float:
                        daterange = kwargs.get('daterange', (0.0, 1.0))
                        result[root_name] = random.uniform(daterange[0], daterange[1])
                    elif data_type == str:
                        # 确保daterange是一个字符串序列
                        daterange = kwargs.get('daterange', string.ascii_letters)
                        length = kwargs.get('len', 5)
                        result[root_name] = ''.join(random.choices(daterange, k=length))
                    elif data_type == bool:
                        result[root_name] = random.choice([True, False])


            # 调用原始函数，并传入生成的数据
            func(self, result)

    return wrapper


class DataProcessor:
    @data_generator
    def process_data(self, data):
        # 这里可以按照需要处理数据
        print(data)

    # 示例用法


data_structure = {
    'int_value': {'dataType': int, 'kwargs': {'daterange': (1, 10)}},
    'float_value': {'dataType': float, 'kwargs': {'daterange': (0.5, 2.0)}},
    'str_value': {'dataType': str, 'kwargs': {'daterange': string.ascii_letters, 'len': 10}},
    'bool_value': {'dataType': bool},
    'list_value': {
        'dataType': list,
        'subs': {'sub1': {'dataType': int, 'kwargs': {'daterange': (10, 20), 'size': 3}}},
        'kwargs': {'size': 2}
    },
    'tuple_value': {
        'dataType': tuple,
        'subs': {
            'sub1': {'dataType': int, 'kwargs': {'daterange': (1, 5)}},
            'sub2': {'dataType': str, 'kwargs': {'daterange': string.ascii_letters, 'len': 3}}
        }
    }
}

processor = DataProcessor()
processor.process_data(data_structure, num_samples=3)  # 调用装饰后的方法
