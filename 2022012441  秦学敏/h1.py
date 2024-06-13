import string
import random
import warnings


class DataSampler:
    def __init__(self):
        self.datatypes = {
            int: self._generate_int,
            float: self._generate_float,
            str: self._generate_str,
            bool: self._generate_bool,
            list: self._generate_list,
            tuple: self._generate_tuple,
        }

    def sample(self, data_structure):
        if isinstance(data_structure, dict):
            data_type = data_structure.get('dataType')
            if data_type in self.datatypes:
                return self.datatypes[data_type](data_structure)
            else:
                raise ValueError(f"Unsupported data type: {data_type}")
        else:
            raise ValueError("Data structure should be a dict.")

    def _generate_int(self, data_structure):
        return random.randint(data_structure['range'][0], data_structure['range'][1])

    def _generate_float(self, data_structure):
        return random.uniform(data_structure['range'][0], data_structure['range'][1])

    def _generate_str(self, data_structure):
        # 假设有一个'length'键表示字符串长度
        length = data_structure.get('length', 10)  # 默认长度为10
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def _generate_bool(self, data_structure):
        # 可以直接返回True或False，不需要额外的data_structure信息
        return random.choice([True, False])

    def _generate_tuple(self, data_structure):
        subs = data_structure['subs']
        return tuple(self.sample(sub) for sub in subs.values())
        # 其他数据类型的方法


# 使用类
data_structure = {
    'dataType': 'tuple',
    'subs': {
        'int_val': {'dataType': 'int', 'range': [1, 100]},
        'float_val': {'dataType': 'float', 'range': [0.0, 1.0]},
        'str_val': {'dataType': 'str', 'length': 5},
        # 其他可能的子数据结构

    }
}

warnings.warn("warning: please change the data_structure into what you need before running in file.")
times = int(input("请输入需要生成的数据组数："))

sampler = DataSampler()
for _ in range(times):
    print(sampler.sample(data_structure))