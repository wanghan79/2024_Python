import random

class Sampling:
    @staticmethod
    def getRandom(**kwargs):
        result = []
        for key, value in kwargs.items():
            if key == 'int':
                a, b = value['datarange']
                result.append(random.randint(a, b))
            elif key == 'float':
                a, b = value['datarange']
                result.append(random.uniform(a, b))
            elif key == 'str':
                result.append(''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len'])))
            elif key == 'tuple':
                result.append(tuple(Sampling.getRandom(**value)))
            elif key == 'list':
                result.append(list(Sampling.getRandom(**value)))
            elif key == 'set':
                result.append(set(Sampling.getRandom(**value)))
        return result

    @staticmethod
    def calculate(data, operation='None'):
        int_float_values = []
        for value in data:
            if isinstance(value, int) or isinstance(value, float):
                int_float_values.append(value)
            elif isinstance(value, list) or isinstance(value, tuple) or isinstance(value, set):
                Sampling.calculate(value, operation)
        if not int_float_values:
            return 0
        total = sum(int_float_values)
        average = total / len(int_float_values) if len(int_float_values) > 0 else 0
        if operation == 'sum':
            return total
        elif operation == 'average':
            return average
        elif operation == 'both':
            answer = {'sum': total, 'average': average}
            return answer
        else:
            return None

    @staticmethod
    def decorator(cal_func):
        def wrapper(operation, *args, **kwargs):
            new_data = Sampling.getRandom(**Sampling.my_dict)
            print(f"生成的随机数的结构是：")
            print(new_data)
            return cal_func(new_data, operation, *args)
        return wrapper

    my_dict = {
        'num': 4,
        'int': {'datarange': (5, 10)},
        'float': {'datarange': (0, 100.0)},
        'str': {'datarange': 'avbshcmg', 'len': 10},
        'list': {'int': {'datarange': (0, 10)},
                 'list': {'str': {'datarange': 'abcde', 'len': 4},
                          'float': {'datarange': (10.2, 29.3)}
                          },
                 'tuple': {'float': {'datarange': (0, 1)},
                           'int': {'datarange': (5, 7)}
                           }
                 }
    }

@Sampling.decorator
def calculate(data, operation='None'):
    return Sampling.calculate(data, operation)

for i in range(Sampling.my_dict['num']):
    output = calculate('both')
    print("两个都求:")
    print(output)
# 只需要修改calculate的参数即可实现求什么。当是both时，两者都求，当是sum时，只求sum，当是average时只求average，其他都是两者都不求