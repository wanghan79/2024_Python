import random
import string

# 定义生成数据样本的函数
def generate_sample(structure):
    result = []
    for data_type, data_details in structure.items():
        if data_type == 'int':
            range_start, range_end = data_details['range']
            result.append(random.randint(range_start, range_end))
        elif data_type == 'float':
            range_start, range_end = data_details['range']
            result.append(random.uniform(range_start, range_end))
        elif data_type == 'str':
            chars = data_details['chars']
            str_length = data_details['length']
            result.append(''.join(random.choice(chars) for _ in range(str_length)))
        elif data_type in ['tuple', 'list', 'set']:
            sub_data = generate_sample(data_details)
            if data_type == 'tuple':
                result.append(tuple(sub_data))
            elif data_type == 'list':
                result.append(sub_data)
            elif data_type == 'set':
                result.append(set(sub_data))
    return result

# 定义生成函数
def sample_generator(structure, num=1):
    for _ in range(num):
        yield generate_sample(structure)

# Test the generator function
if __name__ == '__main__':
    # Create a generator and iterate over generated data samples
    generator = sample_generator(
        structure={
            'int': {'range': [1, 100]},
            'list': {
                'int': {'range': [1, 100]},
                'float': {'range': [1.0, 100.0]},
                'str': {'chars': string.ascii_letters, 'length': 12},
                'tuple': {
                    'str': {'chars': string.ascii_lowercase, 'length': 8}
                }
            }
        },
        num=5
    )

    # print
    for sample in generator:
        print(sample)
