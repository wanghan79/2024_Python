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
class RandomClass():
    def __init__(self,**kwargs):
        if kwargs:
            self.data=self.data_sampling(**kwargs)[0]
        else:
            self.data='you should input kwargs'
            
    def sum(self):
        content=str(self.data)
        nums=re.findall(r'\d+\.\d+|\d+',content)
        sum=0
        for num in nums:
            sum+=float(num)
        return sum
    
    def average(self):
        content=str(self.data)
        nums=re.findall(r'\d+\.\d+|\d+', content)
        numsLen=len(nums)
        avr=self.sum()/numsLen
        return avr

    def data_sampling(self,**kwargs):
        result = list()
        sample=iter(kwargs)
        name=next(sample)
        if(name=="example"):
            result=self.data_sampling(**kwargs[name]) 
        elif(re.match(r'^sub\d+',name)!=None):
            example=iter(kwargs)
            while True:
                try:
                    name1=next(example)
                    result.append(self.data_sampling(**kwargs[name1])[0])
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
                        result.append(self.basic_data_create(type, kwargs[name2],0))
                    elif type is float:
                        name2=next(example)
                        result.append(self.basic_data_create(type, kwargs[name2],0))
                    elif type is str:
                        name2=next(example)
                        name3=next(example)
                        result.append(self.basic_data_create(type, kwargs[name2],kwargs[name3]))
                    elif type is list:
                        name2=next(example)
                        result.append(self.data_sampling(**kwargs[name2]))
                    elif type is tuple:
                        name2=next(example)
                        result.append(tuple(self.data_sampling(**kwargs[name2])))
                except StopIteration:
                    break
        return result
    
    def basic_data_create(self,datatype,datarange,len):
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
        
#类里面data变量即为生成的随机值，sum方法为数字总和，average方法为数字平均值
x=RandomClass(example={
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
        },
        "sub4":{"datatype":list,
                "subs":{
                    "sub1":{
                        "datatype":int,
                        "datarange":(0,100)
                    },
                    "sub2":{
                        "datatype":int,
                        "datarange":(0,100)
                    },
                    "sub3":{
                        "datatype":str,
                        "datarange":string.ascii_uppercase, 
                        "len": 5
                    }
                },
        }
    }
})
print(x.data)
print(x.sum())
print(x.average())
