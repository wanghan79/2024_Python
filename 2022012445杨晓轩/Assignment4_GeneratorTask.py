import random

def Sat(*args):
    def decorator(func):
        def wrapper(data, operation):
            total_int = 0
            count_int = 0
            total_float = 0
            count_float = 0

            stack = [data]  # 使用栈来迭代处理数据
            while stack:
                current_data = stack.pop()
                if isinstance(current_data, list) or isinstance(current_data, tuple) or isinstance(current_data, set):
                    for item in current_data:
                        stack.append(item)
                elif isinstance(current_data, int):
                    total_int += current_data
                    count_int += 1
                elif isinstance(current_data, float):
                    total_float += current_data
                    count_float += 1

            if operation == 'sum_int':  # 求和
                print("Total Sum of 'int' Values in Random Data:", total_int)
            elif operation == 'average_int':  # 求平均
                if count_int == 0:
                    print("Average of 'int' Values in Random Data:", 0)
                print("Average of 'int' Values in Random Data:", total_int / count_int)
            elif operation == 'both_int':
                if count_int == 0:
                    total_int = 0
                print("Total Sum of 'int' Values in Random Data:", total_int)
                print("Average of 'int' Values in Random Data:", total_int / count_int)
            elif operation == 'sum_float':  # 求和
                print("Total Sum of 'float' Values in Random Data:", total_float)
            elif operation == 'average_float':  # 求平均
                if count_float == 0:
                    print("Average of 'float' Values in Random Data:", 0)
                print("Average of 'float' Values in Random Data:", total_float / count_float)
            elif operation == 'both_float':
                if count_float == 0:
                    total_float = 0
                print("Total Sum of 'float' Values in Random Data:", total_float)
                print("Average of 'float' Values in Random Data:", total_float / count_float)
            elif operation == 'none':
                print("没有进行任何操作")
            else:
                print("无效的计算方式")

            return func(data, operation)
        return wrapper
    return decorator

def dataSamping(**kwargs):
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
            result.append(''.join(random.choice(datarange) for _ in range(datalength)))
        elif key == 'tuple':
            result.append(tuple(dataSamping(**value)))
        elif key == 'set':
            result.append(set(dataSamping(**value)))
        elif key == 'list':
            result.append(list(dataSamping(**value)))
    return result

@Sat()
def compute_operation(data, operation):
    print("这是一次分析结果")

def generate_structures(**kwargs): #生成器
    for key, value in kwargs.items():
        yield dataSamping(**my_dict)

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
               'int': {'datarange': [1, 10]}
               }

if __name__ == '__main__':
    n = int(input("请输入一个整数num,表示想要生成的字典数目: \n"))
    for i in range(1, n + 1):
        print("\nGenerated data", i, ":")
        data = generate_structures(**my_dict)
        dataresult = next(data)
        print(dataresult)
        operation = input("请输入想对字典进行的操作(如：'sum_int'、'average_float'、'none'):\n")
        compute_operation(dataresult, operation)

