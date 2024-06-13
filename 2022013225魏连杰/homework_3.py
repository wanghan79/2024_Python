import random
import string


class DataProcessor:
    def __init__(self, structure):
        self.structure = structure

    def generate_data(self, structure=None):
        if structure is None:
            structure = self.structure
        if structure['datatype'] == 'tuple':
            return tuple(self.generate_data(sub) for sub in structure['subs'].values())
        elif structure['datatype'] == 'list':
            return [self.generate_data(sub) for sub in structure['subs'].values()]
        elif structure['datatype'] == 'set':
            return set(self.generate_data(sub) for sub in structure['subs'].values())
        elif structure['datatype'] == 'int':
            return random.randint(*structure['datarange'])
        elif structure['datatype'] == 'float':
            return random.uniform(*structure['datarange'])
        elif structure['datatype'] == 'str':
            return ''.join(random.choices(string.ascii_uppercase, k=structure['datarange'][1]))

    def sum_values(self, data):
        if isinstance(data, (int, float)):
            return data
        elif isinstance(data, (tuple, list, set)):
            return sum(self.sum_values(item) for item in data)
        else:
            return 0

    def count_values(self, data):
        if isinstance(data, (int, float)):
            return 1
        elif isinstance(data, (tuple, list, set)):
            return sum(self.count_values(item) for item in data)
        else:
            return 0

    def average_values(self, data):
        total_sum = self.sum_values(data)
        total_count = self.count_values(data)
        return total_sum / total_count if total_count > 0 else 0

    def choose_cal(self, decPara):
        def decorator(func):
            def wrapper(data):
                print("%s is running" % func.__name__)
                if decPara == "求和":
                    result = self.sum_values(data)
                    print("总和:", result)
                elif decPara == "求均值":
                    result = self.average_values(data)
                    print("均值:", result)
                elif decPara == "求和与均值":
                    sum_result = self.sum_values(data)
                    average_result = self.average_values(data)
                    print("总和:", sum_result)
                    print("均值:", average_result)
                elif decPara == "无":
                    print("没有进行任何计算")
                else:
                    print("无效的计算方式")
                func(data)

            return wrapper

        return decorator

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
if __name__ == '__main__':

    processor = DataProcessor(sample_structure)
    generated_data = processor.generate_data()
    print(generated_data)
    ways = input("求什么? ('求和', '求均值', '求和与均值', '无'): ")
    @processor.choose_cal(ways)
    def calculate(data):
        print("计算完成")
    calculate(generated_data)
