import random
import string

class DataAnalyzer:
    def __init__(self, structure, calculation_method):
        self.structure = structure
        self.calculation_method = calculation_method  # Store the calculation method

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
# yield所在位置
    def generate_multiple_data(self, count):
        for _ in range(count):
            yield self.generate_data()

    def sum_values(self, data):
        if isinstance(data, (int, float)):
            return data
        elif isinstance(data, (list, tuple, set)):
            return sum(self.sum_values(item) for item in data)
        return 0

    def count_values(self, data):
        if isinstance(data, (int, float)):
            return 1
        elif isinstance(data, (list, tuple, set)):
            return sum(self.count_values(item) for item in data)
        return 0

    def average_values(self, data):
        total_sum = self.sum_values(data)
        total_count = self.count_values(data)
        return total_sum / total_count if total_count > 0 else 0

    def calculate(self, data):
        if self.calculation_method == "求和":
            result = self.sum_values(data)
            print("总和:", result)
        elif self.calculation_method == "求均值":
            result = self.average_values(data)
            print("均值:", result)
        elif self.calculation_method == "求和与均值":
            sum_result = self.sum_values(data)
            average_result = self.average_values(data)
            print("总和:", sum_result)
            print("均值:", average_result)
        elif self.calculation_method == "无":
            print("没有进行任何计算")
        else:
            print("无效的计算方式")

# 使用示例
if __name__ == '__main__':
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
    calculation_method = input("请输入计算方式 ('求和', '求均值', '求和与均值', '无'):\n")
    analyzer = DataAnalyzer(sample_structure, calculation_method)
    data_count = int(input("请输入生成数据的数量:\n"))
    for generated_data in analyzer.generate_multiple_data(data_count):
        print(generated_data)
        analyzer.calculate(generated_data)

#
# import random
# import string
#
# class DataAnalyzer:
#     def __init__(self, structure):
#         self.structure = structure
#
#     def generate_data(self, structure=None):
#         if structure is None:
#             structure = self.structure
#         if structure['datatype'] == 'tuple':
#             return tuple(self.generate_data(sub) for sub in structure['subs'].values())
#         elif structure['datatype'] == 'list':
#             return [self.generate_data(sub) for sub in structure['subs'].values()]
#         elif structure['datatype'] == 'set':
#             return set(self.generate_data(sub) for sub in structure['subs'].values())
#         elif structure['datatype'] == 'int':
#             return random.randint(*structure['datarange'])
#         elif structure['datatype'] == 'float':
#             return random.uniform(*structure['datarange'])
#         elif structure['datatype'] == 'str':
#             return ''.join(random.choices(string.ascii_uppercase, k=structure['datarange'][1]))
#
#     def generate_multiple_data(self, count):
#         for _ in range(count):
#             yield self.generate_data()
#
#     def sum_values(self, data):
#         if isinstance(data, (int, float)):
#             return data
#         elif isinstance(data, (list, tuple, set)):
#             return sum(self.sum_values(item) for item in data)
#         return 0
#
#     def count_values(self, data):
#         if isinstance(data, (int, float)):
#             return 1
#         elif isinstance(data, (list, tuple, set)):
#             return sum(self.count_values(item) for item in data)
#         return 0
#
#     def average_values(self, data):
#         total_sum = self.sum_values(data)
#         total_count = self.count_values(data)
#         return total_sum / total_count if total_count > 0 else 0
#
#     def calculate(self, method, data):
#         if method == "求和":
#             result = self.sum_values(data)
#             print("总和:", result)
#         elif method == "求均值":
#             result = self.average_values(data)
#             print("均值:", result)
#         elif method == "求和与均值":
#             sum_result = self.sum_values(data)
#             average_result = self.average_values(data)
#             print("总和:", sum_result)
#             print("均值:", average_result)
#         elif method == "无":
#             print("没有进行任何计算")
#         else:
#             print("无效的计算方式")
#
# # 使用示例
# if __name__ == '__main__':
#     sample_structure = {
#         'datatype': 'tuple',
#         'subs': {
#             'sub1': {
#                 'datatype': 'set',
#                 'subs': {
#                     'sub1': {
#                         'datatype': 'int',
#                         'datarange': (0, 100)
#                     },
#                     'sub2': {
#                         'datatype': 'str',
#                         'datarange': (0, 10)
#                     }
#                 }
#             },
#             'sub2': {
#                 'datatype': 'list',
#                 'subs': {
#                     'sub1': {
#                         'datatype': 'float',
#                         'datarange': (0, 5000)
#                     },
#                     'sub2': {
#                         'datatype': 'int',
#                         'datarange': (1, 200)
#                     }
#                 }
#             },
#             'sub3': {
#                 'datatype': 'str',
#                 'datarange': (0, 5)
#             }
#         }
#     }
#
#     analyzer = DataAnalyzer(sample_structure)
#     data_count = int(input("请输入生成数据的数量:\n"))
#     for generated_data in analyzer.generate_multiple_data(data_count):
#         print(generated_data)
#         method = input("求什么? ('求和', '求均值', '求和与均值', '无'): ")
#         analyzer.calculate(method, generated_data)
