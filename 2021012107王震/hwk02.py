import random
import string
import statistics


class DataProcessor:
    def __init__(self):
        pass

    def _flatten_and_filter(self, data):
        flattened_data = []
        for item in data:
            if isinstance(item, (int, float)):
                flattened_data.append(item)
            elif isinstance(item, (list, tuple)):
                flattened_data.extend(self._flatten_and_filter(item))
        return flattened_data

    def dataSampling(self, **kwargs):
        result = []
        for key, specs in kwargs.items():
            if key == 'int':
                result.append(random.randint(*specs['datarange']))
            elif key == 'float':
                result.append(random.uniform(*specs['datarange']))
            elif key == 'str':
                chars = specs['datarange']
                length = specs.get('len', 0)
                result.append(''.join(random.choice(chars) for _ in range(length)))
            elif key == 'tuple':
                tuple_elements = [self.dataSampling(**{k: v}) for k, v in specs.items() if isinstance(v, dict)]
                result.append(tuple(tuple_elements))
            elif key == 'list':
                list_elements = [self.dataSampling(**specs) for _ in range(specs.get('count', 1))]
                result.append(list_elements)
        return result

    def dataScreening(self, num, **kwargs):
        screened_data = []
        for _ in range(num):
            sampled_data = self.dataSampling(**kwargs)
            flattened_data = self._flatten_and_filter(sampled_data)
            screened_data.append(flattened_data)
            print("生成数据为:", sampled_data)
        return screened_data

    def dataFiguring(self, data_sets):
        flattened_data = [item for data_set in data_sets for item in data_set]
        print("可参与运算的数据为:", flattened_data)

        while True:
            print("\n请选择要处理的数据类型: 整数类型（int）, 浮点数类型（float）, 或两者一起处理（both)。")
            data_type = input("请输入 'int', 'float', 'both', 或输入 'e' 直接退出: ").strip().lower()
            if data_type == 'e':
                print("已成功退出！")
                break

            int_data = [item for item in flattened_data if isinstance(item, int)]
            float_data = [item for item in flattened_data if isinstance(item, float)]

            if data_type == 'int':
                selected_data = int_data
            elif data_type == 'float':
                selected_data = float_data
            elif data_type == 'both':
                selected_data = int_data + float_data
            else:
                print("无效, 请重新选择。")
                continue

            print("\n请选择要进行的运算: 求和（sum), 求均值（ave）, 求方差（var）。")
            operation = input("请输入 'sum', 'ave', 'var', 或输入 'e' 直接退出: ").strip().lower()
            if operation == 'e':
                print("已成功退出！")
                break

            if operation not in ['sum', 'ave', 'var']:
                print("无效, 请重新选择。")
                continue

            if operation == 'sum':
                result = sum(selected_data)
            elif operation == 'ave':
                result = statistics.mean(selected_data) if selected_data else 0
            elif operation == 'var':
                result = statistics.variance(selected_data) if len(selected_data) > 1 else 0

            print(f"所选数据的 {operation} 为: {result}")


# 使用示例
processor = DataProcessor()
struct = {
    'int': {'datarange': [1, 10]},
    'float': {'datarange': [1.0, 10.0]},
    'tuple': {
        'int': {'datarange': [1, 50]},
        'str': {'datarange': string.ascii_uppercase, 'len': 0}
    },
    'list': {
        'int': {'datarange': [1, 30]},
        'str': {'datarange': string.ascii_lowercase, 'len': 8},
        'float': {'datarange': [1.0, 10.0]}
    }
}

data_sets = processor.dataScreening(2, **struct)
processor.dataFiguring(data_sets)
