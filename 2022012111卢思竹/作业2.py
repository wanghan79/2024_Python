import random
import string

def extract_integers(data):
    integers = []

    if isinstance(data, int):
        integers.append(data)
    elif isinstance(data, (list, tuple, set)):
        for item in data:
            integers.extend(extract_integers(item))
    elif isinstance(data, dict):
        for item in data.values():
            integers.extend(extract_integers(item))

    return integers

def calculate_data(operation, integers):
    if operation == 'sum':
        result = sum(integers)
    elif operation == 'average':
        result = sum(integers) / len(integers)
    else:
        raise ValueError(f"Invalid operation. Please choose either 'sum' or 'average'.")

    return result

def generate_data_sample(data_structure):
    sample = {}
    for key, value in data_structure.items():
        if key == 'int':
            sample[key] = random.randint(value['datarange'][0], value['datarange'][1])
        elif key == 'float':
            sample[key] = random.uniform(value['datarange'][0], value['datarange'][1])
        elif key == 'str':
            sample[key] = ''.join(random.choice(value['datarange']) for _ in range(value['len']))
        elif key in ('tuple', 'list', 'set'):
            sample[key] = generate_data_sample(value)
    return sample

def generate_random_data(data_specs):
    return [generate_data_sample(data_specs['structure']) for _ in range(data_specs['num'])]

if __name__ == '__main__':
    data_specs = {
        'num': 5,
        'structure': {
            'tuple': {
                'int': {'datarange': [1, 10]},
                'list': {
                    'int': {'datarange': [1, 10]},
                    'str': {'datarange': string.ascii_lowercase, 'len': 8},
                    'tuple': {'str': {'datarange': string.ascii_lowercase, 'len': 5}}
                }
            }
        }
    }

    # Generate random data
    random_data = generate_random_data(data_specs)

    # Extract integers
    integers = extract_integers(random_data)
    print(random_data)

    # Calculate sum
    sum_result = calculate_data('sum', integers)
    print("Sum:", sum_result)

    # Calculate average
    average_result = calculate_data('average', integers)
    print("Average:", average_result)
