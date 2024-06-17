import random 

class RandomDictGenerator:
    def __init__(self, num):
        self.num = num
    def generate_random_dict(self):
        result = {}
        for i in range(self.num):
            key = f"key_{i}"  
            value = random.randint(1, 100)
            result[key] = value
        return result 
    def sum_int_values(self, random_dict):
        return sum([value for value in random_dict.values()
if isinstance(value, int)])
generator = RandomDictGenerator(5)
random_dict = generator.generate_random_dict()
print(random_dict)
print(generator.sum_int_values(random_dict))