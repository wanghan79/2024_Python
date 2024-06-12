import random
import string

def sum_and_average(data):
    if isinstance(data, (int, float)):
        return data, 1  #返回值和计数
    elif isinstance(data, (tuple, list, set)):
        total_sum = 0
        total_count = 0
        for item in data:
            item_sum, item_count = sum_and_average(item)
            total_sum += item_sum
            total_count += item_count
        return total_sum, total_count
    else:
        return 0, 0  # 对于非数值类型，返回0

def sum_values(data):
    if isinstance(data, (int, float)):
        return data  # 返回单个数值
    elif isinstance(data, (tuple, list, set)):
        total_sum = 0
        for item in data:
            total_sum += sum_values(item)  #求和
        return total_sum
    else:
        return 0  

def count_values(data):
    if isinstance(data, (int, float)):
        return 1  
    elif isinstance(data, (tuple, list, set)):
        total_count = 0
        for item in data:
            total_count += count_values(item)  
        return total_count
    else:
        return 0  #非数值类型不计入总数

def average_values(data):
    total_sum = sum_values(data) 
    total_count = count_values(data)  

    if total_count > 0:
        return total_sum / total_count  
    else:
        return 0  #避免除以零的错误

def choose_calculation(calculation_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result_data = func(*args, **kwargs)
            if calculation_type == "求和":
                total_sum = sum_values(result_data)
                print("总和:", total_sum)
            elif calculation_type == "求均值":
                average = average_values(result_data)
                print("均值:", average)
            elif calculation_type == "求和与均值":
                total_sum = sum_values(result_data)
                average = average_values(result_data)
                print("总和:", total_sum)
                print("均值:", average)
            elif calculation_type == "无":
                print("没有进行任何计算")
            else:
                print("无效的计算方式")
            return result_data
        return wrapper
    return decorator

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

    @choose_calculation("求和与均值")
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
    print("生成的数据:", generated_data)

    # 用户输入计算类型
    ways = input("求____.(求和/求均值/求和与均值/无)\n")

    # 重新应用修饰器并生成数据
    rng.generate_data = choose_calculation(ways)(rng.generate_data)
    generated_data = rng.generate_data(sample_structure)
    print("计算后的数据:", generated_data)
