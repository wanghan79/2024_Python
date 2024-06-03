import random
import string


def structDataSampling():
    results = []
    num_samples = int(input("请输入样本数量："))
    data_struct = {}

    while True:
        data_type = input("请输入数据类型（输入exit退出）：")
        if data_type.lower() == "exit":
            break

        data_options = {}

        if data_type == 'string':
            data_options['datarange'] = string.ascii_uppercase
            len_range = input("请输入字符串长度范围（最小值和最大值以空格分隔，可选，不输入则使用默认值）：")
            if len_range:
                data_options['len'] = tuple(map(int, len_range.split()))
            else:
                data_options['len'] = (10, 10)
        elif data_type == 'int':
            data_options['datarange'] = tuple(map(int, input("请输入int的范围（以空格分隔）：").split()))
        elif data_type == 'float':
            data_options['datarange'] = tuple(map(float, input("请输入float的范围（以空格分隔）：").split()))
        elif data_type == 'double':
            data_options['datarange'] = tuple(map(float, input("请输入double的范围（以空格分隔）：").split()))
        elif data_type == 'list' or data_type == 'tuple':
            data_options['datarange'] = input("请输入自定义类型的数据范围（以空格分隔）：").split()

        data_struct[data_type] = data_options

    for _ in range(num_samples):
        sample = {}
        for data_type, data_options in data_struct.items():
            if data_type == 'string':
                datarange = data_options.get('datarange', string.ascii_uppercase)
                len_range = data_options.get('len', (10, 10))
                str_len = random.randint(len_range[0], len_range[1])
                sample[data_type] = ''.join(random.choices(datarange, k=str_len))
            elif data_type == 'int':
                datarange = data_options.get('datarange', (18, 25))
                sample[data_type] = random.randint(datarange[0], datarange[1])
            elif data_type == 'float':
                datarange = data_options.get('datarange', (150.0, 200.0))
                sample[data_type] = round(random.uniform(datarange[0], datarange[1]), 2)
            elif data_type == 'double':
                datarange = data_options.get('datarange', (150.0, 200.0))
                sample[data_type] = round(random.uniform(datarange[0], datarange[1]), 2)
            elif data_type == 'list' or data_type == 'tuple':
                datarange = data_options.get('datarange', [])
                sample[data_type] = random.sample(datarange, random.randint(1, len(datarange)))

        results.append(sample)

    return results


samples = structDataSampling()
for sample in samples:
    print(sample)