import random

def generate_random_dict(num):
    result = {}
    for i in range(num):
        key = f"key_{i}"
        value = random.randint(1, 100)
        result[key] = value
    return result

random_dict = generate_random_dict(5)
print(random_dict)
