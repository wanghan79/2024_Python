import random
import string


def collect_integers(data):
    integers = []

    def _collect_integers(data):
        if isinstance(data, int):
            integers.append(data)
        elif isinstance(data, (list, tuple, set)):
            for item in data:
                _collect_integers(item)
        elif isinstance(data, dict):
            for item in data.values():
                _collect_integers(item)

    _collect_integers(data)
    return integers


def compute_data(operation, integers):
    if operation == 'sum':
        result = sum(integers)
    elif operation == 'average':
        result = sum(integers) / len(integers)
    else:
        raise ValueError("Invalid operation. Please choose either 'sum' or 'average'.")

    return result


def data_processor(func):
    def wrapper(operation, **kwargs):
        # Generate random data
        generated_data = func(**kwargs)

        # Extract integers from the generated data
        integers = collect_integers(generated_data)

        # Compute the result based on the given operation
        result = compute_data(operation, integers)

        return result

    return wrapper


def generate_random_sample(data_structure):
    sample = {}
    for key, value in data_structure.items():
        if key == 'int':
            range_start, range_end = value['datarange']
            sample[key] = random.randint(range_start, range_end)
        elif key == 'float':
            range_start, range_end = value['datarange']
            sample[key] = random.uniform(range_start, range_end)
        elif key == 'str':
            chars = value['datarange']
            str_length = value['len']
            sample[key] = ''.join(random.choice(chars) for _ in range(str_length))
        elif key in ['tuple', 'list', 'set']:
            sample[key] = generate_random_sample(value)
    return sample


@data_processor
def process_random_data(**kwargs):
    num_samples = kwargs.pop('num')
    data = []
    for _ in range(int(num_samples)):
        data.append(generate_random_sample(kwargs['structure']))
    return data


# Generate random data and calculate the sum
sum_result = process_random_data('sum', num=5, structure={'tuple': {'int': {'datarange': [1, 10]},
                                                                 'list': {'int': {'datarange': [1, 10]},
                                                                          'str': {'datarange': string.ascii_lowercase,
                                                                                  'len': 8},
                                                                          'tuple': {'str': {'datarange': string.ascii_lowercase,
                                                                                            'len': 5}}}}})
print("Sum:", sum_result)

# Generate random data and calculate the average
average_result = process_random_data('average', num=5, structure={'tuple': {'int': {'datarange': [1, 10]},
                                                                         'list': {'int': {'datarange': [1, 10]},
                                                                                  'str': {'datarange': string.ascii_lowercase,
                                                                                          'len': 8},
                                                                                  'tuple': {'str': {'datarange': string.ascii_lowercase,
                                                                                                    'len': 5}}}}})
print("Average:", average_result)
