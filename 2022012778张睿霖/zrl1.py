import random

def generate_data(**kwargs):
    result = []
    for key, value in kwargs.items():
        if key == 'int':
            data = [random.randint(value.get('min', 0), value.get('max', 100)) for _ in range(value.get('size', 1))]
        elif key == 'float':
            data = [random.uniform(value.get('min', 0.0), value.get('max', 1.0)) for _ in range(value.get('size', 1))]
        elif key == 'str':
            chars = value.get('chars', 'abcdefghijklmnopqrstuvwxyz0123456789')
            data = [''.join(random.choices(chars, k=value.get('len', 1))) for _ in range(value.get('size', 1))]
        elif key in ('tuple', 'list', 'set'):
            if 'size' in value:
                data = [generate_data(**value) for _ in range(value['size'])]
                data = tuple(data) if key == 'tuple' else list(data) if key == 'list' else {tuple(data)}
            else:
                data = generate_data(**value)
        result.append(data)
    return result

def summarize_data(data):
    int_sum, int_count, float_sum, float_count = 0, 0, 0, 0
    for item in data:
        if isinstance(item, int):
            int_sum += item
            int_count += 1
        elif isinstance(item, float):
            float_sum += item
            float_count += 1
    return int_sum, int_count, float_sum, float_count

if __name__ == '__main__':
    data = generate_data(
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
    )

    int_sum, int_count, float_sum, float_count = summarize_data(data)

    print("Generated Data:", data)
    # 可有可无
    # print("Sum of Integers:", int_sum)
    # print("Sum of Floats:", float_sum)
    # print("Average of Integers:", int_sum / max(int_count, 1))
    # print("Average of Floats:", float_sum / max(float_count, 1))
