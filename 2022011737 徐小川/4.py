import random
import string

def generate_data(structure):
    if structure['datatype'] == 'tuple':
        for sub in structure['subs'].values():
            yield tuple(generate_data(sub))
    elif structure['datatype'] == 'list':
        for sub in structure['subs'].values():
            yield list(generate_data(sub))
    elif structure['datatype'] == 'int':
        yield random.randint(*structure['datarange'])
    elif structure['datatype'] == 'float':
        yield random.uniform(*structure['datarange'])
    elif structure['datatype'] == 'str':
        length = random.randint(*structure['datarange'])
        yield ''.join(random.choices(string.ascii_uppercase, k=length))


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

# 生成多组随机数据
num_data_sets = 8
for _ in range(num_data_sets):
    generated_data = list(generate_data(sample_structure))
    print(generated_data)