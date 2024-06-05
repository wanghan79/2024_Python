import random
import string

def data_sample_inner(data_type, **kwargs):
    """根据传入的参数类型生成相应类型的数据"""
    if data_type == 'int':
        return random.randint(kwargs.get('min', 1), kwargs.get('max', 100))
    elif data_type == 'float':
        return round(random.uniform(kwargs.get('min', 0.0), kwargs.get('max', 1.0)), 2)
    elif data_type == 'str':
        length = kwargs.get('length', 10)
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    elif data_type == 'tuple':
        return tuple(data_sample_inner(sub_data_type, **sub_kwargs) for sub_data_type, sub_kwargs in kwargs.get('elements', []))
    elif data_type == 'list':
        element = data_sample_inner(kwargs.get('element_type'), **kwargs)
        return [element for _ in range(kwargs.get('size', 5))]
    elif data_type == 'set':
        element = data_sample_inner(kwargs.get('element_type'), **kwargs)
        return {element for _ in range(kwargs.get('size', 5))}  # Use set comprehension to avoid duplicate elements
    else:
        raise ValueError(f"Unsupported data type: {data_type}")

def data_sample_generator(num, **kwargs):
    """生成指定数量的数据样本"""
    for _ in range(num):
        yield data_sample_inner(kwargs['data_type'], **kwargs)

# 测试部分
if __name__ == "__main__":
    # 指定参数配置
    params = {
        'data_type': 'list',
        'element_type': {'data_type': 'float'},  # 配置元素类型为浮点数
        'min': 0.0,
        'max': 100.0,
        'size': 5  # 列表大小
    }

    # 创建迭代器
    iterator = data_sample_generator(
        num=5,  # 要生成的数据样本数量
        **params
    )
    
    # 遍历迭代器并打印每个生成的样本
    for sample in iterator:
        print(sample)