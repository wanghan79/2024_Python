import random

def generate_data(**kwargs):
    result = []
    for k, x in kwargs.items():
        if k == 'int':
            data = [random.randint(x.get('min', 0), x.get('max', 100)) for _ in range(x.get('size', 1))]
        elif k == 'float':
            data = [random.uniform(x.get('min', 0.0), x.get('max', 1.0)) for _ in range(x.get('size', 1))]
        elif k == 'str':
            chars = x.get('chars', 'abcdefghijklmnopqrstuvwxyz0123456789')
            data = [''.join(random.choices(chars, k=x.get('len', 1))) for _ in range(x.get('size', 1))]
        elif k in ('tuple', 'list', 'set'):
            if 'size' in x:
                data = [generate_data(**x) for _ in range(x['size'])]
                data = tuple(data) if k == 'tuple' else list(data) if k == 'list' else {tuple(data)}
            else:
                data = generate_data(**x)
        result.append(data)
    return result

if __name__ == '__main__':
    print(generate_data(
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
    ))
