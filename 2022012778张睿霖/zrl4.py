import random

def generate_data_inner(**kwargs):
    result = []
    for k, x in kwargs.items():
        data = None  # 默认赋值为 None
        if k == 'int':
            data = random.randint(x.get('min', 0), x.get('max', 100))
        elif k == 'float':
            data = random.uniform(x.get('min', 0.0), x.get('max', 1.0))
        elif k == 'str':
            chars = x.get('chars', 'abcdefghijklmnopqrstuvwxyz0123456789')
            data = ''.join(random.choices(chars, k=x.get('len', 1)))
        elif k == 'tuple':
            data = tuple(generate_data_inner(**x) for _ in range(x.get('size', 1)))
        elif k == 'list':
            data = [generate_data_inner(**x) for _ in range(x.get('size', 1))]
        elif k == 'set':
            data = {tuple(generate_data_inner(**x)) for _ in range(x.get('size', 1))}
        result.append(data)
    return result

def generate_data(**kwargs):
    for _ in range(kwargs.get('num', 1)):
        yield generate_data_inner(**kwargs)

if __name__ == '__main__':
    for sample in generate_data(
        num=5,
        int={'min': 10, 'max': 20, 'size': 7},
        tuple={
            'list': {'int': {'min': 5, 'max': 15, 'size': 3}},
            'float': {'min': 1, 'max': 10, 'size': 5},
            'str': {'chars': 'abc123', 'len': 6, 'size': 4},
            'tuple': {
                'str': {'chars': 'wjs2kqn31', 'len': 5, 'size': 5},
                'list': {'float': {'min': 0.5, 'max': 2.5, 'size': 4}},
                'int': {'min': 30, 'max': 50, 'size': 3}
            }
        }
    ):
        print(sample)
