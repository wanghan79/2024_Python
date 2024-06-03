
import random

def Sat(*args):
    def decorator(sample_analysis):
        def wrapper(data, operation):
            total_sum_int = 0
            total_sum_float = 0
            count_int= 0
            count_float= 0
            stack = [data]  # 使用栈来迭代处理数据
            while stack:
                current_data = stack.pop()
                if isinstance(current_data, list) or isinstance(current_data, tuple):
                    for item in current_data:
                        stack.append(item)
                elif isinstance(current_data, int):
                    total_sum_int += current_data
                    count_int += 1
                elif isinstance(current_data, float):
                    total_sum_float += current_data
                    count_float += 1

            if operation == 'int_sum':
                return total_sum_int  # 求整型int总和
            elif operation == 'float_sum':
                return total_sum_float   # 求浮点型float总和

            elif operation == 'int_average':
                if count_int == 0:
                    return 0
                else:
                    return total_sum_int / count_int
            elif operation == 'float_average':
                if count_float == 0:
                    return 0
                else:
                    return total_sum_float / count_float
            # return sample_analysis(*args, **kwargs)
        return wrapper
    return decorator


class ClassTest(object):
    my_dict = {
        'tuple': {
            'int': {
                'datarange': [1, 10]
            },
            'float': {
                'datarange': [100, 1000]
            },
            'list': {
                'int': {
                    'datarange': [1, 50]
                },
                'float': {
                    'datarange': [1, 10]
                },
                'str': {
                    'datarange': "abcefghijklmnopqrstuvwxyz",
                    "datalength": 6
                },
                'tuple': {
                    'str': {
                        'datarange': "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                        "datalength": 6
                    }
                }
            }
        }
    }

    @staticmethod
    def get_random(**kwargs):
        result = []
        for key, value in kwargs.items():
            if key == 'tuple':
                result.append(tuple(ClassTest.get_random(**value)))
            elif key == 'list':
                result.append(list(ClassTest.get_random(**value)))
            elif key == 'set':
                result.append(set(ClassTest.get_random(**value)))
            elif key == 'int':
                a, b = value['datarange']
                result.append(random.randint(a, b))
            elif key == 'float':
                a, b = value['datarange']
                result.append(random.uniform(a, b))
            elif key == 'str':
                datarange = value["datarange"]
                datalength = value["datalength"]
                result.append(''.join(random.choice(datarange) for _ in range(datalength)))
            else:
                print("This is an undefined type")
                result.append("********")
        return result

    @staticmethod
    def getSample(*args,**kwargs):
        dc = dict()
        for k, v in kwargs.items():
            if k == 'num':
                num = v
            else:
                dc[k] = v
        result = ClassTest.get_random(**dc)
        return result

    @Sat()
    @staticmethod
    def sample_analysis(data, operation):
        print("========Above is the results of sample analysing in this round========")
        return data

if __name__ == '__main__':
    N = 5
    test = ClassTest()
    for i in range(N):
        result_data = test.getSample(**ClassTest.my_dict)
        print("Generated Random Data", i+1, ":")
        print(result_data)

        total_sum = ClassTest.sample_analysis(result_data, 'int_sum')  # 求int和操作
        print("Total Sum of 'int' Values in Random Data:",total_sum)

        average = ClassTest.sample_analysis(result_data, 'int_average')  # 求int平均操作
        print("Average of 'int' Values in Random Data:",average)

        total_sum = ClassTest.sample_analysis(result_data, 'float_sum')  # 求float和操作
        print("Total Sum of 'float' Values in Random Data:", total_sum)

        average = ClassTest.sample_analysis(result_data, 'float_average')  # 求float平均操作
        print("Average of 'float' Values in Random Data:", average)
        print('\n')