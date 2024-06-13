import random

class DataCreator:
    def __init__(self):
        self.config = {}

    def create(self, **specs):
        output = []
        for data_type, params in specs.items():
            if data_type == 'integer':
                numbers = [random.randint(params.get('lower', 0), params.get('upper', 100)) for _ in range(params.get('count', 1))]
            elif data_type == 'decimal':
                numbers = [random.uniform(params.get('lower', 0.0), params.get('upper', 1.0)) for _ in range(params.get('count', 1))]
            elif data_type == 'characters':
                choices = params.get('set', 'abcdefghijklmnopqrstuvwxyz0123456789')
                numbers = [''.join(random.choices(choices, k=params.get('length', 1))) for _ in range(params.get('count', 1))]
            elif data_type == 'group':
                if 'count' in params:
                    numbers = tuple(self.create(**params) for _ in range(params['count']))
                else:
                    numbers = tuple(self.create(**params))
            elif data_type == 'sequence':
                if 'count' in params:
                    numbers = [self.create(**params) for _ in range(params['count'])]
                else:
                    numbers = [self.create(**params)]
            elif data_type == 'collection':
                if 'count' in params:
                    numbers = {tuple(self.create(**params)) for _ in range(params['count'])}
                else:
                    numbers = {tuple(self.create(**params))}
            output.append(numbers)
        return output

if __name__ == '__main__':
    data_gen = DataCreator()
    print(data_gen.create(
        integer={'lower': 10, 'upper': 20, 'count': 7},
        group={
            'sequence': {'integer': {'lower': 5, 'upper': 15, 'count': 3}},
            'decimal': {'lower': 1, 'upper': 10, 'count': 5},
            'characters': {'set': 'abc123', 'length': 6, 'count': 4},
            'group': {
                'characters': {'set': 'wjs2kqn31', 'length': 5, 'count': 5},
                'sequence': {'decimal': {'lower': 0.5, 'upper': 2.5, 'count': 4}},
                'integer': {'lower': 30, 'upper': 50, 'count': 3}
            }
        }
    ))
