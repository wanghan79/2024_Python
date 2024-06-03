import random
import string


class DataGenerator:
    def __init__(self, data_struct):
        self.data_struct = data_struct
        self.subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'Computer Science']

    def _gen_string(self, datarange, length):
        for _ in range(length):
            yield random.choice(datarange)

    def _gen_int(self, datarange):
        start, end = datarange
        while True:
            yield random.randint(start, end)

    def _gen_float(self, datarange):
        start, end = datarange
        while True:
            yield round(random.uniform(start, end), 2)

    def generate_sample(self, data_type, data_options):
        if data_type == 'string':
            datarange = data_options.get('datarange', string.ascii_uppercase)
            len_range = data_options.get('len', (5, 10))
            str_len = random.randint(*len_range)
            return ''.join(self._gen_string(datarange, str_len))
        elif data_type == 'int':
            datarange = data_options.get('datarange', (1, 100))
            return next(self._gen_int(datarange))
        elif data_type == 'float' or data_type == 'double':
            datarange = data_options.get('datarange', (0.0, 100.0))
            return next(self._gen_float(datarange))
        elif data_type == 'list':
            datarange = self.subjects
            return random.sample(datarange, min(len(datarange), random.randint(1, len(datarange))))
        elif data_type == 'tuple':
            datarange = tuple(self.subjects)
            return tuple(random.sample(list(datarange), min(len(datarange), random.randint(1, len(datarange)))))

    def struct_data_sampling(self, num_samples):
        for _ in range(num_samples):
            sample = {}
            for data_type, data_options in self.data_struct.items():
                sample[data_type] = self.generate_sample(data_type, data_options)
            yield sample

# 定义数据结构
data_struct = {
    'string': {'datarange': string.ascii_uppercase, 'len': (5, 10)},
    'int': {'datarange': (1, 100)},
    'float': {'datarange': (0.0, 100.0)},
    'double': {'datarange': (0.0, 100.0)},
    'list': {},
    'tuple': {}
}

# 创建 DataGenerator 实例并生成样本
generator = DataGenerator(data_struct)

# 生成并打印样本
num_samples = 5
for sample in generator.struct_data_sampling(num_samples):
    print(sample)