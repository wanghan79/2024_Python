import random
import string

def count_data(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        counts = {}
        for key, value in result.items():
            if isinstance(value, int):
                counts['int'] = counts.get('int', 0) + 1
            elif isinstance(value, str):
                counts['str'] = counts.get('str', 0) + 1
            elif isinstance(value, bool):
                counts['bool'] = counts.get('bool', 0) + 1
            elif isinstance(value, list):
                counts['list'] = counts.get('list', 0) + 1
        print("Data counts:", counts)
        return result
    return wrapper

class RandomDataGenerator:
    def __init__(self):
        pass

    @count_data
    def generate_random_dict_data(self):
        return {
            "number": random.randint(1, 100),
            "string": ''.join(random.choices(string.ascii_letters, k=5)),
            "boolean": random.choice([True, False])
        }

    @count_data
    def generate_random_list_data(self, element_type, count=5):
        if element_type == "dict":
            return [self.generate_random_dict_data() for _ in range(count)]
        elif element_type == "str":
            return [''.join(random.choices(string.ascii_letters, k=5)) for _ in range(count)]

    @count_data
    def generate_random_data_based_on_structure(self, struct):
        random_data = {}
        for key, value_type in struct.items():
            if value_type == "int":
                random_data[key] = random.randint(1, 100)
            elif value_type == "str":
                random_data[key] = ''.join(random.choices(string.ascii_letters, k=5))
            elif value_type == "bool":
                random_data[key] = random.choice([True, False])
            elif value_type == "list":
                # 假设列表中的每个元素都是一个字典类型的随机数据
                random_data[key] = self.generate_random_list_data("dict", count=random.randint(1, 5))
        return random_data

# 示例数据结构
example_data_structures = {
    "data_structure_1": {
        "number": "int",
        "string": "str",
        "boolean": "bool"
    },
    "data_structure_2": {
        "name": "str",
        "age": "int",
        "is_student": "bool",
        "hobbies": "list"  # 假设 hobbies 是一个包含随机字符串的列表
    }
}

data_generator = RandomDataGenerator()
# 生成符合示例数据结构的随机数据
random_data = {struct_name: data_generator.generate_random_data_based_on_structure(struct_data) for struct_name, struct_data in example_data_structures.items()}
for struct_name, data in random_data.items():
    print(f"{struct_name}: {data}")