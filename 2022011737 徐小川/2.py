import random
import string

class DataGenerator:
    def __init__(self):
        pass

    def generate_data(self, structure):
        if structure['datatype'] == 'tuple':
            sub_data = [self.generate_data(sub) for sub in structure['subs'].values()]
            return tuple(sub_data)
        elif structure['datatype'] == 'list':
            sub_data = [self.generate_data(sub) for sub in structure['subs'].values()]
            return sub_data
        elif structure['datatype'] == 'int':
            return random.randint(*structure['datarange'])
        elif structure['datatype'] == 'float':
            return random.uniform(*structure['datarange'])
        elif structure['datatype'] == 'str':
            length = random.randint(*structure['datarange'])
            return ''.join(random.choices(string.ascii_uppercase, k=length))

# 示例结构
sample_structure = {
    'datatype': 'tuple',
    'subs': {
        'sub1': {
            'datatype': 'list',
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

# 生成器实例化
generator = DataGenerator()

# 生成多组随机数据
num_data_sets = 8
for _ in range(num_data_sets):
    generated_data = generator.generate_data(sample_structure)
    print(generated_data)