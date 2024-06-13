import random
import functools
import statistics

def calculate_stats(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        numbers = func(*args, **kwargs)
        mean = statistics.mean(numbers)
        variance = statistics.variance(numbers)
        print("mean:", mean)
        print("v:", variance)
        return numbers
    return wrapper

def generate_random_ints(num, it):
    return [random.randint(next(it, 0), next(it, 100)) for _ in range(num)]

def generate_random_floats(num, it):
    return [random.uniform(next(it, 0.0), next(it, 100.0)) for _ in range(num)]

@calculate_stats
def generate_random_ints_with_bounds(num, it):
    return generate_random_ints(num, it)

@calculate_stats
def generate_random_floats_with_bounds(num, it):
    return generate_random_floats(num, it)

it = iter([0, 100])
random_integers = generate_random_ints_with_bounds(10, it)
print(random_integers)

it = iter([0.0, 100.0])
random_floats = generate_random_floats_with_bounds(10, it)
print(random_floats)
