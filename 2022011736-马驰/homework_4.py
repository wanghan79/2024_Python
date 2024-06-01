import random
import string
from collections import defaultdict

# 创建一个装饰器，用于计数数据类型
def count_data_types(func):
    def wrapper(self, structure, *args, **kwargs):
        result = func(self, structure)
        # 更新计数器
        if structure['datatype'] == 'tuple' or structure['datatype'] == 'list':
            # 递归计数内部数据类型
            for item in result:
                self.count_data_types(item, *args, **kwargs)
        else:
            # 直接计数基本数据类型
            self.count[structure['datatype']] += 1
        return result
    return wrapper

class RandomDataGenerator:
    def __init__(self, data_structure):
        self.data_structure = data_structure
        self.count = defaultdict(int)  # 初始化计数器

    @count_data_types
    def generate_data(self, structure):
        # 根据数据结构字典中的 datatype 来决定如何生成数据
        if structure['datatype'] == 'tuple':
            sub_data = tuple(self.generate_data(sub) for sub in structure['subs'].values())
            return sub_data
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

    def count_data_types(self, data):
        # 递归计数数据类型
        if isinstance(data, (tuple, list)):
            for item in data:
                self.count_data_types(item)
        else:
            self.count[type(data).__name__] += 1

    def generate_multiple(self, num_data_sets):
        for _ in range(num_data_sets):
            yield self.generate_data(self.data_structure)

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
                    'datarange': (1, 100)
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
            'datarange': (1, 10)
        }
    }
}

# 创建一个生成器实例
generator = RandomDataGenerator(sample_structure)

# 生成多组随机数据
num_data_sets = 100
generated_data_sets = list(generator.generate_multiple(num_data_sets))

# 打印生成的数据和计数结果
for data_set in generated_data_sets:
    print(data_set)
print("Data type counts:", dict(generator.count))
