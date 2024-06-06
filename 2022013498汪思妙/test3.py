import random
import string

class RandomDataGenerator:
    def __init__(self, data_config):
        self.data_config = data_config

    def create_random_value(self, data_type):
        if data_type == 'int':
            return random.randint(*self.data_config[data_type]['range'])
        elif data_type == 'float':
            return round(random.uniform(*self.data_config[data_type]['range']), 2)
        elif data_type == 'str':
            return ''.join(random.choice(self.data_config[data_type]['datarange']) for _ in range(self.data_config[data_type]['length']))
        elif data_type == 'bool':
            return random.choice([True, False])
        elif data_type == 'list':
            datarange = self.data_config[data_type]['datarange']
            return random.sample(datarange, random.randint(1, len(datarange)))
        else:
            print(f"Unsupported data type: {data_type}")
            return None

    def generate_sample(self):
        sample = {}
        for data_type in self.data_config:
            if data_type in ['int', 'float', 'str', 'bool', 'list']:
                sample[data_type] = self.create_random_value(data_type)
            else:
                print(f"Invalid data type: {data_type}")
        return sample

    def generate_multiple_samples(self, num_samples):
        return [self.generate_sample() for _ in range(num_samples)]

# 定义生成随机数据的参数
data_config = {
    'int': {'range': (1, 100)},
    'float': {'range': (0.0, 100.0)},
    'str': {'length': 10, 'datarange': string.ascii_letters},
    'bool': {},
    'list': {'datarange': ['red', 'green', 'blue', 'yellow', 'black', 'white']}
}
generator = RandomDataGenerator(data_config)
num_samples = 5
samples = generator.generate_multiple_samples(num_samples)

# 装饰器定义
def statistics_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        int_values = [value for sample in result for value in sample.values() if isinstance(value, int)]
        float_values = [value for sample in result for value in sample.values() if isinstance(value, float)]
        int_sum = sum(int_values)
        float_sum = sum(float_values)
        int_average = int_sum / len(int_values) if int_values else 0
        float_average = float_sum / len(float_values) if float_values else 0
        print(f"Sum of integers: {int_sum}")
        print(f"Sum of floats: {float_sum}")
        print(f"Average of integers: {int_average}")
        print(f"Average of floats: {float_average}")
        return result
    return wrapper

# 使用装饰器
@statistics_decorator
def generate_samples(generator, num_samples):
    return [generator.generate_sample() for _ in range(num_samples)]

# 生成样本并计算总和和平均值
generate_samples(generator, num_samples)
