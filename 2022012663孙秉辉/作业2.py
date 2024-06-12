import random

class Sampling:
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
                result.append(''.join(random.SystemRandom().choice(value['datarange'])for _ in range(value['len'])))
            elif key == 'tuple':
                result.append(tuple(Sampling.getRandom(**value)))
            elif key == 'list':
                result.append(list(Sampling.getRandom(**value)))
            elif key == 'set':
                result.append(set(Sampling.getRandom(**value)))
        return result

    def calculate(data, *args):
        int_float_values = []
        for value in data:
            if isinstance(value, int) or isinstance(value, float):
                int_float_values.append(value)
            elif isinstance(value, list) or isinstance(value, tuple) or isinstance(value, set):
                Sampling.calculate(value)
        if not int_float_values:
            return 0
        total = sum(int_float_values)
        average = total/len(int_float_values)
        answer = {}
        if  'cal_sum' in args:
            answer['sum'] = total
        else:
            answer['sum'] = 'None'
        if 'cal_average' in args:
            answer['average'] = average
        else:
            answer['average'] = 'None'
        return answer


    my_dict = {
        'num': 4,
        'int': {'datarange': (5, 10)},
        'float': {'datarange': (0, 100.0)},
        'str': {'datarange': 'avbshcmg', 'len': 10},
        'list': {'int': {'datarange': (0, 10)},
                'list': {'str': {'datarange': 'abcde','len': 4},
                        'float': {'datarange': (10.2, 29.3)}
                        },
                'tuple': {'float': {'datarange': (0, 1)},
                        'int': {'datarange': (5, 7)}
                        }
                }
    }

for i in range(Sampling.my_dict['num']):
    new_data = Sampling.getRandom(**Sampling.my_dict)
    print(f"生成的随机数的结构是：")
    print(new_data)
    output = Sampling.calculate(new_data, 'cal_sum','cal_average')
    print("sum和average都求:")
    print(output)
    output = Sampling.calculate(new_data, 'cal_average')
    print("只求average:")
    print(output)
    output = Sampling.calculate(new_data, 'cal_sum')
    print("只求sum:")
    print(output)
    output = Sampling.calculate(new_data)
    print("两个都不求:")
    print(output)
    print("*************************")






