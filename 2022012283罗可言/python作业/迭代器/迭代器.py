import random
import string
from typing import Any, Callable, Dict, Set, Tuple, Union

# 定义一个装饰器，用于生成随机数据
def random_data_generator(datatype: type, datarange: Union[Tuple[int, int], str], num: int, strlen: int = 10) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(self, *args, **kwargs) -> None:
            result = set()
            for _ in range(num):
                if datatype == int:
                    item = random.randint(datarange[0], datarange[1])
                elif datatype == float:
                    item = random.uniform(datarange[0], datarange[1])
                elif datatype == str:
                    item = ''.join(random.choices(datarange, k=strlen))
                else:
                    raise ValueError("Unsupported data type")
                result.add(item)
            self.sampled_data = result
            return func(self, *args, **kwargs)
        return wrapper
    return decorator

class DataProcessor:
    def __init__(self):
        self.data_range = {
            'name': {'John', 'Smith', 'Peter'},
            'age': {str(age) for age in range(10, 91)},  # 年龄范围10-90
            'id': {''.join(random.choices(string.ascii_letters + string.digits, k=5)) for _ in range(10)}  # 随机生成ID
        }
        self.sampled_data = set()
        self.extracted_data = set()

    # 使用装饰器来生成随机数据
    @random_data_generator(datatype=int, datarange=(10, 100), num=5)
    def dataSampling(self) -> None:
        pass

    # 数据提取方法
    def dataExtraction(self, example: Tuple[str, ...], num: int) -> None:
        result = set()
        for _ in range(num):
            temp = tuple(random.choice(list(self.data_range[key])) for key in example if key in self.data_range)
            result.add(temp)
        self.extracted_data = result

    def __iter__(self):
        return DataIterator(self.extracted_data)

class DataIterator:
    def __init__(self, data: Set[Tuple[str, ...]]) -> None:
        self._data = list(data)
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self) -> Tuple[str, ...]:
        if self._index < len(self._data):
            result = self._data[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration()

if __name__ == '__main__':
    processor = DataProcessor()
    processor.dataSampling()
    print("随机生成的数据集：", processor.sampled_data)

    example = ('name', 'age', 'id')
    processor.dataExtraction(example, num=3)
    print("随机抽取的数据集：")
    for data in processor:
        print(data)
