import random
import string

def create_random_value(data_type, data_config):
    if data_type == 'int':
        return random.randint(*data_config['range'])
    elif data_type == 'float':
        return round(random.uniform(*data_config['range']), 2)
    elif data_type == 'str':
        return ''.join(random.choice(string.ascii_letters) for _ in range(data_config['length']))
    elif data_type == 'bool':
        return random.choice([True, False])
    elif data_type == 'list':
        return random.sample(data_config['datarange'], random.randint(1, len(data_config['datarange'])))
    else:
        print(f"Unsupported data type: {data_type}")
        return None

def generate_sample(data_config):
    sample = {}
    for data_type, config in data_config.items():
        sample[data_type] = create_random_value(data_type, config)
    return sample

def generate_multiple_samples(data_config, num_samples):
    return [generate_sample(data_config) for _ in range(num_samples)]

# 定义生成随机数据的参数
data_config = {
    'int': {'range': (1, 100)},
    'float': {'range': (0.0, 100.0)},
    'str': {'length': 10},
    'bool': {},
    'list': {'datarange': ['red', 'green', 'blue', 'yellow', 'black', 'white']}
}

# 生成5个样本
num_samples = 5
samples = generate_multiple_samples(data_config, num_samples)

# 打印生成的样本
for i, sample in enumerate(samples, start=1):
    print(f"Sample {i}: {sample}")
