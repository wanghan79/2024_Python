import random
student = {'datatype': tuple ,
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
student2 = {'datatype': tuple ,
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
class number:
    def __init__(self , num , kwargs):
        self.num = num
        self.kwargs = kwargs

    def __iter__(self):
        return self

    def __next__(self):
        tem = 0
        if tem == self.num:
            raise StopIteration
        result = self.dataSampling2(1 , self.kwargs)
        tem = tem + 1
        yield result
    def genelist(self,dic):
        listre = list()
        for key , value in dic.items():
            if value.get("datatype") == int:
                x = random.randint(value.get("datarange")[0] , value.get("datarange")[1])
                listre.append(x)
            if value.get("datatype") == float:
                x = random.uniform(value.get("datarange")[0] , value.get("datarange")[1])
                listre.append(x)
            if value.get("datatype") == str:
                x = str()
                strlen = value.get("len")
                for j in range(0 , strlen):
                    y = random.choice(value.get("datarange"))
                    x = x + y
                listre.append(x)
            if value.get("datatype") == tuple:
                x = self.genestruct(value)
                listre.append(x)
            if value.get("datatype") == list:
                x = self.genestruct(value)
                listre.append(x)
            if value.get("datatype") == dict:
                x = self.genedic(value)
                listre.append(x)
        return listre
    def genetuple(self,dic):
        listre = list()
        for key, value in dic.items():
            if value.get("datatype") == int:
                x = random.randint(value.get("datarange")[0], value.get("datarange")[1])
                listre.append(x)
            if value.get("datatype") == float:
                x = random.uniform(value.get("datarange")[0], value.get("datarange")[1])
                listre.append(x)
            if value.get("datatype") == str:
                x = str()
                strlen = value.get("len")
                for j in range(0, strlen):
                    y = random.choice(value.get("datarange"))
                    x = x + y
                listre.append(x)
            if value.get("datatype") == tuple:
                x = self.genestruct(value)
                listre.append(x)
            if value.get("datatype") == list:
                x = self.genestruct(value)
                listre.append(x)
            if value.get("datatype") == dict:
                x = self.genedic(value)
                listre.append(x)
        tuplere = tuple(listre)
        return tuplere
    def genestruct(self,struct):
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
                    '''for keys,values in value.items():'''
                    x = self.genelist(value)
                    return x
                elif temp == tuple:
                    x = self.genetuple(value)
                    return x
    def dataSampling2(self):
        result = list()
        for i in range(0, self.num):
            x = self.genestruct(self.kwargs)
            yield x
    def sum(self,dic):
        if type(dic) == tuple:
            return self.sumtuple(dic)
        if type(dic) == list:
            return self.sumlist(dic)
        else:
            return dic
    def sumtuple(self,dic):
        result3 = 0.0
        for value in dic:
            if type(value) == int:
                print()
                result3 = result3 + value
            elif type(value) == float:
                result3 = result3 + value
            elif type(value) == str:
                continue
            elif type(value) == tuple:
                result3 = result3 + self.sumtuple(value)
            elif type(value) == list:
                result3 = result3 + self.sumlist(value)
        return result3
    def sumlist(self,dic):
        result3 = 0.0
        for value in dic:
            if type(value) == int:
                result3 = result3 + value
            elif type(value) == float:
                result3 = result3 + value
            elif type(value) == str:
                continue
            elif type(value) == tuple:
                result3 = result3 + self.sumtuple(value)
            elif type(value) == list:
                result3 = result3 + self.sumlist(value)
        return result3

    def sumtimestuple(self,dic):
        times = 0
        for value in dic:
            if type(value) == int:
                times = times + 1
            elif type(value) == float:
                times = times + 1
            elif type(value) == str:
                continue
            elif type(value) == tuple:
                times = times + self.sumtimestuple(value)
            elif type(value) == list:
                times = times + self.sumtimeslist(value)
        return times
    def sumtimeslist(self,dic):
        times = 0
        for value in dic:
            if type(value) == int:
                times = times + 1
            elif type(value) == float:
                times = times + 1
            elif type(value) == str:
                continue
            elif type(value) == dict:
                times = times + self.sumtimes(value)
            elif type(value) == tuple:
                times = times + self.sumtimestuple(value)
            elif type(value) == list:
                times = times + self.sumtimeslist(value)
        return times
    def sumtimes(self,dic):
        times = 0
        for value in dic:
            if type(value) == int:
                times = times + 1
            elif type(value) == float:
                times = times + 1
            elif type(value) == str:
                continue
            elif type(value) == dict:
                times = times + self.sumtimes(value)
            elif type(value) == tuple:
                times = times + self.sumtimestuple(value)
            elif type(value) == list:
                times = times + self.sumtimeslist(value)
        return times
    def ave(self,dic):
        sumnum = sum(dic)
        times = self.sumtimes(dic)
        return sumnum / times

result = number(5,student2)
result2 = result.dataSampling2()
for i in result2:
    print(i)