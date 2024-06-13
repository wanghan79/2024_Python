import random

class RandomDataGenerator:
    def __init__(self):
        pass

    def _generate_data(self, data_spec):
        data_type = data_spec['type']
        if data_type == 'int':
            return random.randint(*data_spec['datarange'])
        elif data_type == 'float':
            return random.uniform(*data_spec['datarange'])
        elif data_type == 'str':
            return ''.join(random.choice(data_spec['datarange']) for _ in range(data_spec['len']))
        elif data_type == 'tuple':
            return tuple(self._generate_data(item) for item in data_spec['elements'])
        elif data_type == 'list':
            return [self._generate_data(item) for item in data_spec['elements']]
        elif data_type == 'set':
            return set(self._generate_data(item) for item in data_spec['elements'])
        else:
            raise ValueError(f"Unsupported data type: {data_type}")

    def generate_samples(self, num, data_spec):
        return [self._generate_data(data_spec) for _ in range(num)]

# 使用示例
if __name__ == '__main__':
    generator = RandomDataGenerator()
    samples = generator.generate_samples(
        5,
        {
            'type': 'tuple',
            'elements': [
                {'type': 'int', 'datarange': [1, 10]},
                {'type': 'list', 'elements': [
                    {'type': 'int', 'datarange': [1, 10]},
                    {'type': 'float', 'datarange': [1, 10]},
                    {'type': 'str', 'datarange': 'q1w2e3', 'len': 8},
                    {'type': 'tuple', 'elements': [
                        {'type': 'str', 'datarange': 'q1w2e3r4t5y6', 'len': 5}
                    ]}
                ]}
            ]
        }
    )
    print(samples)
