import random
import string
from typing import Any, Dict, Set, Tuple, Union


def generate_random_data(datatype: type, datarange: Union[Tuple[int, int], Tuple[float, float]], num: int, strlen: int = 10) -> Set[Any]:
    result = set()
    for _ in range(num):
        if datatype == int:
            item = random.randint(datarange[0], datarange[1])
        elif datatype == float:
            item = random.uniform(datarange[0], datarange[1])
        elif datatype == str:
            item = ''.join(random.choices(string.ascii_letters + string.digits, k=strlen))
        else:
            raise ValueError("Unsupported data type")
        result.add(item)
    return result


def data_extraction(data_range: Dict[str, Set[str]], example: Tuple[str, ...], num: int) -> Set[Tuple[str, ...]]:
    result = set()
    for _ in range(num):
        try:
            temp = tuple(random.choice(list(data_range[key])) for key in example if key in data_range)
            result.add(temp)
        except KeyError as e:
            print(f"Key error: {e}")
        except IndexError as e:
            print(f"Index error: {e}")
    return result


if __name__ == '__main__':
    # 随机生成的数据集
    sampled_data = generate_random_data(datatype=int, datarange=(10, 100), num=5)
    print("随机生成的数据集：", sampled_data)

    # 定义数据范围
    data_range = {
        'name': {'John', 'Smith', 'Peter'},
        'age': {str(age) for age in range(10, 91)},  # 年龄范围10-90
        'id': {''.join(random.choices(string.ascii_letters + string.digits, k=5)) for _ in range(10)}  # 随机生成ID
    }
    example = ('name', 'age', 'id')

    # 随机抽取的数据集
    extracted_data = data_extraction(data_range, example, num=3)
    print("随机抽取的数据集：")
    for data in extracted_data:
        print(data)
