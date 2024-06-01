from functools import wraps
import random
import time

class RandomDataGenerator:
    def __init__(self):
        pass

    # use_logging decorator remains unchanged

    def get_element(self, data, out_list=None):
        if out_list is None:
            out_list = []
        for item in data:
            if isinstance(item, (int, float)):
                out_list.append(item)
            elif isinstance(item, (list, set, tuple)):
                self.get_element(item, out_list)
        return out_list

    def calculate_sum_and_average(self, func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            sum_ = 0
            count = 0
            for item in func(self, *args, **kwargs):
                if isinstance(item, (int, float)):
                    sum_ += item
                    count += 1
            average = sum_ / count if count != 0 else 0
            print(f"Sum: {sum_}, Average: {average}")
            return item  # Return the last item for consistency with generator
        return wrapper

    def get_random(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'tuple':
                yield tuple(self.get_random(**value))
            elif key == 'list':
                yield list(self.get_random(**value))
            elif key == 'set':
                yield set(self.get_random(**value))
            elif key == 'int':
                a, b = (value['datarange'] if 'datarange' in value else (1, 10))
                yield random.randint(a, b)
            elif key == 'float':
                a, b = (value['datarange'] if 'datarange' in value else (1.0, 10.0))
                yield random.uniform(a, b)
            elif key == 'str':
                datarange = value.get("datarange", "abcdef")
                datalength = value.get("datalength", 5)
                yield ''.join(random.choice(datarange) for _ in range(datalength))
            else:
                print("This is an undefined type")
                yield "********"

    @calculate_sum_and_average
    def get_random_(self, **kwargs):
        for item in self.get_random(**kwargs):
            print(item)

# __name__ == "__main__" block remains unchanged