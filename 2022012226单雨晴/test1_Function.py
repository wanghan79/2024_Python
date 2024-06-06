#函数生成随机数
import random
import string

def structDataSampling(**kwargs):
    type_mapping = {
        int: "整型",
        float: "浮点数",
        str: "字符串",
        list: "列表"
    }

    results = []
    num = kwargs.get('num', 1)
    struct = kwargs.get('struct', {})

    for _ in range(num):
        group = []  # 存放每一组随机数
        for element_type, element_options in struct.items():
            if element_type == int:
                data_range = element_options['datarange']
                random_number = random.randint(data_range[0], data_range[1])
                group.append((random_number, type_mapping[element_type]))
            elif element_type == float:
                data_range = element_options['datarange']
                random_number = random.uniform(data_range[0], data_range[1])
                group.append((random_number, type_mapping[element_type]))
            elif element_type == tuple:
                data_range = element_options['datarange']
                random_number = random.uniform(data_range[0], data_range[1])
                group.append((random_number, type_mapping[element_type]))
            elif element_type == str:
                data_range = element_options['datarange']
                str_length = element_options.get('len', 10)
                random_string = ''.join(random.choice(data_range) for _ in range(str_length))
                group.append((random_string, type_mapping[element_type]))
            elif element_type == list:
                list_length = element_options.get('len', 10)
                random_list = [random.randint(-100, 100) for _ in range(list_length)]
                group.append((random_list, type_mapping[element_type]))

        results.append(group)

    return results

# 将struct存放到一个字典读入
data = [
    {int: {"datarange": (0, 10)}, str: {"datarange": string.ascii_letters, "len": 10}},
    {float: {"datarange": (0, 10000)}, str: {"datarange": string.ascii_uppercase, "len": 50}},
    {int: {"datarange": (0, 100)}, float: {"datarange": (0, 10000)}, str: {"datarange": string.ascii_uppercase, "len": 50}},
    {int:{"datarange": (0, 100)}, float: {"datarange": (0, 10000)}, str: {"datarange": string.ascii_uppercase, "len": 50}},
    {list: {"len": 5}}
]

for struct in data:
    result = structDataSampling(num=5, struct=struct)
    print(result)
