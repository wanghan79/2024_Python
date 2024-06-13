import random
import string

class RandomDataGenerator:
    def __init__(self):
        pass

    def generate_random_string(self, length):
        """生成指定长度的随机字符串"""
        char_set = string.ascii_letters
        return ''.join(random.choice(char_set) for _ in range(length))

    def generate_random_integer(self, min_val, max_val):
        """生成指定范围内的随机整数"""
        return random.randint(min_val, max_val)

    def generate_random_float(self, min_val, max_val):
        """生成指定范围内的随机浮点数"""
        return random.uniform(min_val, max_val)

    def produce_random_data(self, specification):
        """根据数据规格生成随机数据"""
        if isinstance(specification, dict) and 'type' in specification:
            data_type = specification['type']
            if data_type == 'string':
                return self.generate_random_string(specification['length'])
            elif data_type == 'int':
                return self.generate_random_integer(specification['min'], specification['max'])
            elif data_type == 'float':
                return self.generate_random_float(specification['min'], specification['max'])
            elif data_type == 'list':
                list_length = specification['length']
                item_spec = specification['item']
                return [self.produce_random_data(item_spec) for _ in range(list_length)]
        elif isinstance(specification, dict):
            generated_data = {}
            for key, value in specification.items():
                generated_data[key] = self.produce_random_data(value)
            return generated_data
        else:
            raise ValueError("Invalid structure format")

# 数据规格
schema = {
    "name": {"type": "string", "length": 10},
    "age": {"type": "int", "min": 18, "max": 99},
    "address": {
        "street": {"type": "string", "length": 15},
        "city": {"type": "string", "length": 10},
        "zipcode": {"type": "int", "min": 10000, "max": 99999}
    },
    "scores": {"type": "list", "length": 5, "item": {"type": "float", "min": 0.0, "max": 100.0}}
}

# 生成随机数据
generator = RandomDataGenerator()
generated_random_data = generator.produce_random_data(schema)
print(generated_random_data)
