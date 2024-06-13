import random

class DataGenerator:
    def generate(self, **kwargs):
        data = self._generate(**kwargs)
        int_sum, int_count, float_sum, float_count = self._summarize(data)
        int_avg = int_sum / max(int_count, 1)
        float_avg = float_sum / max(float_count, 1)
        return data, int_sum, float_sum, int_avg, float_avg

    def _generate(self, **kwargs):
        result = []
        for key, value in kwargs.items():
            if key == 'int':
                result.extend(random.randint(value.get('min', 0), value.get('max', 100)) for _ in range(value.get('size', 1)))
            elif key == 'float':
                result.extend(random.uniform(value.get('min', 0.0), value.get('max', 1.0)) for _ in range(value.get('size', 1)))
            elif key == 'str':
                chars = value.get('chars', 'abcdefghijklmnopqrstuvwxyz0123456789')
                result.extend(''.join(random.choices(chars, k=value.get('len', 1))) for _ in range(value.get('size', 1)))
            elif key in ('tuple', 'list', 'set'):
                gen_func = (self._generate(**value) if 'size' in value else [self._generate(**value)])
                result.extend((tuple(gen_func) if key == 'tuple' else list(gen_func)) if key == 'set' else gen_func)
        return result

    def _summarize(self, data):
        int_sum = sum(item for item in data if isinstance(item, int))
        int_count = sum(1 for item in data if isinstance(item, int))
        float_sum = sum(item for item in data if isinstance(item, float))
        float_count = sum(1 for item in data if isinstance(item, float))
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
