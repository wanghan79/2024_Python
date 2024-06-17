import random


def dataSampling_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        int_values = [value for value in result.values() if isinstance(value, int)]
        print(f"Sum of int values: {sum(int_values)}")
        print(f"Average of int values: {sum(int_values) / len(int_values)}")
        return result
    return wrapper

@dataSampling_decorator
def generate_random_dict(num):
    result = {}
    for i in range(num):
        key = f"key_{i}"
        value = random.randint(1, 100)
        result[key] = value
    return result

random_dict = generate_random_dict(5)
print(random_dict)