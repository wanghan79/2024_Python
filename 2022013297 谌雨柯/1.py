import random
import string

# 随机生成一个字典类型的数据
def generate_random_dict_data():
    return {
        "number": random.randint(1, 100),
        "string": ''.join(random.choices(string.ascii_letters, k=5)),
        "boolean": random.choice([True, False])
    }

# 随机生成一个列表类型的数据
def generate_random_list_data(element_type, count=5):
    if element_type == list:
        return [generate_random_dict_data() for _ in range(count)]
    elif element_type == str:
        return [''.join(random.choices(string.ascii_letters, k=5)) for _ in range(count)]
    # 可以根据需要添加更多的类型处理

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

# 生成符合示例数据结构的随机数据
def generate_random_data_based_on_structure(struct):
    random_data = {}
    for key, value_type in struct.items():
        if value_type == "int":
            random_data[key] = random.randint(1, 100)
        elif value_type == "str":
            random_data[key] = ''.join(random.choices(string.ascii_letters, k=5))
        elif value_type == "bool":
            random_data[key] = random.choice([True, False])
        elif value_type == "list":
            # 这里假设列表中的元素类型与data_structure_1相同
            random_data[key] = generate_random_list_data(generate_random_dict_data, count=random.randint(1, 5))
    return random_data

# 打印生成的随机数据
random_data = {struct_name: generate_random_data_based_on_structure(struct_data) for struct_name, struct_data in example_data_structures.items()}
for struct_name, data in random_data.items():
    print(f"{struct_name}: {data}")
