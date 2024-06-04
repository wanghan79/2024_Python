# 在之前的基础上加上修饰器
import random
import string
#求和，求均值，求两者或者什么都不干的修饰

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
    structure=kwargs
    if structure['datatype'] == 'tuple':
        return tuple(generate_data(**sub) for sub in structure['subs'].values())
    elif structure['datatype'] == 'list':
        return [generate_data(**sub) for sub in structure['subs'].values()]
    elif structure['datatype'] == 'set':
        return [generate_data(**sub) for sub in structure['subs'].values()]
    elif structure['datatype'] == 'int':
        return random.randint(*structure['datarange'])
    elif structure['datatype'] == 'float':
        return random.uniform(*structure['datarange'])
    elif structure['datatype'] == 'str':
        return ''.join(random.choices(string.ascii_uppercase, k=structure['datarange'][1]))
# GPT生成
def sum_and_average(data):
    if isinstance(data, (int, float)):
        return data, 1  # 返回值和计数
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
            total_sum += sum_values(item)  # 递归求和
        return total_sum
    else:
        return 0  # 对于非数值类型，返回0
def count_values(data):
    if isinstance(data, (int, float)):
        return 1  # 数值类型计数为1
    elif isinstance(data, (tuple, list, set)):
        total_count = 0
        for item in data:
            total_count += count_values(item)  # 递归计算数值总数
        return total_count
    else:
        return 0  # 非数值类型不计入总数
def average_values(data):
    total_sum = sum_values(data)  # 使用sum_values函数获取总和
    total_count = count_values(data)  # 单独计算数据中数值的总数

    if total_count > 0:
        return total_sum / total_count  # 计算平均值
    else:
        return 0  # 避免除以零的错误
def ChooseCal(decPara):
    if (decPara == "求和"):
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
                return func(*args,**kwargs)
            return wrapper # = wrapper  (*args,**kwargs)
    else:
        def decorator(func):
            def wrapper(*args, **kwargs):
                print("%s is running" % func.__name__)
                return func(*args,**kwargs)
            return wrapper# = wrapper  (*args,**kwargs)
    return decorator

@ChooseCal("求和")
def calculateHK(ways,data):
    print("完毕")
if __name__ == '__main__':
    generated_data = generate_data(**sample_structure)
    print(generated_data)
    ways = input("求什么?\n")
    calculateHK(ways,generated_data)


# # 计算总和和均值
# total_sum, total_count = sum_and_average(generated_data)
# print("Total Sum:", total_sum)
# print("Average:", total_sum / total_count if total_count else 0)