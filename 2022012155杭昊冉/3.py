import random
import string
from functools import wraps


class RandomDataGenerator:
    def __init__(self, schema):
        self.schema = schema
        self.counts = {
            'string': 0,
            'int': 0,
            'float': 0,
            'list': 0
        }

    def _increment_count(self, data_type):
        """增加指定类型的计数器"""
        self.counts[data_type] += 1

    def _generate_random_string(self, length):
        """生成指定长度的随机字符串"""
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))

    def _generate_random_int(self, min_val, max_val):
        """生成指定范围内的随机整数"""
        return random.randint(min_val, max_val)

    def _generate_random_float(self, min_val, max_val):
        """生成指定范围内的随机浮点数"""
        return random.uniform(min_val, max_val)

    def generate_random_data(self, schema=None):
        """根据提供的schema生成随机数据"""
        if schema is None:
            schema = self.schema

        if isinstance(schema, dict) and 'type' in schema:
            if schema['type'] == 'string':
                self._increment_count('string')
                return self._generate_random_string(schema['length'])
            elif schema['type'] == 'int':
                self._increment_count('int')
                return self._generate_random_int(schema['min'], schema['max'])
            elif schema['type'] == 'float':
                self._increment_count('float')
                return self._generate_random_float(schema['min'], schema['max'])
            elif schema['type'] == 'list':
                length = schema['length']
                item_schema = schema['item']
                result = [self.generate_random_data(item_schema) for _ in range(length)]
                self._increment_count('list')
                return result
        elif isinstance(schema, dict):
            data = {}
            for key, value in schema.items():
                data[key] = self.generate_random_data(value)
            return data
        else:
            raise ValueError("Unsupported schema format")

# 数据结构
data_schema = {
    "name": {"type": "string", "length": 10},
    "age": {"type": "int", "min": 18, "max": 99},
    "address": {
        "street": {"type": "string", "length": 15},
        "city": {"type": "string", "length": 10},
        "zipcode": {"type": "int", "min": 10000, "max": 99999}
    },
    "scores": {"type": "list", "length": 5, "item": {"type": "float", "min": 0.0, "max": 100.0}}
}

# 创建RandomDataGenerator实例并生成随机数据
generator = RandomDataGenerator(data_schema)
random_data = generator.generate_random_data()
print(random_data)
print(generator.counts)
