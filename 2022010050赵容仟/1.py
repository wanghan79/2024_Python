import random
import string

# 定义数据结构规范
data_spec = {
    'integer': {'type': 'int', 'min': 1, 'max': 100},
    'float': {'type': 'float', 'min': 0.1, 'max': 0.5},
    'string': {'type': 'str', 'length': 10},
    'tuple': {'type': 'tuple', 'elements': [{'type': 'integer'}, {'type': 'string'}]},
    'list': {'type': 'list', 'count': 5, 'element_type': 'float'},
    'dict': {'type': 'dict', 'keys': ['key1', 'key2'], 'value_types': [{'type': 'str', 'length': 5}, {'type': 'int', 'min': 1, 'max': 10}]},
    'set': {'type': 'set', 'count': 3, 'element_type': 'string'}
}

# 根据规范生成随机数据的函数
def generate_random_data(spec):
    data_type = spec['type']
    
    if data_type == 'int':
        return random.randint(spec['min'], spec['max'])
    elif data_type == 'float':
        return round(random.uniform(spec['min'], spec['max']), 2)  # 保留两位小数
    elif data_type == 'str':
        return ''.join(random.choices(string.ascii_lowercase, k=spec['length']))
    elif data_type == 'tuple':
        return tuple(generate_random_data(sub_spec) for sub_spec in spec['elements'])
    elif data_type == 'list':
        return [generate_random_data({'type': sub_spec['type']}) for sub_spec in [spec['element_type']] * spec['count']]
    elif data_type == 'dict':
        return {key: generate_random_data(sub_spec) for key, sub_spec in zip(spec['keys'], spec['value_types'])}
    elif data_type == 'set':
        element = generate_random_data({'type': spec['element_type']})
        return {element for _ in range(spec['count'])}  # 创建一个包含count个元素的集合
    else:
        raise ValueError(f"Unsupported data type: {data_type}")

# 根据data_spec生成随机数据
random_data = generate_random_data(data_spec)

# 打印随机数据
print(random_data)