import random
import string

class RandomGenerator:
    def __init__(self, seed=None):
        if seed is not None:
            random.seed(seed)

    def generate_random_variable(self, datatype, datarange):
        if datatype == 'int':
            return self.random_integer(datarange)
        elif datatype == 'float':
            return self.random_float(datarange)
        elif datatype == 'str':
            return self.random_string(datarange)
        else:
            raise ValueError("不支持类型")

    def random_integer(self, datarange):
        return random.randint(*datarange)

    def random_float(self, datarange):
        return random.uniform(*datarange)

    def random_string(self, datarange):
        length = datarange[1]
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def generate_data(self, structure):
        if structure['datatype'] == 'tuple':
            return tuple(self.generate_data(sub) for sub in structure['subs'].values())
        elif structure['datatype'] == 'list':
            return [self.generate_data(sub) for sub in structure['subs'].values()]
        elif structure['datatype'] == 'set':
            return {self.generate_data(sub) for sub in structure['subs'].values()}
        elif structure['datatype'] in ['int', 'float', 'str']:
            return self.generate_random_variable(structure['datatype'], structure['datarange'])
        else:
            raise ValueError("不支持的类型")

if __name__ == "__main__":
    rng = RandomGenerator(seed=42)

    sample_structure = {
        'datatype': 'tuple',
        'subs': {
            'sub1': {
                'datatype': 'set',
                'subs': {
                    'sub1': {
                        'datatype': 'int',
                        'datarange': (0, 100)
                    },
                    'sub2': {
                        'datatype': 'str',
                        'datarange': (0, 10)
                    }
                }
            },
            'sub2': {
                'datatype': 'list',
                'subs': {
                    'sub1': {
                        'datatype': 'float',
                        'datarange': (0, 5000)
                    },
                    'sub2': {
                        'datatype': 'int',
                        'datarange': (1, 200)
                    }
                }
            },
            'sub3': {
                'datatype': 'str',
                'datarange': (0, 5)
            }
        }
    }

    generated_data = rng.generate_data(sample_structure)
    print(generated_data)
