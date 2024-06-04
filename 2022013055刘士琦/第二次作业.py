import random


class Sampling:
    data = []
    @staticmethod
    def dataSampling(**kwargs):
        result = []
        for key, value in kwargs.items():
            if key == 'tuple':
                result.append(tuple(Sampling.dataSampling(**value)))
            elif key == 'list':
                result.append(list(Sampling.dataSampling(**value)))
            elif key == 'set':
                result.append(set(Sampling.dataSampling(**value)))
            elif key == 'int':
                a, b = value['datarange']
                randInt = random.randint(a, b)
                result.append(randInt)
                Sampling.data.append(randInt)
            elif key == 'float':
                a, b = value['datarange']
                randFloat = random.uniform(a, b)
                result.append(randFloat)
                Sampling.data.append(randFloat)
            elif key == 'str':
                result.append(''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len'])))
        return result

    @classmethod
    def analysis(cls, *args):
        dataSum = sum(Sampling.data)
        if len(Sampling.data) > 0:
            dataAve = dataSum / len(Sampling.data)
        else:
            dataAve = 0
        if 'sum' in args:
            print("数据的和为：", dataSum)
        if 'average' in args:
            print("数据的平均值为：", dataAve)



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
    print(Sampling.dataSampling(**my_dict))
    print("得到的数据为：")
    for x in Sampling.data:
        print(x)
    # Sampling.analysis('sum')
    # Sampling.analysis('average')
    Sampling.analysis('sum', 'average')
    Sampling.data = []
    print("********")
