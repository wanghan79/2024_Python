"""
类封装
"""

import random


class DataGenerator:
    def __init__(self):
        pass

    def generate_data(self, **kwargs):
        data_type = kwargs.get('data_type')
        subs = kwargs.get('subs')

        if data_type == int:
            return self._generate_int(**kwargs)
        elif data_type == bool:
            return self._generate_bool(**kwargs)
        elif data_type == float:
            return self._generate_float(**kwargs)
        elif data_type == str:
            return self._generate_str(**kwargs)
        elif data_type == tuple:
            return self._generate_tuple(**kwargs)
        elif data_type == set:
            return self._generate_set(**kwargs)
        elif data_type == list:
            return self._generate_list(**kwargs)
        elif data_type == dict:
            return self._generate_dict(**kwargs)
        else:
            raise ValueError("Invalid data type")

    def _generate_int(self, **kwargs):
        data_range = kwargs.get('data_range')
        if len(data_range) == 1:
            return data_range[0]
        else:
            return random.randint(*data_range)

    def _generate_bool(self, **kwargs):
        data_range = kwargs.get('data_range')
        return random.choice(data_range)

    def _generate_float(self, **kwargs):
        data_range = kwargs.get('data_range')
        if len(data_range) == 1:
            return data_range[0]
        else:
            return random.uniform(*data_range)

    def _generate_str(self, **kwargs):
        data_range = kwargs.get('data_range')
        if isinstance(data_range, str):
            data_len = kwargs.get('len')
            return ''.join(random.choice(data_range) for _ in range(data_len))
        else:
            return random.choice(data_range)

    def _generate_tuple(self, **kwargs):
        subs = kwargs.get('subs')
        return tuple(self.generate_data(**v) for v in subs.values())

    def _generate_set(self, **kwargs):
        subs = kwargs.get('subs')
        return {self.generate_data(**v) for v in subs.values()}

    def _generate_list(self, **kwargs):
        subs = kwargs.get('subs')
        return [self.generate_data(**v) for v in subs.values()]

    def _generate_dict(self, **kwargs):
        subs = kwargs.get('subs')
        return {k: self.generate_data(**v) for k, v in subs.items()}


# Test the DataGenerator class
data_generator = DataGenerator()
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

print(data_generator.generate_data(**complex_structure))
