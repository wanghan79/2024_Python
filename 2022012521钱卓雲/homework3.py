from functools import wraps
import random
import time

class RandomDataGenerator:
    def __init__(self):
        pass

    def use_Calculate(func):
        print('-------------------------------------------------')
        start_time = time.time()  # 获取开始时间
        print(f"Logging: The function {func.__name__} is running")
        print(f"Time: {time.strftime('%X', time.localtime())}")
        @wraps(func)
        def wrapper(self, *args, **kwargs):

            result = None
            #result = func(self, *args, **kwargs)
            data_ = self.get_random(**kwargs)
            print(data_)
            number_list = self.get_element(data_, None)
            cont_number = len(number_list)
            sum = 0
            average = 0
            for num in number_list:
                sum += num
            if cont_number != 0:
                average = sum / cont_number
            print(f"Sum: {sum}, Average: {average}")

            end_time = time.time()  # 获取结束时间
            print(f"Logging: The function {func.__name__} has ended")
            print(f"Time: {time.strftime('%X', time.localtime())}")
            print(f"Execution time: {end_time - start_time:.6f} seconds")
            print('-------------------------------------------------')
            return result
        return wrapper


    def get_element(self, data, out_list = None):
        if(out_list == None):
            out_list = []
        for item in data:
            if isinstance(item, (int, float)):
                out_list.append(item)
            elif isinstance(item, (list, set, tuple)):
                self.get_element(item, out_list=out_list)
        return out_list

    def calculate_sum_and_average(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            data_ = self.get_random(**kwargs)
            number_list = self.get_element(data_, None)
            cont_number = len(number_list)
            sum = 0
            average = 0
            for num in number_list:
                sum += num
            if cont_number != 0:
                average = sum/cont_number
            print(f"Sum: {sum}, Average: {average}")
            return result
        return wrapper

    def get_random(self, **kwargs):
        result = []
        for key, value in kwargs.items():
            if key == 'tuple':
                result.append(tuple(self.get_random(**value)))
            elif key == 'list':
                result.append(list(self.get_random(**value)))
            elif key == 'set':
                result.append(set(self.get_random(**value)))
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

    @use_Calculate
    def get_random_(self, **kwargs):
        print(self.get_random(**kwargs))

if __name__ == "__main__":
    gen = RandomDataGenerator()
    my_dict = {'tuple': {'int': {'datarange': [1, 10]},
                         'list': {
                             'int': {'datarange': [1, 10]},
                             'float': {'datarange': [1, 10]},
                             'str': {'datarange': "gfzxcv", "datalength": 6},
                             'tuple': {'str': {'datarange': "gfzxcv", "datalength": 6}},
                             'tuple': {'int': {'datarange': [1, 10]},
                                       'list': {
                                           'int': {'datarange': [1, 10]},
                                           'float': {'datarange': [1, 10]},
                                           'str': {'datarange': "gfzxcv", "datalength": 6},
                                           'tuple': {'str': {'datarange': "gfzxcv", "datalength": 6}}
                                       }}
                         }}
               }
    gen.get_random_(**my_dict)
