import random
from collections import deque

class DataAnalyzer(object):

    def dataSamping(self, **kwargs):
        result = []
        for key, value in kwargs.items():
            if key == 'int':
                a, b = value['datarange']
                result.append(random.randint(a, b))
            elif key == 'float':
                a, b = value['datarange']
                result.append(random.uniform(a, b))
            elif key == 'str':
                datarange = value['datarange']
                datalength = value['datalength']
                result.append(''.join(random.choice(datarange)for _ in range(datalength)))
            elif key == 'tuple':
                result.append(tuple(self.dataSamping(**value)))
            elif key == 'set':
                result.append(set(self.dataSamping(**value)))
            elif key == 'list':
                result.append(list(self.dataSamping(**value)))
        return result

    def analysis(self, data_dict, analysis_type):
        total = 0
        count = 0
        if analysis_type == 'sum_float' or analysis_type =='average_float' or analysis_type =='both_float':
            float_values = []
            queue = deque(data_dict)
            while queue:
                val = queue.popleft()
                if isinstance(val, float):
                    float_values.append(val)
                elif isinstance(val, (list, tuple, set)):
                    queue.extend(val)
            if float_values:
                total = sum(float_values)
                count = len(float_values)
            if(analysis_type == 'sum_float'):
                print("Total Sum of 'float' Values in Random Data:", total)
            elif analysis_type == 'average_float':
                print("Average of 'float' Values in Random Data:", total / count)
            elif analysis_type == 'both_float':
                print("Total Sum of 'float' Values in Random Data:", total)
                print("Average of 'float' Values in Random Data:", total / count)

        elif analysis_type == 'average_int' or analysis_type =='sum_int' or analysis_type =='both_int':
            int_values = []
            queue = deque(data_dict)
            while queue:
                val = queue.popleft()
                if isinstance(val, int):
                    int_values.append(val)
                elif isinstance(val, (list, tuple, set)):
                    queue.extend(val)
            if int_values:
                total = sum(int_values)
                count = len(int_values)
            if analysis_type == 'average_int':
                print("Average of 'int' Values in Random Data:", total / count)
            elif analysis_type == 'sum_int':
                print("Total Sum of 'int' Values in Random Data:", total)
            elif analysis_type == 'both_int':
                print("Total Sum of 'int' Values in Random Data:", total)
                print("Average of 'int' Values in Random Data:", total / count)
        elif analysis_type == 'none':
            print("没有进行任何操作")
        else:
            print("无效的计算方式")

# 示例用法
my_dict = {'tuple': {'int': {'datarange': [1, 10]},
                         'list': {
                             'int': {'datarange': [1, 10]},
                             'float': {'datarange': [1, 10]},
                             'str': {'datarange': "gfzxcv", "datalength": 6},
                             'tuple': {'str': {'datarange': "gfzxcv", "datalength": 6},
                                       'int': {'datarange': [1, 100]}}
                         },
                         'set': {
                             'int': {'datarange': [1, 10]},
                             'float': {'datarange': [1, 10]},
                             'str': {'datarange': "gfzxcv", "datalength": 6}
                         }
                         },
               'int': {'datarange':[1,100]}
               }

data_analyzer = DataAnalyzer()
num = int(input("请输入一个整数num,表示想要生成的字典数目: \n")) # 指定生成的字典数量
for i in range(1, num + 1):
    data_values = data_analyzer.dataSamping(**my_dict)
    print("\nGenerated Data", i, ":")
    print(data_values)
    operation = input("请输入想对字典进行的操作(如：'sum_int' or 'average_float' or 'both_int' or 'none'):\n")
    print("Analysis Result:")
    data_analyzer.analysis(data_values, operation)

