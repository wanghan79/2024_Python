import random

# 定义数据结构
data_struct1 = {
    'type': tuple,
    'subfields': {
        'field1': {
            'type': list,
            'subfields': {
                'element1': {'type': int, 'range': [0, 100]},
                'element2': {'type': str, 'range': 'abcd', 'length': 5}
            }
        },
        'field2': {
            'type': tuple,
            'subfields': {
                'element1': {'type': float, 'range': [0, 100]},
                'element2': {'type': int, 'range': [0, 100]}
            }
        },
        'field3': {'type': str, 'range': 'abcdefg', 'length': 10}
    }
}

data_struct2 = {
    'type': tuple,
    'subfields': {
        'field1': {
            'type': list,
            'subfields': {
                'element1': {'type': int, 'range': [0, 100]},
                'element2': {'type': str, 'range': 'abcd', 'length': 5}
            }
        },
        'field2': {
            'type': tuple,
            'subfields': {
                'element1': {
                    'type': tuple,
                    'subfields': {
                        'subelement1': {'type': int, 'range': [0, 100]},
                        'subelement2': {'type': float, 'range': [0, 20]}
                    }
                },
                'element2': {'type': int, 'range': [0, 100]}
            }
        },
        'field3': {'type': str, 'range': 'abcdefg', 'length': 10}
    }
}

class DataGenerator:
    def __init__(self):
        self.num = 1

    def generate_list(self, config):
        result = []
        for key, spec in config.items():
            if spec.get("type") == int:
                val = random.randint(spec.get("range")[0], spec.get("range")[1])
                result.append(val)
            elif spec.get("type") == float:
                val = random.uniform(spec.get("range")[0], spec.get("range")[1])
                result.append(val)
            elif spec.get("type") == str:
                val = ''.join(random.choice(spec.get("range")) for _ in range(spec.get("length")))
                result.append(val)
            elif spec.get("type") in (tuple, list):
                val = self.generate_structure(spec)
                result.append(val)
            elif spec.get("type") == dict:
                val = self.generate_dict(spec)
                result.append(val)
        return result

    def generate_tuple(self, config):
        result = []
        for key, spec in config.items():
            if spec.get("type") == int:
                val = random.randint(spec.get("range")[0], spec.get("range")[1])
                result.append(val)
            elif spec.get("type") == float:
                val = random.uniform(spec.get("range")[0], spec.get("range")[1])
                result.append(val)
            elif spec.get("type") == str:
                val = ''.join(random.choice(spec.get("range")) for _ in range(spec.get("length")))
                result.append(val)
            elif spec.get("type") in (tuple, list):
                val = self.generate_structure(spec)
                result.append(val)
            elif spec.get("type") == dict:
                val = self.generate_dict(spec)
                result.append(val)
        return tuple(result)

    def generate_structure(self, struct):
        type = struct.get('type')
        if type == int:
            return random.randint(struct['range'][0], struct['range'][1])
        elif type == float:
            return random.uniform(struct['range'][0], struct['range'][1])
        elif type == str:
            return ''.join(random.choice(struct['range']) for _ in range(struct['length']))
        elif type == list:
            return self.generate_list(struct['subfields'])
        elif type == tuple:
            return self.generate_tuple(struct['subfields'])

    def data_sampling(self, count, config):
        return [self.generate_structure(config) for _ in range(count)]

    def calculate_sum(self, data):
        if isinstance(data, tuple):
            return self.sum_tuple(data)
        elif isinstance(data, list):
            return self.sum_list(data)
        return data

    def sum_tuple(self, data):
        return sum(self.calculate_sum(value) if isinstance(value, (tuple, list)) else value for value in data)

    def sum_list(self, data):
        return sum(self.calculate_sum(value) if isinstance(value, (tuple, list)) else value for value in data)

    def count_elements(self, data):
        if isinstance(data, tuple):
            return self.count_tuple_elements(data)
        elif isinstance(data, list):
            return self.count_list_elements(data)
        return 1

    def count_tuple_elements(self, data):
        return sum(self.count_elements(value) for value in data)

    def count_list_elements(self, data):
        return sum(self.count_elements(value) for value in data)

    def calculate_average(self, data):
        total_sum = self.calculate_sum(data)
        total_count = self.count_elements(data)
        return total_sum / total_count

generator = DataGenerator()
sampled_data = generator.data_sampling(1, data_struct2)
print(sampled_data)
