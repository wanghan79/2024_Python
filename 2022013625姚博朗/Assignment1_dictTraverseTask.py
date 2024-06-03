import random



def get_random(**kwargs):
    result = []
    for key, value in kwargs.items():
        if key == 'tuple':
            result.append(tuple(get_random(**value)))
        elif key == 'list':
            result.append(list(get_random(**value)))
        elif key == 'set':
            result.append(set(get_random(**value)))
        elif key == 'int':
            a, b = value['datarange']
            result.append(random.randint(a, b))
        elif key == 'float':
            a, b = value['datarange']
            result.append(random.uniform(a, b))
        elif key == 'str':
            datarange = value["datarange"]
            datalength = value["datalength"]
            result.append(''.join(random.choice(datarange) for _ in range(datalength)))
        else:
            print("This is an undefined type")
            result.append("********")
    return result

def get_sample(**kwargs):
    global num
    dc=dict()
    for k,v in kwargs.items():
        if k == 'num':
            num=v
        else:
            dc[k]=v
    result = []
    for _ in range(int (num)):
        result.append(get_random(**dc))
    return result


my_dict = {
        'tuple': {
            'int': {
                'datarange': [1, 10]
            },
            'float': {
                'datarange': [100, 1000]
            },
            'list': {
                'int': {
                    'datarange': [1, 50]
                },
                'float': {
                    'datarange': [1, 10]
                },
                'str': {
                    'datarange': "abcefghijklmnopqrstuvwxyz",
                    "datalength": 6
                },
                'tuple': {
                    'str': {
                        'datarange': "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                        "datalength": 6
                    }
                }
            }
        }
    }


print(get_sample(**my_dict))
