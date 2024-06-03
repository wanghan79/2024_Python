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
def data_sampling(n,**kwargs):
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
    num=0
    while num<n:
        yield _data_sampling(**kwargs)[0]
        num=num+1
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
    
#第一个参数决定生成几个，第二个键值对参数是样本模版
result=data_sampling(7,example={
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
for x in result:
    print(x)


