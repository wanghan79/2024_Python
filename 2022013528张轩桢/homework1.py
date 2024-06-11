import random
import string


def generate_structure(**kwargs):
    if 'datatype' not in kwargs:
        raise ValueError("数据结构定义中缺少'datatype'字段")

    datatype = kwargs['datatype']
    subs = kwargs.get('subs', None)

    if datatype == 'int':
        return random.randint(*kwargs['datarange'])
    elif datatype == 'float':
        return round(random.uniform(*kwargs['datarange']), 2)
    elif datatype == 'str':
        length = random.randint(*kwargs['datarange'])
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    elif datatype == 'list':
        return [generate_structure(**sub) for sub in subs.values()]
    elif datatype == 'tuple':
        return tuple(generate_structure(**sub) for sub in subs.values())
    else:
        raise ValueError(f"不支持的数据类型: {datatype}")



def main():
    n = int(input("请输入要生成的随机数据结构的数量："))
    for i in range(n):
        data_structure = {
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
                            'datarange': (1, 10)
                        }
                    }
                },
                'sub2': {
                    'datatype': 'tuple',
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
                    'datarange': (1, 5)
                }
            }
        }
        random_data = generate_structure(**data_structure)
        print(f"随机数据结构{i + 1}:", random_data)

if __name__ == "__main__":
    main()
