import random
import string

class RandomDataGenerator:
    def __init__(self, data_config):
        self.data_config = data_config

    def create_random_value(self, data_type):
        if data_type == 'int':
            return random.randint(*self.data_config[data_type]['range'])
        elif data_type == 'float':
            return round(random.uniform(*self.data_config[data_type]['range']), 2)
        elif data_type == 'str':
            return ''.join(random.choice(self.data_config[data_type]['datarange']) for _ in range(self.data_config[data_type]['length']))
        elif data_type == 'bool':
            return random.choice([True, False])
        elif data_type == 'list':
            datarange = self.data_config[data_type]['datarange']
            return random.sample(datarange, random.randint(1, len(datarange)))
        else:
            print(f"Unsupported data type: {data_type}")
            return None

    def generate_sample(self):
        sample = {}
        for data_type in self.data_config:
            if data_type in ['int', 'float', 'str', 'bool', 'list']:
                sample[data_type] = self.create_random_value(data_type)
            else:
                print(f"Invalid data type: {data_type}")
        return sample

    def generate_multiple_samples(self, num_samples):
        class SampleIterator:
            def __init__(self, generator, num_samples):
                self.generator = generator
                self.num_samples = num_samples
                self.counter = 0

            def __iter__(self):
                return self

            def __next__(self):
                if self.counter < self.num_samples:
                    self.counter += 1
                    return self.generator.generate_sample()
                else:
                    raise StopIteration

        return SampleIterator(self, num_samples)
data_config = {
    'int': {'range': (1, 100)},
    'float': {'range': (0.0, 100.0)},
    'str': {'length': 10, 'datarange': string.ascii_letters},
    'bool': {},
    'list': {'datarange': ['red', 'green', 'blue', 'yellow', 'black', 'white']}
}
generator = RandomDataGenerator(data_config)
num_samples = 5
samples = generator.generate_multiple_samples(num_samples)
for i, sample in enumerate(samples, start=1):
    print(f"Sample {i}: {sample}")
