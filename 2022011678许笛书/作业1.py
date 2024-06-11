import random


def dataSampling(datatype, datarange, num, strlen=8):
    """

    :Description: Generate a given condition random data set.
    :param datatype:
    :param datarange:
    :param num:
    :param strlen:
    :return:
    """

    result = set()
    for index in range(0, num):
        if datatype is int:
            it = iter(datarange)
            item = random.randint(next(it), next(it))
            result.add(item)
            continue
        elif datatype is float:
            it = iter(datarange)
            item = random.uniform(next(it), next(it))
            result.add(item)
            continue
        elif datatype is str:
            item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
            result.add(item)
            continue
        else:
            continue
    return result

random_data_int = dataSampling(int, (1, 100), 10)
print(random_data_int)

random_data_float = dataSampling(float, (0.1, 0.9), 5)
print(random_data_float)

random_data_str = dataSampling(str, ('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'),3 , 10)
print(random_data_str)


def listSampling(data_type, num_list, name, id_range, grade_range,strlen):
    """

    :param data_type:
    :param num_list:
    :param name:
    :param id_range:
    :param grade_range:
    :return:
    """
    result = set()
    for index in range(0, num_list):
        if data_type is list:
            # name
            item1 = ''.join(random.SystemRandom().choice(name) for _ in range(strlen))
            result.add(item1)
            # id
            it = iter(id_range)
            item2 = random.randint(next(it), next(it))
            result.add(item2)
            # grade
            it = iter(grade_range)
            item3 = random.uniform(next(it), next(it))
            result.add(item3)
            continue
        elif data_type is tuple:
            # name
            item1 = ''.join(random.SystemRandom().choice(name) for _ in range(strlen))
            result.add(item1)
            # id
            it = iter(id_range)
            item2 = random.randint(next(it), next(it))
            result.add(item2)
            # grade
            it = iter(grade_range)
            item3 = random.uniform(next(it), next(it))
            result.add(item3)
            continue
        else:
            continue
    return result

random_data_list = listSampling(list, 1, ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'), (1,10), (0, 100), 5)
print(random_data_list)

random_data_tuple = listSampling(tuple, 5, ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'), (1,20), (0, 100), 5)
print(random_data_tuple)
