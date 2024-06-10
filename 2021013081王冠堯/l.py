import random
import string

class RandomGenerator:
    def __init__(self, seed=None):
        random.seed(seed)

    def generate_random_variable(self, data_types):
        data_type = random.choice(data_types)
        generator = {
            int: self.random_integer,
            float: self.random_float,
            str: self.random_string
        }.get(data_type, self.unsupported_type)
        return generator()

    def random_integer(self):
        return random.randint(1, 100)

    def random_float(self):
        return random.uniform(0.0, 1.0)

    def random_string(self):
        return ''.join(random.choice(string.ascii_letters) for _ in range(5))

    def unsupported_type(self):
        raise ValueError("Unsupported data type")

    def generate_random_lists(self, data_types, num_lists, items_per_list_min, items_per_list_max):
        return [
            [self.generate_random_variable(data_types) for _ in range(random.randint(items_per_list_min, items_per_list_max))]
            for _ in range(num_lists)
        ]

if __name__ == "__main__":
    rng = RandomGenerator(seed=42)

    data_types = [int, float, str]
    num_lists = 5
    items_per_list_min = 1
    items_per_list_max = 10

    random_lists = rng.generate_random_lists(data_types, num_lists, items_per_list_min, items_per_list_max)

    for i, lst in enumerate(random_lists):
        print(f"List {i+1}: {lst}")
