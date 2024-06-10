import random
import string

class RandomGenerator:
    def __init__(self, seed=None):
        random.seed(seed)

    def generate_random_variable(self, data_types):
        random_type = random.choice(data_types)
        if random_type == int:
            return self.random_integer()
        elif random_type == float:
            return self.random_float()
        elif random_type == str:
            return self.random_string()
        else:
            raise ValueError("不支持类型")

    @staticmethod
    def random_integer():
        return random.randint(1, 100)

    @staticmethod
    def random_float():
        return random.uniform(0.0, 1.0)

    @staticmethod
    def random_string():
        return ''.join(random.choice(string.ascii_letters) for _ in range(5))

    def generate_random_lists(self, data_types, num_lists, items_per_list_min, items_per_list_max):
        random_lists = []
        for _ in range(num_lists):
            items_count = random.randint(items_per_list_min, items_per_list_max)
            random_list = [self.generate_random_variable(data_types) for _ in range(items_count)]
            random_lists.append(random_list)
        return random_lists

    @staticmethod
    def sum_of_list(lst):
        return sum(item for item in lst if isinstance(item, (int, float)))

    @staticmethod
    def average_of_list(lst):
        values = [item for item in lst if isinstance(item, (int, float))]
        return sum(values) / len(values) if values else None

    def process_lists(self, lists):
        results = []
        for i, lst in enumerate(lists):
            if all(isinstance(item, (int, float)) for item in lst):
                sum_result = self.sum_of_list(lst)
                average_result = self.average_of_list(lst)
                results.append((i, sum_result, average_result))
            else:
                print(f"List {i+1} 无法计算和与平均")
        return results

def main():
    rng = RandomGenerator(seed=42)

    data_types = [int, float, str]
    num_lists = 5
    items_per_list_min = 1
    items_per_list_max = 10

    random_lists = rng.generate_random_lists(data_types, num_lists, items_per_list_min, items_per_list_max)

    for i, lst in enumerate(random_lists):
        print(f"List {i+1}: {lst}")

    results = rng.process_lists(random_lists)
    for idx, sum_result, average_result in results:
        if average_result is not None:
            print(f"List {idx+1}: 和= {sum_result}, 平均数 = {average_result}")
        else:
            print(f"List {idx+1} 无法计算和与平均")

if __name__ == "__main__":
    main()
