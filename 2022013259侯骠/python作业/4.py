import random

student_data = {'datatype': tuple ,
           'subs': {
               'sub1': {
                   'datatype': list ,
                   'subs': {'sub1': {'datatype': int , 'datarange': [0 , 100]} ,
                            'sub2': {'datatype': str , 'datarange': 'abcd' , 'len': 5}}} ,
               'sub2': {'datatype': tuple ,
                        'subs': {'sub1': {'datatype': float , 'datarange': [0 , 100]} ,
                                 'sub2': {'datatype': int , 'datarange': [0 , 100]}}} ,
               'sub3': {'datatype': str , 'datarange': 'abcdefg' , 'len': 10}
           }
}

student2_data = {'datatype': tuple ,
           'subs': {
               'sub1': {
                   'datatype': list ,
                   'subs': {'sub1': {'datatype': int , 'datarange': [0 , 100]} ,
                            'sub2': {'datatype': str , 'datarange': 'abcd' , 'len': 5}}} ,
               'sub2': {'datatype': tuple ,
                        'subs': {'sub1': {'datatype': tuple , 'subs': {
                            'sub1':{'datatype':int,'datarange':[0,100]},
                            'sub2':{'datatype':float,'datarange':[0,20]}
                        }} ,
                                 'sub2': {'datatype': int , 'datarange': [0 , 100]}}} ,
               'sub3': {'datatype': str , 'datarange': 'abcdefg' , 'len': 10}
           }
}

class NumberGenerator:
    def __init__(self , num , kwargs):
        self.num = num
        self.kwargs = kwargs

    def __iter__(self):
        return self

    def __next__(self):
        tem = 0
        if tem == self.num:
            raise StopIteration
        result = self.data_sampling(1 , self.kwargs)
        tem = tem + 1
        yield result

    def generate_list(self,dic):
        list_result = list()
        for key , value in dic.items():
            if value.get("datatype") == int:
                x = random.randint(value.get("datarange")[0] , value.get("datarange")[1])
                list_result.append(x)
            if value.get("datatype") == float:
                x = random.uniform(value.get("datarange")[0] , value.get("datarange")[1])
                list_result.append(x)
            if value.get("datatype") == str:
                x = str()
                strlen = value.get("len")
                for j in range(0 , strlen):
                    y = random.choice(value.get("datarange"))
                    x = x + y
                list_result.append(x)
            if value.get("datatype") == tuple:
                x = self.generate_structure(value)
                list_result.append(x)
            if value.get("datatype") == list:
                x = self.generate_structure(value)
                list_result.append(x)
            if value.get("datatype") == dict:
                x = self.generate_dictionary(value)
                list_result.append(x)
        return list_result

    def generate_tuple(self,dic):
        list_result = list()
        for key, value in dic.items():
            if value.get("datatype") == int:
                x = random.randint(value.get("datarange")[0], value.get("datarange")[1])
                list_result.append(x)
            if value.get("datatype") == float:
                x = random.uniform(value.get("datarange")[0], value.get("datarange")[1])
                list_result.append(x)
            if value.get("datatype") == str:
                x = str()
                strlen = value.get("len")
                for j in range(0, strlen):
                    y = random.choice(value.get("datarange"))
                    x = x + y
                list_result.append(x)
            if value.get("datatype") == tuple:
                x = self.generate_structure(value)
                list_result.append(x)
            if value.get("datatype") == list:
                x = self.generate_structure(value)
                list_result.append(x)
            if value.get("datatype") == dict:
                x = self.generate_dictionary(value)
                list_result.append(x)
        tuple_result = tuple(list_result)
        return tuple_result

    def generate_structure(self,struct):
        temp = int
        for key, value in struct.items():
            if key == 'datatype':
                temp = value
                continue
            else:
                if temp == int:
                    x = random.randint(value[0], value[1])
                    return x
                elif temp == float:
                    x = random.uniform(value[0], value[1])
                    return x
                elif temp == str:
                    x = str()
                    strlen = value.get("len")
                    for j in range(0, strlen):
                        y = random.choice(value.get("datarange"))
                        x = x + y
                    return x
                elif temp == list:
                    x = self.generate_list(value)
                    return x
                elif temp == tuple:
                    x = self.generate_tuple(value)
                    return x

    def data_sampling(self):
        result = list()
        for i in range(0, self.num):
            x = self.generate_structure(self.kwargs)
            yield x

result = NumberGenerator(5,student2_data)
result2 = result.data_sampling()
for i in result2:
    print(i)
