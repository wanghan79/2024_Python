import random
from example_template import example_template

def generate_data(template):
    datatype = template.get("datatype")
    subs = template.get("subs", {})

    result = {
        tuple: (),
        list: [],
        dict: {},
        set: set()
    }[datatype]

    for key, value in subs.items():
        data = generate_item(value)
        if datatype == tuple:
            result += (data,)
        elif datatype == list:
            result.append(data)
        elif datatype == dict:
            result[key] = data
        elif datatype == set:
            result.add(data)

    return result

def generate_item(value):
    if "datatype" in value and "datarange" in value:
        if value["datatype"] == int:
            return random.randint(value["datarange"][0], value["datarange"][1])
        elif value["datatype"] == float:
            return random.uniform(value["datarange"][0], value["datarange"][1])
        elif value["datatype"] == str:
            return random.SystemRandom().choice(value['datarange'])
    return generate_data(value)


def dataExtraction(example, num):
    result = []
    for _ in range(num):
        extracted_data = generate_data(example)
        result.append(extracted_data)
    return result

if __name__ == '__main__':
    extracted_data = dataExtraction(example_template, num=3)

    print("Generated random data:")
    for data in extracted_data:
        print(data)
