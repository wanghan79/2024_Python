import random
import string

#修饰器修饰，并求和、均值
def data_sampling_decorator(func):
    def wrapper(*args, **kwargs):
        results = func(*args, **kwargs)

        # 对结果进行修饰处理
        decorated_results = []
        for group in results:
            decorated_group = []
            for data, data_type in group:
                if data_type == "整数":
                    decorated_data = f"整数数据：{data}"
                    decorated_group.append(decorated_data)
                elif data_type == "浮点数":
                    decorated_data = f"浮点数数据：{data:.2f}"
                    decorated_group.append(decorated_data)
                elif data_type == "字符串":
                    decorated_data = f"字符串数据：'{data}'"
                    decorated_group.append(decorated_data)
                elif data_type == "列表":
                    decorated_data = f"列表数据：{data}"
                    if all(isinstance(item, (int, float)) for item in data):
                        sum_value = sum(data)
                        avg_value = sum_value / len(data)
                        decorated_data += f"，和为：{sum_value:.2f}，均值为：{avg_value:.2f}"
                    else:
                        decorated_data += f"，无法求和和均值"
                    decorated_group.append(decorated_data)

            decorated_results.append(decorated_group)

        return decorated_results

    return wrapper


@data_sampling_decorator
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
    {int: {"datarange": (0, 100)}, float: {"datarange": (0, 10000)},
     str: {"datarange": string.ascii_uppercase, "len": 50}},
    {int: {"datarange": (0, 100)}, float: {"datarange": (0, 10000)},
     str: {"datarange": string.ascii_uppercase, "len": 50}},
    {list: {"len": 5}}
]

for struct in data:
    result = structDataSampling(num=5, struct=struct)
    print(result)
