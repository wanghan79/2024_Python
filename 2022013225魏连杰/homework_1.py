import random
import string


def generate_data(structure, count=1):
    def generate_single_data(**kwargs):
        structure = kwargs
        if structure['datatype'] == 'tuple':
            return tuple(generate_single_data(**sub) for sub in structure['subs'].values())
        elif structure['datatype'] == 'list':
            return [generate_single_data(**sub) for sub in structure['subs'].values()]
        elif structure['datatype'] == 'set':
            return {generate_single_data(**sub) for sub in structure['subs'].values()}
        elif structure['datatype'] == 'int':
            return random.randint(*structure['datarange'])
        elif structure['datatype'] == 'float':
            return random.uniform(*structure['datarange'])
        elif structure['datatype'] == 'str':
            return ''.join(random.choices(string.ascii_uppercase, k=structure['datarange'][1]))

    return [generate_single_data(**structure) for _ in range(count)]


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

# 用户输入生成结构的数量
count = int(input("请输入要生成的数据结构数量："))

generated_data = generate_data(sample_structure, count=count)
for data in generated_data:
    print(data)
