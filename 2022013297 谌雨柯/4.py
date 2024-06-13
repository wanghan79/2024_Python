import random
import string

# 随机生成一个字典类型的数据的生成器
def generate_random_dict_data():
    while True:  # 使生成器无限运行
        yield {
            "number": random.randint(1, 100),
            "string": ''.join(random.choices(string.ascii_letters, k=5)),
            "boolean": random.choice([True, False])
        }

# 随机生成一个列表类型的数据的生成器
def generate_random_list_data(element_type, count=5):
    while True:  # 使生成器无限运行
        for _ in range(count):
            if element_type == "dict":
                yield generate_random_dict_data()
            elif element_type == "str":
                yield ''.join(random.choices(string.ascii_letters, k=5))

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
        "hobbies": "list"  # 这里指定为list，意味着hobbies字段是一个字符串列表
    }
}

# 生成符合示例数据结构的随机数据的生成器
def generate_random_data_based_on_structure(struct):
    for key, value_type in struct.items():
        if value_type == "int":
            yield (key, random.randint(1, 100))
        elif value_type == "str":
            yield (key, ''.join(random.choices(string.ascii_letters, k=5)))
        elif value_type == "bool":
            yield (key, random.choice([True, False]))
        elif value_type == "list":
            # 假设列表中的元素类型与data_structure_1相同，生成一个包含生成器的列表
            list_generator = generate_random_list_data("dict", random.randint(1, 5))
            yield (key, list(list_generator))  # 获取列表中的所有项

# 使用生成器创建和输出数据
def print_random_data(structure):
    for struct_name, struct_data in structure.items():
        random_data_gen = generate_random_data_based_on_structure(struct_data)
        random_data = dict(random_data_gen)  # 获取生成器中的所有项
        print(f"{struct_name}: {random_data}")

# 调用函数打印随机数据
print_random_data(example_data_structures)