from functools import wraps
import random
import time

class RandomDataGenerator:
    def __init__(self):
        pass

    def use_logging(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            print('-------------------------------------------------')
            start_time = time.time()  # 获取开始时间
            print(f"Logging: The function {func.__name__} is running")
            print(f"Time: {time.strftime('%X', time.localtime())}")
            result = func(self, *args, **kwargs)
            end_time = time.time()  # 获取结束时间
            print(f"Logging: The function {func.__name__} has ended")
            print(f"Time: {time.strftime('%X', time.localtime())}")
            print(f"Execution time: {end_time - start_time:.6f} seconds")
            print('-------------------------------------------------')
            return result
        return wrapper




    def get_random(self, **kwargs):
        # Modified to be a generator function using yield
        for key, value in kwargs.items():
            if key == 'tuple':
                for item in self.get_random(**value):
                    yield item
            elif key == 'list':
                for item in self.get_random(**value):
                    yield item
            elif key == 'set':
                for item in self.get_random(**value):
                    yield item
            elif key == 'int':
                a, b = value['datarange']
                yield random.randint(a, b)
            elif key == 'float':
                a, b = value['datarange']
                yield random.uniform(a, b)
            elif key == 'str':
                datarange = value["datarange"]
                datalength = value["datalength"]
                yield ''.join(random.choice(datarange) for _ in range(datalength))
            else:
                print("This is an undefined type")
                yield "********"

    def get_element(self, data):
        out_list = []
        for item in data:
            if isinstance(item, (int, float)):
                out_list.append(item)
            elif isinstance(item, (list, set, tuple)):
                self.get_element(item, out_list)  # Pass the out_list to be filled
        return out_list

    @use_logging
    def get_random_(self, **kwargs):
        number_list = []
        sum = 0
        for item in self.get_random(**kwargs):
            print(item)  # Print each generated random number
            if isinstance(item, (int, float)):
                number_list.append(item)
                sum += item
        count = len(number_list)
        average = sum / count if count != 0 else 0
        print(f"Sum: {sum}, Average: {average}")
if __name__ == "__main__":
    gen = RandomDataGenerator()
    my_dict = {'tuple': {'int': {'datarange': [1, 10]},
                         'list': {
                             'int': {'datarange': [1, 10]},
                             'float': {'datarange': [1, 10]},
                             'str': {'datarange': "gfzxcv", "datalength": 6},
                             'tuple': {'str': {'datarange': "gfzxcv", "datalength": 6}}
                         }}}
    gen.get_random_(**my_dict)
