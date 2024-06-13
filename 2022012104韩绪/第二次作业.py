import random
from example_template import example_template

class Data_sampler():
    def __init__(self, example_template):
        self.example_template = example_template
    
    def generate_data(self, template):
        datatype = template.get("datatype")
        subs = template.get("subs", {})

        result = {
            tuple: (),
            list: [],
            dict: {},
            set: set()
        }[datatype]

        for key, value in subs.items():
            data = self.generate_item(value)
            if datatype == tuple:
                result += (data,)
            elif datatype == list:
                result.append(data)
            elif datatype == dict:
                result[key] = data
            elif datatype == set:
                result.add(data)

        return result

    def generate_item(self, value):
        if "datatype" in value and "datarange" in value:
            if value["datatype"] == int:
                return random.randint(value["datarange"][0], value["datarange"][1])
            elif value["datatype"] == float:
                return random.uniform(value["datarange"][0], value["datarange"][1])
            elif value["datatype"] == str:
                return random.SystemRandom().choice(value['datarange'])
        return self.generate_data(value)


    def dataExtraction(self, num):
        result = []
        for _ in range(num):
            extracted_data = self.generate_data(self.example_template)
            result.append(extracted_data)
        return result

if __name__ == '__main__':

    data_sampler = Data_sampler(example_template)
    extracted_data = data_sampler.dataExtraction(num=3)

    print("Generated random data:")
    for data in extracted_data:
        print(data)
