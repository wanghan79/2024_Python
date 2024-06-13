import random
### 作业1
class DataStructure:
    def __init__(self, data_type, value_range):
        self.data_type = data_type
        self.value_range = value_range

    def generate_random_data(self):
        if self.data_type == 'int':
            return random.randint(*self.value_range)
        elif self.data_type == 'float':
            return random.uniform(*self.value_range)
        elif self.data_type == 'str':
            return ''.join(random.choices(self.value_range, k=10))
        else:
            return None

# 示例用法
ds = DataStructure('int', (1, 100))
print(ds.generate_random_data())


### 作业2
class RandomDataGenerator:
    def __init__(self, data_structures):
        self.data_structures = data_structures

    def generate_data(self):
        return [ds.generate_random_data() for ds in self.data_structures]

# 示例用法
data_structures = [DataStructure('int', (1, 100)), DataStructure('float', (1.0, 100.0))]
generator = RandomDataGenerator(data_structures)
print(generator.generate_data())


### 作业3
def count_data_types(func):
    counts = {'int': 0, 'float': 0, 'str': 0}

    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        for item in data:
            if isinstance(item, int):
                counts['int'] += 1
            elif isinstance(item, float):
                counts['float'] += 1
            elif isinstance(item, str):
                counts['str'] += 1
        print("Data type counts:", counts)
        return data

    return wrapper

class EnhancedRandomDataGenerator(RandomDataGenerator):
    @count_data_types
    def generate_data(self):
        return super().generate_data()

# 示例用法
enhanced_generator = EnhancedRandomDataGenerator(data_structures)
print(enhanced_generator.generate_data())



### 作业4
class IterableRandomDataGenerator:
    def __init__(self, data_structures):
        self.data_structures = data_structures

    def __iter__(self):
        return self.generate_data()

    def generate_data(self):
        for ds in self.data_structures:
            yield ds.generate_random_data()

# 示例用法
iterable_generator = IterableRandomDataGenerator(data_structures)
for data in iterable_generator:
    print(data)

