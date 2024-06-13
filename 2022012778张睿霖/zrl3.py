import random

def calculate_statistics(func):
    def wrapper(self, **kwargs):
        data = func(self, **kwargs)
        int_sum, int_count, float_sum, float_count = self._summarize_data(data)
        int_avg = int_sum / max(int_count, 1)
        float_avg = float_sum / max(float_count, 1)
        return data, int_sum, float_sum, int_avg, float_avg
    return wrapper

class DataGenerator:
    @calculate_statistics
    def generate(self, **kwargs):
        return self._generate_data(**kwargs)

    def _generate_data(self, **kwargs):
        result = []
        for key, value in kwargs.items():
            if key == 'int':
                for _ in range(value.get('size', 1)):
                    result.append(random.randint(value.get('min', 0), value.get('max', 100)))
            elif key == 'float':
                for _ in range(value.get('size', 1)):
                    result.append(random.uniform(value.get('min', 0.0), value.get('max', 1.0)))
            elif key == 'str':
                chars = value.get('chars', 'abcdefghijklmnopqrstuvwxyz0123456789')
                for _ in range(value.get('size', 1)):
                    result.append(''.join(random.choices(chars, k=value.get('len', 1))))
            elif key in ('tuple', 'list', 'set'):
                gen_func = self._generate_data(**value) if 'size' in value else [self._generate_data(**value)]
                if key == 'set':
                    for _ in range(value.get('size', 1)):
                        result.append(tuple(gen_func))
                else:
                    result.extend(gen_func)
        return result

    def _summarize_data(self, data):
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
    generator = DataGenerator()
    data, int_sum, float_sum, int_avg, float_avg = generator.generate(
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
    print("Generated Data:", data)
    print("Sum of Integers:", int_sum)
    print("Sum of Floats:", float_sum)
    print("Average of Integers:", int_avg)
    print("Average of Floats:", float_avg)
