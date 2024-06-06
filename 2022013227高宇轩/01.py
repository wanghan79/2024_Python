"""
源代码
"""

import random


def data_sampling(**kwargs):
    data_type = kwargs.get('data_type')
    data_range = kwargs.get('data_range')
    subs = kwargs.get('subs')

    if data_type == int:
        if len(data_range) == 1:
            return data_range[0]
        else:
            return random.randint(*data_range)

    elif data_type == bool:
        return random.choice(data_range)

    elif data_type == float:
        if len(data_range) == 1:
            return data_range[0]
        else:
            return random.uniform(*data_range)

    elif data_type == str:
        if isinstance(data_range, str):
            data_len = kwargs.get('len')
            return ''.join(random.choice(data_range) for _ in range(data_len))
        else:
            return random.choice(data_range)

    elif data_type == tuple:
        return tuple(data_sampling(**v) for v in subs.values())

    elif data_type == set:
        return {data_sampling(**v) for v in subs.values()}

    elif data_type == list:
        return [data_sampling(**v) for v in subs.values()]

    else:
        return {k: data_sampling(**v) for k, v in subs.items()}


# Test Case
# Define a complex data structure
complex_structure = {
    'data_type': dict,
    'subs': {
        'name': {'data_type': str, 'data_range': 'abcdefghijklmnopqrstuvwxyz', 'len': 5},
        'age': {'data_type': int, 'data_range': [18, 80]},
        'coordinates': {
            'data_type': tuple,
            'subs': {
                'latitude': {'data_type': float, 'data_range': [-90, 90]},
                'longitude': {'data_type': float, 'data_range': [-180, 180]}
            }
        },
        'friends': {
            'data_type': list,
            'subs': {
                'friend': {'data_type': str, 'data_range': ['Alice', 'Bob', 'Charlie', 'Diana']}
            }
        }
    }
}

# Generate data using the complex structure
print(data_sampling(**complex_structure))


