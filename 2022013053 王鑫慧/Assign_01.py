import string
import random



def data_Sampling(**kwargs):
    result = []
    for key, value in kwargs.items():
        if key == 'dataType':
            dataType = value
            if dataType == int:
                daterange = kwargs['datarange']
                result.append(("int", random.randint(daterange[0], daterange[1])))

            elif dataType == float:
                daterange = kwargs['datarange']
                result.append(("float", random.uniform(daterange[0], daterange[1])))

            elif dataType == str:
                datarange = kwargs['datarange']
                result.append(("string", ''.join(random.choice(datarange) for _ in range(kwargs['len']))))

            elif dataType == bool:
                result.append(("bool", random.choice([True, False])))

            elif dataType == list:
                datarange = kwargs['datarange']
                result.append(("list", [random.randint(0, 100) for _ in range(datarange)]))

            elif dataType == tuple:
                subs = kwargs['subs']
                result.append(("tuple", tuple(data_Sampling(**sub) for sub in subs.values())))

    return result

# 定义数据结构的形式
data_structure = {
    "dataType": tuple,
    "subs": {
        "sub1": {
            "dataType": str,
            "datarange": string.ascii_letters,
            "len": 5
        },
        "sub2": {
            "dataType": tuple,
            "subs": {
                "sub1": {
                    "dataType": int,
                    "datarange": (0, 100),
                },
                "sub2": {
                    "dataType": list,
                    "datarange": 5,
                    "subs": {
                        "elem": {
                            "dataType": float,
                            "datarange": (0.0, 100.0)
                        }
                    }
                },
                "sub3": {
                    "dataType": float,
                    "datarange": (0.0, 10.0),
                },

            }
        }
    }
}

def format_data(data):
    if isinstance(data, tuple):
        return f"({data[0]}[{data[1]}])"
    elif isinstance(data, list):
        return "[" + ", ".join(format_data(item) for item in data) + "]"
    else:
        return str(data)



times = random.randint(1, 5)
# 生成随机个数个这样的随机数据结构
for _ in range(times):
    formatted_data = format_data(data_Sampling(**data_structure))
    print(formatted_data)