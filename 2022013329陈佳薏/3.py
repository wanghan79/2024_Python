import random
import string
import re
#样本的格式实例为：
'''example={
    "datatype":tuple,
    "subs":{
        "sub1":{"datatype":list,
                "subs":{
                    "sub1":{
                        "datatype":int,
                        "datarange":(0,100)
                    },
                    "sub2":{
                        "datatype":float,
                        "datarange":(0,100)
                    },
                    "sub3":{
                        "datatype":str,
                        "datarange":string.ascii_uppercase, 
                        "len": 5
                    }
                },
        },
        "sub2":{"datatype":tuple,
                "subs":{
                    "sub1":{
                        "datatype":int,
                        "datarange":(0,100)
                    },
                    "sub2":{
                        "datatype":str,
                        "datarange":string.ascii_uppercase, 
                        "len": 5
                    }
                },
        },
        "sub3":{
            "datatype":str,
            "datarange":string.ascii_uppercase, 
            "len": 5
        }
    }
}'''
def sum(content):
    nums=re.findall(r'\d+\.\d+|\d+', content)
    sum=0
    for num in nums:
        sum+=float(num)
    return sum
def average(content):
    nums=re.findall(r'\d+\.\d+|\d+', content)
    numsLen=len(nums)
    avr=sum(content)/numsLen
    return avr
def sum_or_average(*decPara):
    def decorater(func):
        def wrapper(**kwargs):
            result=func(**kwargs)
            print(result)
            content=str(result)
            decPaLen=len(decPara)
            if decPaLen==1:
                if decPara[0]=='sum':
                    print("sum equal to %f" % sum(content))
                elif decPara[0]=='average':
                    print("average equal to %f" % average(content))
                else:
                    print("parameter error")
            elif decPaLen==2:
                condition1=decPara[0]=='sum' and decPara[1]=='average'
                condition2=decPara[1]=='sum' and decPara[0]=='average'
                if condition1 or condition2:
                    print("sum equal to %f" % sum(content))
                    print("average equal to %f" % average(content))
            else:
                print("parameter error")
            return result
        return wrapper
    return decorater

#修饰器参数为"average"则会输出平均值，为"sum"则会输出和，还可以有两个参数，则会输出平均值与和
@sum_or_average("sum")
def data_sampling(**kwargs):
    def _data_sampling(**kwargs):
        result = list()
        sample=iter(kwargs)
        name=next(sample)
        if(name=="example"):
            result=_data_sampling(**kwargs[name]) 
        elif(re.match('^sub\\d+',name)!=None):
            example=iter(kwargs)
            while True:
                try:
                    name1=next(example)
                    result.append(_data_sampling(**kwargs[name1])[0])
                except StopIteration:
                    break
        else:
            example=iter(kwargs)
            while True:
                try:
                    name1=next(example)
                    type=kwargs[name1]
                    if type is int:
                        name2=next(example)
                        result.append(basic_data_create(type, kwargs[name2],0))
                    elif type is float:
                        name2=next(example)
                        result.append(basic_data_create(type, kwargs[name2],0))
                    elif type is str:
                        name2=next(example)
                        name3=next(example)
                        result.append(basic_data_create(type, kwargs[name2],kwargs[name3]))
                    elif type is list:
                        name2=next(example)
                        result.append(_data_sampling(**kwargs[name2]))
                    elif type is tuple:
                        name2=next(example)
                        result.append(tuple(_data_sampling(**kwargs[name2])))
                except StopIteration:
                    break
        return result
    return _data_sampling(**kwargs)
def basic_data_create(datatype,datarange,len):
    if datatype is int:
        it = iter(datarange)
        item = random.randint(next(it), next(it))
        return item
    elif datatype is float:
        it = iter(datarange)
        item = random.uniform(next(it), next(it))
        return item
    elif datatype is str:
        item = ''.join(random.SystemRandom().choice(datarange) for _ in range(len))
        return item
    else:
        return "error"

data_sampling(example={
    "datatype":tuple,
    "subs":{
        "sub1":{"datatype":list,
                "subs":{
                    "sub1":{
                        "datatype":int,
                        "datarange":(0,100)
                    },
                    "sub2":{
                        "datatype":float,
                        "datarange":(0,100)
                    },
                    "sub3":{
                        "datatype":str,
                        "datarange":string.ascii_uppercase, 
                        "len": 5
                    }
                },
        },
        "sub2":{"datatype":tuple,
                "subs":{
                    "sub1":{
                        "datatype":int,
                        "datarange":(0,100)
                    },
                    "sub2":{
                        "datatype":str,
                        "datarange":string.ascii_uppercase, 
                        "len": 5
                    }
                },
        },
        "sub3":{
            "datatype":str,
            "datarange":string.ascii_uppercase, 
            "len": 5
        }
    }
})


