import random
import string

class DataRandomizer:
    def __init__(self, schema):
        self.schema = schema

    def _create_random_string(self, length):
        """生成指定长度的随机字符串"""
        characters = string.ascii_letters
        return ''.join(random.choice(characters) for _ in range(length))

    def _create_random_integer(self, min_value, max_value):
        """生成指定范围内的随机整数"""
        return random.randint(min_value, max_value)

    def _create_random_float(self, min_value, max_value):
        """生成指定范围内的随机浮点数"""
        return random.uniform(min_value, max_value)

    def _produce_random_data(self, schema=None):
        """根据提供的schema生成随机数据"""
        if schema is None:
            schema = self.schema

        if isinstance(schema, dict) and 'type' in schema:
            data_type = schema['type']
            if data_type == 'string':
                return self._create_random_string(schema['length'])
            elif data_type == 'int':
                return self._create_random_integer(schema['min'], schema['max'])
            elif data_type == 'float':
                return self._create_random_float(schema['min'], schema['max'])
            elif data_type == 'list':
                list_length = schema['length']
                item_schema = schema['item']
                return [self._produce_random_data(item_schema) for _ in range(list_length)]
        elif isinstance(schema, dict):
            generated_data = {}
            for key, value in schema.items():
                generated_data[key] = self._produce_random_data(value)
            return generated_data
        else:
            raise ValueError("Unsupported schema format")

# 定义数据schema
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

# 创建DataRandomizer实例并生成随机数据
randomizer = DataRandomizer(data_schema)
randomized_data = randomizer._produce_random_data()
print(randomized_data)
