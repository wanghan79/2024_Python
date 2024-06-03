import random
import string


class DataSampler:
    def __init__(self, num_samples, data_struct):
        self.num_samples = num_samples
        self.data_struct = data_struct
        self.subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'Computer Science']

    def generate_sample(self, data_type, data_options):
        if data_type == 'string':
            datarange = data_options.get('datarange', string.ascii_uppercase)
            len_range = data_options.get('len', (5, 10))
            str_len = random.randint(len_range[0], len_range[1])
            return ''.join(random.choices(datarange, k=str_len))
        elif data_type == 'int':
            datarange = data_options.get('datarange', (1, 100))
            return random.randint(datarange[0], datarange[1])
        elif data_type == 'float' or data_type == 'double':
            datarange = data_options.get('datarange', (0.0, 100.0))
            return round(random.uniform(datarange[0], datarange[1]), 2)
        elif data_type == 'list':
            datarange = self.subjects
            return random.sample(datarange, min(len(datarange), random.randint(1, len(datarange))))
        elif data_type == 'tuple':
            datarange = tuple(self.subjects)
            return tuple(random.sample(list(datarange), min(len(datarange), random.randint(1, len(datarange)))))

    def struct_data_sampling(self):
        results = []

        for _ in range(self.num_samples):
            sample = {}
            for data_type, data_options in self.data_struct.items():
                sample[data_type] = self.generate_sample(data_type, data_options)

            results.append(sample)

        return results


# 定义数据结构和样本数量
num_samples = 5  # 这里设定生成5个样本
data_struct = {
    'string': {'datarange': string.ascii_uppercase, 'len': (5, 10)},
    'int': {'datarange': (1, 100)},
    'float': {'datarange': (0.0, 100.0)},
    'double': {'datarange': (0.0, 100.0)},
    'list': {},
    'tuple': {}
}

# 创建 DataSampler 实例并生成样本
sampler = DataSampler(num_samples, data_struct)
samples = sampler.struct_data_sampling()

for sample in samples:
    print(sample)