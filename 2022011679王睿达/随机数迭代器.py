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


def generate_random_ints(num, start, end):
    return [random.randint(start, end) for _ in range(num)]


def generate_random_floats(num, start, end):
    return [random.uniform(start, end) for _ in range(num)]


@calculate_stats
def generate_random_ints_with_bounds(num, start, end):
    return generate_random_ints(num, start, end)


@calculate_stats
def generate_random_floats_with_bounds(num, start, end):
    return generate_random_floats(num, start, end)


class RangeIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration



it_int = RangeIterator(0, 100)
random_integers = generate_random_ints_with_bounds(10, next(it_int), next(it_int))
print(random_integers)

it_float = RangeIterator(0, 100)
random_floats = generate_random_floats_with_bounds(10, next(it_float), next(it_float))
print(random_floats)
