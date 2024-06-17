import random
import string

def random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_random_dict_generator(num, depth=1, max_depth=3):
    if depth > max_depth:
        yield random.randint(1, 100)
    else:
        for _ in range(num):
            key = random_string()
            value = next(generate_random_dict_generator(num, depth + 1, max_depth))
            yield (key, value)

random_dict_gen = generate_random_dict_generator(5, 1, 2)
random_dict = dict(random_dict_gen)
print("Random Dictionary from Generator:", random_dict)