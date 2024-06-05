import random
import string

class RandomData:
    def __init__(self):
        self.result = []

    def randomInt(self, min_val, max_val):
        """生成一个指定范围内的随机整数"""
        return random.randint(min_val, max_val)

    def randomFloat(self, min_val, max_val):
        """生成一个指定范围内的随机浮点数"""
        return random.uniform(min_val, max_val)

    def randomStr(self, length):
        """生成一个指定长度的随机字符串"""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def randomList(self, element_spec, size):
        """生成一个包含指定数量随机元素的列表"""
        return [self.generate(element_spec) for _ in range(size)]

    def randomTuple(self, *element_specs):
        """生成一个包含随机元素的元组"""
        return (self.generate(spec) for spec in element_specs)

    def generate(self, spec):
        """根据数据类型规范生成随机数据"""
        if spec['type'] == 'int':
            return self.randomInt(spec['min'], spec['max'])
        elif spec['type'] == 'float':
            return self.randomFloat(spec['min'], spec['max'])
        elif spec['type'] == 'str':
            return self.randomStr(spec['length'])
        elif spec['type'] == 'list':
            return self.randomList(spec['element'], spec['size'])
        elif spec['type'] == 'tuple':
            return self.randomTuple(*[spec['element'] for _ in range(spec['size'])])
        # 可以根据需要继续添加其他类型的生成方法
        else:
            raise ValueError(f"Unsupported data type: {spec['type']}")

    def get(self, specs):
        """生成随机数据并存储到结果列表中"""
        self.result = [self.generate(spec) for spec in specs]
        return self.result

# 创建RandomData对象
rd = RandomData()

# 定义数据生成规范
specs = [
    {'type': 'int', 'min': 1, 'max': 100},
    {'type': 'float', 'min': 0.1, 'max': 0.5},
    {'type': 'str', 'length': 10},
    {'type': 'list', 'element': {'type': 'float', 'min': 0.1, 'max': 0.5}, 'size': 5},
    {'type': 'tuple', 'element': {'type': 'int', 'min': 1, 'max': 100}, 'size': 2}
]

# 获取并打印随机数据
random_data = rd.get(specs)
print(random_data)