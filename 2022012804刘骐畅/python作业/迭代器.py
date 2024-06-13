import random
import string
from typing import Any, Dict, Set, Tuple, Union

class DataExtractionIterator:
    def __init__(self, data_range: Dict[str, Set[str]], example: Tuple[str, ...], num: int):
        self.data_range = data_range
        self.example = example
        self.num = num
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # 检查是否还有数据可以生成
        if self.current_index < self.num:
            self.current_index += 1
            # 生成数据
            return tuple(random.choice(list(self.data_range[key])) for key in self.example if key in self.data_range)
        else:
            # 所有数据已生成，触发停止迭代异常
            raise StopIteration

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

def data_extraction(data_range: Dict[str, Set[str]], example: Tuple[str, ...], num: int) -> DataExtractionIterator:
    return DataExtractionIterator(data_range, example, num)

if __name__ == '__main__':
    # 随机生成的数据集
    sampled_data = generate_random_data(datatype=int, datarange=(10, 100), num=5)
    print("随机生成的数据集：", sampled_data)

    # 定义数据范围
    data_range = {
        'name': {'Tudou', 'AAA', 'BBB'},
        'age': {str(age) for age in range(1, 101)},
        'id': {''.join(random.choices(string.ascii_letters + string.digits, k=5)) for _ in range(10)}
    }
    example = ('name', 'age', 'id')

    # 使用数据提取器生成数据
    extracted_data = data_extraction(data_range, example, num=3)
    print("随机抽取的数据集：")
    for data in extracted_data:
        print(data)
