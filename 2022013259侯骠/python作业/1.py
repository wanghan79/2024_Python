import random

student1 = {
    'datatype': tuple,
    'subs': {
        'sub1': {
            'datatype': list,
            'subs': {
                'sub1': {'datatype': int, 'datarange': [0, 100]},
                'sub2': {'datatype': str, 'datarange': 'abcd', 'len': 5}
            }
        },
        'sub2': {
            'datatype': tuple,
            'subs': {
                'sub1': {'datatype': float, 'datarange': [0, 100]},
                'sub2': {'datatype': int, 'datarange': [0, 100]}
            }
        },
        'sub3': {'datatype': str, 'datarange': 'abcdefg', 'len': 10}
    }
}

student2 = {
    'datatype': tuple,
    'subs': {
        'sub1': {
            'datatype': list,
            'subs': {
                'sub1': {'datatype': int, 'datarange': [0, 100]},
                'sub2': {'datatype': str, 'datarange': 'abcd', 'len': 5}
            }
        },
        'sub2': {
            'datatype': tuple,
            'subs': {
                'sub1': {
                    'datatype': tuple,
                    'subs': {
                        'sub1': {'datatype': int, 'datarange': [0, 100]},
                        'sub2': {'datatype': float, 'datarange': [0, 20]}
                    }
                },
                'sub2': {'datatype': int, 'datarange': [0, 100]}
            }
        },
        'sub3': {'datatype': str, 'datarange': 'abcdefg', 'len': 10}
    }
}

def generate_list(data_structure):
    result_list = []
    for k, v in data_structure.items():
        if v.get("datatype") == int:
            result_list.append(random.randint(v["datarange"][0], v["datarange"][1]))
        elif v.get("datatype") == float:
            result_list.append(random.uniform(v["datarange"][0], v["datarange"][1]))
        elif v.get("datatype") == str:
            result_str = ''.join(random.choice(v["datarange"]) for _ in range(v["len"]))
            result_list.append(result_str)
        elif v.get("datatype") == tuple:
            result_list.append(generate_structure(v))
        elif v.get("datatype") == list:
            result_list.append(generate_structure(v))
        elif v.get("datatype") == dict:
            result_list.append(generate_dict(v))
    return result_list

def generate_tuple(data_structure):
    temp_list = []
    for k, v in data_structure.items():
        if v.get("datatype") == int:
            temp_list.append(random.randint(v["datarange"][0], v["datarange"][1]))
        elif v.get("datatype") == float:
            temp_list.append(random.uniform(v["datarange"][0], v["datarange"][1]))
        elif v.get("datatype") == str:
            result_str = ''.join(random.choice(v["datarange"]) for _ in range(v["len"]))
            temp_list.append(result_str)
        elif v.get("datatype") == tuple:
            temp_list.append(generate_structure(v))
        elif v.get("datatype") == list:
            temp_list.append(generate_structure(v))
        elif v.get("datatype") == dict:
            temp_list.append(generate_dict(v))
    return tuple(temp_list)

def generate_structure(struct):
    datatype = struct.get("datatype")
    if datatype == int:
        return random.randint(struct["datarange"][0], struct["datarange"][1])
    elif datatype == float:
        return random.uniform(struct["datarange"][0], struct["datarange"][1])
    elif datatype == str:
        return ''.join(random.choice(struct["datarange"]) for _ in range(struct["len"]))
    elif datatype == list:
        return generate_list(struct["subs"])
    elif datatype == tuple:
        return generate_tuple(struct["subs"])

def generate_dict(data_structure):
    result_dict = {}
    for k, v in data_structure.items():
        if v["datatype"] == int:
            result_dict[k] = random.randint(v["datarange"][0], v["datarange"][1])
        elif v["datatype"] == float:
            result_dict[k] = random.uniform(v["datarange"][0], v["datarange"][1])
        elif v["datatype"] == str:
            result_dict[k] = ''.join(random.choice(v["datarange"]) for _ in range(v["len"]))
        elif v["datatype"] == dict:
            result_dict[k] = generate_dict(v)
        elif v["datatype"] == tuple:
            result_dict[k] = generate_structure(v)
        elif v["datatype"] == list:
            result_dict[k] = generate_list(v)
    return result_dict

def data_sampling(num_samples, data_structure):
    samples = []
    for _ in range(num_samples):
        samples.append(generate_structure(data_structure))
    return samples

def calculate_sum(data):
    if isinstance(data, tuple):
        return sum_tuple(data)
    elif isinstance(data, list):
        return sum_list(data)
    else:
        return data

def sum_tuple(data):
    return sum(calculate_sum(value) for value in data if isinstance(value, (int, float, tuple, list)))

def sum_list(data):
    return sum(calculate_sum(value) for value in data if isinstance(value, (int, float, tuple, list)))

def count_elements(data):
    if isinstance(data, tuple):
        return count_tuple_elements(data)
    elif isinstance(data, list):
        return count_list_elements(data)
    elif isinstance(data, dict):
        return count_dict_elements(data)
    else:
        return 1

def count_tuple_elements(data):
    return sum(count_elements(value) for value in data if isinstance(value, (int, float, tuple, list, dict)))

def count_list_elements(data):
    return sum(count_elements(value) for value in data if isinstance(value, (int, float, tuple, list, dict)))

def count_dict_elements(data):
    return sum(count_elements(value) for value in data.values() if isinstance(value, (int, float, tuple, list, dict)))

def calculate_average(data):
    total_sum = calculate_sum(data)
    total_count = count_elements(data)
    return total_sum / total_count

result = data_sampling(1, student2)
print(result)
print("Average value:", calculate_average(result[0]))
