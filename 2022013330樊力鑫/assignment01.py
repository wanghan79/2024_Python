import string
import random
import warnings


def data_Sampling(**kwargs):
    result = []
    for key, value in kwargs.items():
        if key == 'dataType':
            dataType = value
            if dataType == int:
                daterange = kwargs['datarange']
                result.append(random.randint(daterange[0], daterange[1]))

            elif dataType == float:
                daterange = kwargs['datarange']
                result.append(random.uniform(daterange[0], daterange[1]))

            elif dataType == str:
                datarange = kwargs['datarange']
                result.append(''.join(random.choice(datarange) for _ in range(kwargs['len'])))

            elif dataType == bool:
                result.append(random.choice([True, False]))

            elif dataType == list:
                datarange = kwargs['datarange']
                result.append([random.randint(0, 100) for _ in range(datarange)])

            elif dataType == tuple:
                subs = kwargs['subs']
                result.append(tuple(data_Sampling(**sub) for sub in subs.values()))

    return result


# 使用函数
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
                },
            },
        },
    },
}

warnings.warn("warning:please change the data_structure into what you need before running in file.")
times = int(input("请输入需要生成的数据组数："))

for _ in range(times):
    print(data_Sampling(**data_structure))
