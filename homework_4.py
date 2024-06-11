import random
import string

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
                    'datarange': (0, 10)  # Assuming the second value is the length of the string
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
            'datarange': (0, 5)  # Again, assuming the second value is the length
        }
    }
}

def generate_data(**kwargs):
    structure = kwargs
    if structure['datatype'] == 'tuple':
        return tuple(generate_data(**sub) for sub in structure['subs'].values())
    elif structure['datatype'] == 'list':
        return [generate_data(**sub) for sub in structure['subs'].values()]
    elif structure['datatype'] == 'set':
        return set(generate_data(**sub) for sub in structure['subs'].values())
    elif structure['datatype'] == 'int':
        return random.randint(*structure['datarange'])
    elif structure['datatype'] == 'float':
        return random.uniform(*structure['datarange'])
    elif structure['datatype'] == 'str':
        return ''.join(random.choices(string.ascii_uppercase, k=structure['datarange'][1]))

def generate_multiple_data(structure, count):
    for _ in range(count):
        yield generate_data(**structure)

def sum_values(data):
    if isinstance(data, (int, float)):
        return data
    elif isinstance(data, (list, tuple, set)):
        return sum(sum_values(item) for item in data)
    return 0

def count_values(data):
    if isinstance(data, (int, float)):
        return 1
    elif isinstance(data, (list, tuple, set)):
        return sum(count_values(item) for item in data)
    return 0

def average_values(data):
    total_sum = sum_values(data)
    total_count = count_values(data)
    if total_count > 0:
        return total_sum / total_count
    else:
        return 0

def ChooseCal(decPara):
    if decPara == "求和":
        def decorator(func):
            def wrapper(*args, **kwargs):
                print("%s is running" % func.__name__)
                if args[0] == "求和":
                    result = sum_values(args[1])
                    print("总和:", result)
                elif args[0] == "求均值":
                    result = average_values(args[1])
                    print("均值:", result)
                elif args[0] == "求和与均值":
                    sum_result = sum_values(args[1])
                    average_result = average_values(args[1])
                    print("总和:", sum_result)
                    print("均值:", average_result)
                elif args[0] == "无":
                    print("没有进行任何计算")
                else:
                    print("无效的计算方式")
                return func(*args, **kwargs)
            return wrapper
    else:
        def decorator(func):
            def wrapper(*args, **kwargs):
                print("%s is running" % func.__name__)
                return func(*args, **kwargs)
            return wrapper
    return decorator

@ChooseCal("求和")
def calculateHK(ways, data):
    print("完毕")

if __name__ == '__main__':
    data_count = int(input("请输入生成数据的数量:\n"))
    ways = input("求什么?\n")
    for generated_data in generate_multiple_data(sample_structure, data_count):
        print(generated_data)
        calculateHK(ways, generated_data)
