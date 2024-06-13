import random
import string


class RandomContentCreator:
    def __init__(self, blueprint):
        self.blueprint = blueprint

    def _create_random_string(self, size):
        """生成指定长度的随机字符串"""
        available_chars = string.ascii_letters
        return ''.join(random.choice(available_chars) for _ in range(size))

    def _create_random_integer(self, min_limit, max_limit):
        """生成指定范围内的随机整数"""
        return random.randint(min_limit, max_limit)

    def _create_random_float(self, min_limit, max_limit):
        """生成指定范围内的随机浮点数"""
        return random.uniform(min_limit, max_limit)

    def _generate_from_blueprint(self, blueprint=None):
        """根据蓝图生成随机数据"""
        if blueprint is None:
            blueprint = self.blueprint

        if isinstance(blueprint, dict) and 'type' in blueprint:
            if blueprint['type'] == 'string':
                return self._create_random_string(blueprint['length'])
            elif blueprint['type'] == 'int':
                return self._create_random_integer(blueprint['min'], blueprint['max'])
            elif blueprint['type'] == 'float':
                return self._create_random_float(blueprint['min'], blueprint['max'])
            elif blueprint['type'] == 'list':
                length = blueprint['length']
                item_blueprint = blueprint['item']
                return [self._generate_from_blueprint(item_blueprint) for _ in range(length)]
        elif isinstance(blueprint, dict):
            data_block = {}
            for key, value in blueprint.items():
                data_block[key] = self._generate_from_blueprint(value)
            return data_block
        else:
            raise ValueError("不支持的蓝图格式")

# 数据蓝图
data_blueprint = {
    "name": {"type": "string", "length": 10},
    "age": {"type": "int", "min": 18, "max": 99},
    "address": {
        "street": {"type": "string", "length": 15},
        "city": {"type": "string", "length": 10},
        "zipcode": {"type": "int", "min": 10000, "max": 99999}
    },
    "scores": {"type": "list", "length": 5, "item": {"type": "float", "min": 0.0, "max": 100.0}}
}

# 创建随机内容生成器实例并生成随机数据
creator = RandomContentCreator(data_blueprint)

for _ in range(10):
    random_content = creator._generate_from_blueprint()
    print(random_content)
