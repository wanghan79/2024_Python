import random
import string

class DataGenerator:
    def __init__(self, sample_structure):
        self.sample_structure = sample_structure

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

    def generate_multiple_data_sets(self, num_data_sets):
        for _ in range(num_data_sets):
            generated_data = self.generate_data(self.sample_structure)
            print(generated_data)

# 用户输入的数据结构
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
                    'datarange': (0, 10)  # 假设第二个值是字符串的长度
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
            'datarange': (0, 5)  # 同样，假设第二个值是字符串的长度
        }
    }
}

# 创建数据生成器实例
data_generator = DataGenerator(sample_structure)

# 生成多组随机数据
num_data_sets = 10
data_generator.generate_multiple_data_sets(num_data_sets)
