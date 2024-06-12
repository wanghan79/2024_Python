import random
import string
from typing import Any, Dict, Set, Tuple, Union

class RandomDataGenerator:
    def __init__(self, data_range: Dict[str, Set[str]]):
        self.data_range = data_range

    def generate_random_data(self, datatype: type, datarange: Union[Tuple[int, int], str], num: int, strlen: int = 10) -> Set[Any]:
        result = set()
        for _ in range(num):
            if datatype == int:
                item = random.randint(datarange[0], datarange[1])
            elif datatype == float:
                item = random.uniform(datarange[0], datarange[1])
            elif datatype == str:
                item = ''.join(random.choices(string.ascii_letters, k=strlen))
            else:
                raise ValueError("Unsupported data type")
            result.add(item)
        return result

    def data_extraction(self, example: Tuple[str, ...], num: int) -> Set[Tuple[str, ...]]:
        result = set()
        for _ in range(num):
            temp = []
            for key in example:
                if key in self.data_range:
                    item = random.choice(list(self.data_range[key]))
                    temp.append(item)
            result.add(tuple(temp))
        return result

if __name__ == '__main__':
    data_range = {
        'name': {'John', 'Smith', 'Peter'},
        'age': {'20', '18', '22', '9'},
        'id': {'1', '2', '3'}
    }
    generator = RandomDataGenerator(data_range)

    # 随机生成的数据集
    sampled_data = generator.generate_random_data(datatype=int, datarange=(10, 100), num=5)
    print("随机生成的数据集：", sampled_data)

    example = ('name', 'age', 'id')
    # 随机抽取的数据集
    extracted_data = generator.data_extraction(example, num=3)
    print("随机抽取的数据集：")
    for data in extracted_data:
        print(data)
