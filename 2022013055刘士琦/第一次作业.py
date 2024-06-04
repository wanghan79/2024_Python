import random

def dataSampling(**kwargs):
    result = []
    for key,value in kwargs.items():
        if key == 'tuple':
            result.append(tuple(dataSampling(**value)))
        elif key == 'list':
            result.append(list(dataSampling(**value)))
        elif key == 'set':
            result.append(set(dataSampling(**value)))
        elif key == 'int':
            a,b = value['datarange']
            result.append(random.randint(a,b))
        elif key == 'float':
            a,b = value['datarange']
            result.append(random.uniform(a,b))
        elif key == 'str':
            result.append(''.join(random.SystemRandom().choice(value['datarange'])for _ in range(value['len'])))
    return result

my_dict = {
    'num' : 10 ,
    'int' : {'datarange':(5,15)},
    'tuple' : {
        'int' : {'datarange':(0,10)},
        'list' : {
            'int' : {'datarange':(10,15)},
            'float' : {'datarange':(15,20)},
            'str' : {'datarange':'cinmr','len':10}
        },
        'tuple' : {'str' : {'datarange':'ciflskfnmr','len':5}}
    }
}

for i in range(my_dict['num']):
    print(dataSampling(**my_dict))