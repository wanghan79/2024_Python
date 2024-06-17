import random
import string

def validate_configurations(configurations):
    for data_type, settings in configurations.items():
        if data_type in ['int', 'float']:
            if 'datarange' not in settings or not isinstance(settings['datarange'], list) or len(settings['datarange']) != 2:
                raise ValueError(f"{data_type} 的 datarange 无效")
        elif data_type == 'str':
            if 'datarange' not in settings or not isinstance(settings['datarange'], str):
                raise ValueError(f"{data_type} 的 datarange 无效")
            if 'len' not in settings or not isinstance(settings['len'], int):
                raise ValueError(f"{data_type} 的 len 无效")
        elif data_type in ['tuple', 'list', 'set']:
            validate_configurations(settings)
        else:
            raise ValueError(f"不支持的数据类型: {data_type}")

def create_random_data(**kwargs):
    validate_configurations(kwargs)
    result = []

    for data_type, settings in kwargs.items():
        if data_type == 'int':
            min_val, max_val = settings['datarange']
            result.append(random.randint(min_val, max_val))
        elif data_type == 'float':
            min_val, max_val = settings['datarange']
            result.append(random.uniform(min_val, max_val))
        elif data_type == 'str':
            char_pool = settings['datarange']
            str_length = settings['len']
            result.append(''.join(random.choices(char_pool, k=str_length)))
        elif data_type == 'tuple':
            result.append(tuple(create_random_data(**settings)))
        elif data_type == 'list':
            result.append(create_random_data(**settings))
        elif data_type == 'set':
            result.append(set(create_random_data(**settings)))

    return result

# 示例参数用于生成多样化数据
config = {
    'tuple': {
        'int': {'datarange': [1, 100]},
        'list': {
            'int': {'datarange': [1, 50]},
            'float': {'datarange': [1.0, 100.0]},
            'str': {'datarange': string.ascii_letters + string.digits, 'len': 10},
            'tuple': {'str': {'datarange': string.ascii_lowercase, 'len': 15}}
        }
    }
}

# 生成5组随机数
random_data_sets = [create_random_data(**config) for _ in range(5)]

for i, data_set in enumerate(random_data_sets):
    print(f"随机数集合 {i+1}: {data_set}")
