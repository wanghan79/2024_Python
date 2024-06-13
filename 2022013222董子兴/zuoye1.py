import random

def create_random_data(**params):
    results = []
    for type_key, attributes in params.items():
        if type_key == 'integer':
            sequence = [random.randint(attributes.get('min', 0), attributes.get('max', 100)) for _ in range(attributes.get('size', 1))]
        elif type_key == 'floating':
            sequence = [random.uniform(attributes.get('min', 0.0), attributes.get('max', 1.0)) for _ in range(attributes.get('size', 1))]
        elif type_key == 'string':
            characters = attributes.get('characters', 'abcdefghijklmnopqrstuvwxyz0123456789')
            sequence = [''.join(random.choices(characters, k=attributes.get('length', 1))) for _ in range(attributes.get('size', 1))]
        elif type_key == 'tuple_type':
            if 'size' in attributes:
                sequence = tuple(create_random_data(**attributes) for _ in range(attributes['size']))
            else:
                sequence = tuple(create_random_data(**attributes))
        elif type_key == 'list_type':
            if 'size' in attributes:
                sequence = [create_random_data(**attributes) for _ in range(attributes['size'])]
            else:
                sequence = [create_random_data(**attributes)]
        elif type_key == 'set_type':
            if 'size' in attributes:
                sequence = {tuple(create_random_data(**attributes)) for _ in range(attributes['size'])}
            else:
                sequence = {tuple(create_random_data(**attributes))}
        results.append(sequence)
    return results

if __name__ == '__main__':
    print(create_random_data(
        integer={'min': 10, 'max': 20, 'size': 7},
        tuple_type={
            'list_type': {'integer': {'min': 5, 'max': 15, 'size': 3}},
            'floating': {'min': 1, 'max': 10, 'size': 5},
            'string': {'characters': 'abc123', 'length': 6, 'size': 4},
            'tuple_type': {
                'string': {'characters': 'wjs2kqn31', 'length': 5, 'size': 5},
                'list_type': {'floating': {'min': 0.5, 'max': 2.5, 'size': 4}},
                'integer': {'min': 30, 'max': 50, 'size': 3}
            }
        }
    ))
