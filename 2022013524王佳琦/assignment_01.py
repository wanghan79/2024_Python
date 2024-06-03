import random
import string

def structDataSampling(num_samples, data_struct):
    results = []
    subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'Computer Science']

    for _ in range(num_samples):
        sample = {}
        for data_type, data_options in data_struct.items():
            if data_type == 'string':
                datarange = data_options.get('datarange', string.ascii_uppercase)
                len_range = data_options.get('len', (5, 10))
                str_len = random.randint(len_range[0], len_range[1])
                sample[data_type] = ''.join(random.choices(datarange, k=str_len))
            elif data_type == 'int':
                datarange = data_options.get('datarange', (1, 100))
                sample[data_type] = random.randint(datarange[0], datarange[1])
            elif data_type == 'float' or data_type == 'double':
                datarange = data_options.get('datarange', (0.0, 100.0))
                sample[data_type] = round(random.uniform(datarange[0], datarange[1]), 2)
            elif data_type == 'list':
                datarange = subjects
                sample[data_type] = random.sample(datarange, min(len(datarange), random.randint(1, len(datarange))))
            elif data_type == 'tuple':
                datarange = tuple(subjects)
                sample[data_type] = tuple(random.sample(list(datarange), min(len(datarange), random.randint(1, len(datarange)))))

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

samples = structDataSampling(num_samples, data_struct)

for sample in samples:
    print(sample)