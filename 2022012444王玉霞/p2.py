import random
import string


class DataGenerator:
    @staticmethod
    def dataSampling(**kwargs):
        if kwargs['datatype'] == 'int':
            it = iter(kwargs['datarange'])
            return random.randint(next(it), next(it))
        elif kwargs['datatype'] == 'float':
            it = iter(kwargs['datarange'])
            return random.uniform(next(it), next(it))
        elif kwargs['datatype'] == 'str':
            if isinstance(kwargs['datarange'], tuple) and len(kwargs['datarange']) == 2:
                return ''.join(random.choices(string.ascii_letters, k=kwargs['datarange'][1]))
            else:
                return ''.join(random.choices(string.ascii_letters, k=kwargs['datarange']))
        elif kwargs['datatype'] in ('list', 'tuple'):
            elements = []
            for _ in range(kwargs.get('num', 1)):
                sub_elements = {}
                for sub_key, sub_kwargs in kwargs['subs'].items():
                    sub_elements[sub_key] = DataGenerator.dataSampling(**sub_kwargs)
                elements.append(sub_elements)
            if kwargs['datatype'] == 'list':
                return elements
            else:
                return tuple(elements)

    @staticmethod
    def structDataSampling(para):
        result = {}
        result['num'] = para['num']
        result['data'] = []
        for _ in range(para['num']):
            data = {}
            for key, value in para['struct']['subs'].items():
                if isinstance(value, dict):
                    data[key] = DataGenerator.dataSampling(**value)
                else:
                    data[key] = value
            result['data'].append(data)
        return result


# Example usage
para = {
    "num": 1,
    "struct": {
        "datatype": "list",
        "subs": {
            "int_data": {"datatype": "int", "datarange": [1, 100]},
            "float_data": {"datatype": "float", "datarange": [0.0, 1.0]},
            "list_data": {"datatype": "list", "subs": {"int_data": {"datatype": "int", "datarange": [1,47,68]},
                                                        "str_data": {"datatype": "str", "datarange": 10}}}
        }
    }
}

# Sample data
data_generator = DataGenerator()
sample = data_generator.structDataSampling(para)
print(sample)
