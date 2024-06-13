import random

def generate_data_inner(**kwargs):
    for k, x in kwargs.items():
        if k == 'int':
            data = random.randint(x.get('min', 0), x.get('max', 100))
            yield data
        elif k == 'float':
            data = random.uniform(x.get('min', 0.0), x.get('max', 1.0))
            yield data
        elif k == 'str':
            chars = x.get('chars', 'abcdefghijklmnopqrstuvwxyz0123456789')
            data = ''.join(random.choices(chars, k=x.get('len', 1)))
            yield data
        elif k == 'tuple':
            yield tuple(generate_data_inner(**x) for _ in range(x.get('size', 1)))
        elif k == 'list':
            yield [generate_data_inner(**x) for _ in range(x.get('size', 1))]
        elif k == 'set':
            yield {tuple(generate_data_inner(**x)) for _ in range(x.get('size', 1))}

def generate_data(**kwargs):
    for _ in range(kwargs.get('num', 1)):
        data = list(generate_data_inner(**kwargs))
        yield data

def summarize_sample(sample):
    integers = [item for item in sample if isinstance(item, int)]
    floats = [item for item in sample if isinstance(item, float)]

    int_sum = sum(integers)
    int_avg = int_sum / len(integers) if integers else None

    float_sum = sum(floats)
    float_avg = float_sum / len(floats) if floats else None

    return int_sum, int_avg, float_sum, float_avg

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
        int_sum, int_avg, float_sum, float_avg = summarize_sample(sample)

        print("Sample:", sample)
        print("Integers Sum:", int_sum)
        print("Integers Average:", int_avg)
        print("Floats Sum:", float_sum)
        print("Floats Average:", float_avg)
        print()
