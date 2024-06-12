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
def genelist(dic):
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
            x = genestruct(value)
            listre.append(x)
        if value.get("datatype") == list:
            x = genestruct(value)
            listre.append(x)
        if value.get("datatype") == dict:
            x = genedic(value)
            listre.append(x)
    return listre


def genetuple(dic):
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
            x = genestruct(value)
            listre.append(x)
        if value.get("datatype") == list:
            x = genestruct(value)
            listre.append(x)
        if value.get("datatype") == dict:
            x = genedic(value)
            listre.append(x)
    tuplere = tuple(listre)
    return tuplere


def genestruct(struct):
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
                x = genelist(value)
                return x
            elif temp == tuple:
                x = genetuple(value)
                return x




def gene(dic, kwdic):
    for key, value in kwdic.items():
        if key == 'int':
            x = random.randint(value.get("datarange")[0], value.get("datarange")[1])
            dic["int"] = x
        elif key == 'float':
            x = random.uniform(value.get("datarange")[0], value.get("datarange")[1])
            dic["float"] = x
        elif key == 'str':
            x = str()
            strlen = value.get("len")
            for j in range(0, strlen):
                y = random.choice(value.get("datarange"))
                x = x + y
            dic["str"] = x
        elif key == 'dict':
            x = genedic(value)
            dic["dict"] = x
        elif key == 'struct':
            x = genestruct(value)
            dic["struct"] = x


def dataSampling2(num, kwargs):
    result = list()
    for i in range(0, num):
        x = genestruct(kwargs)
        result.append(x)
    return result

def sum(dic):
    if type(dic) == tuple:
        return sumtuple(dic)
    if type(dic) == list:
        return sumlist(dic)
    else:
        return dic
def sumtuple(dic):
    result3 = 0.0
    for value in dic:
        if type(value) == int:
            result3 = result3 + value
        if type(value) == float:
            result3 = result3 + value
        if type(value) == str:
            continue
        if type(value) == tuple:
            result3 = result3 + sumtuple(value)
        if type(value) == list:
            result3 = result3 + sumlist(value)
    return result3
def sumlist(dic):
    result3 = 0.0
    for value in dic:
        if type(value) == int:
            result3 = result3 + value
        if type(value) == float:
            result3 = result3 + value
        if type(value) == str:
            continue
        if type(value) == tuple:
            result3 = result3 + sumtuple(value)
        if type(value) == list:
            result3 = result3 + sumlist(value)
    return result3

def sumtimestuple(dic):
    times = 0
    for value in dic:
        if type(value) == int:
            times = times + 1
        elif type(value) == float:
            times = times + 1
        elif type(value) == str:
            continue
        elif type(value) == tuple:
            times = times + sumtimestuple(value)
        elif type(value) == list:
            times = times + sumtimeslist(value)
    return times
def sumtimeslist(dic):
    times = 0
    for value in dic:
        if type(value) == int:
            times = times + 1
        elif type(value) == float:
            times = times + 1
        elif type(value) == str:
            continue
        elif type(value) == dict:
            times = times + sumtimes(value)
        elif type(value) == tuple:
            times = times + sumtimestuple(value)
        elif type(value) == list:
            times = times + sumtimeslist(value)
    return times
def sumtimes(dic):
    times = 0
    for value in dic:
        if type(value) == int:
            times = times + 1
        elif type(value) == float:
            times = times + 1
        elif type(value) == str:
            continue
        elif type(value) == dict:
            times = times + sumtimes(value)
        elif type(value) == tuple:
            times = times + sumtimestuple(value)
        elif type(value) == list:
            times = times + sumtimeslist(value)
    return times


def ave(dic):
    sumnum = sum(dic)
    times = sumtimes(dic)
    return sumnum / times
result = dataSampling2(1,student2)
print(result)
'''调用dataSampling2函数'''