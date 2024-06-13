import random

def generate_data(data_type, data_range, length=None):
    if data_type == 'int':
        return random.randint(data_range[0], data_range[1])
    elif data_type == 'float':
        return random.uniform(data_range[0], data_range[1])
    elif data_type == 'str':
        return ''.join(random.choice(data_range) for _ in range(length))
    elif data_type == 'tuple':
        return tuple(generate_data(dt, dr) for dt, dr in data_range.items())
    elif data_type == 'list':
        return [generate_data(dt, dr) for dt, dr in data_range.items()]
    elif data_type == 'set':
        return set(generate_data(dt, dr) for dt, dr in data_range.items())

def data_sample(num, **kwargs):
    data_samples = []
    for _ in range(num):
        data_samples.append(generate_data(**kwargs))
    return data_samples

if __name__ == '__main__':
    sample = {
        'num': 5,
        'tuple': {
            'int': {'data_range': [1, 10]},
            'list': {
                'int': {'data_range': [1, 10]},
                'float': {'data_range': [1, 10]},
                'str': {'data_range': 'q1w2e3', 'length': 8},
                'tuple': {'str': {'data_range': 'q1w2e3r4t5y6', 'length': 5}}
            }
        }
    }
    print(data_sample(**sample))
