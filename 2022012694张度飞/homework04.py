import random

class Data_sampler():
    def __init__(self, data_structure):
        self.data_structure = data_structure

    def __str__(self):
        print('<Class Data_sampler>')
        print('data_structure:',self.data_structure)

    def gen_random_data(self, data_structure):
        if data_structure["datatype"] == tuple:
            res = ()
        elif data_structure["datatype"] == list:
            res = []

        for _, value in data_structure["subs"].items():
            if "data_range" in value:
                if value["datatype"] == str:
                    random_data = random.SystemRandom().choice(value['data_range'])
                elif value["datatype"] == int:
                    random_data = random.randint(value["data_range"][0], value["data_range"][1])
            else:
                random_data = self.gen_random_data(value)

            if isinstance(res, tuple):
                res += (random_data,)
            elif isinstance(res, list):
                res.append(random_data)

        return res
    
    def gen_multi_random_data(self, num=10):
        res = []

        for _ in range(10):
            res.append(self.gen_random_data(self.data_structure))
        
        return res


def data_generator(data_sampler:Data_sampler):
        try:
            while True:
                yield data_sampler.gen_random_data(data_structure=data_sampler.data_structure)
        except:
            return 0
        

if __name__ == '__main__':
    data_structure = {
        "datatype":list,
        "subs": {
            "sub1":{
                "datatype":tuple,
                "subs":{
                    "name":{
                        "datatype":str,
                        "data_range":['aaa', 'bbb', 'ccc', 'ddd', 'eee']
                    },
                    "age": {
                        "datatype": int,
                        "data_range": (18,24)
                    },
                }
            },

        "sub2": {
                "datatype": tuple,
                "subs": {
                    "course": {
                        "datatype": str,
                        "data_range": [
                            "Introduction to Computer Science",
                            "Data Structures and Algorithms",
                            "Database Systems",
                            "Computer Architecture",
                            "Operating Systems",
                            "Networks and Communications",
                            "Software Engineering",
                            "Artificial Intelligence",
                            "Machine Learning"
                        ]
                    },
                    "score": {
                        "datatype": int,
                        "data_range":(60,100)
                    }
                }
            }
        }
    }

data_sampler = Data_sampler(data_structure)
iter = data_generator(data_sampler)

for _ in range(10):
    print(next(iter))
