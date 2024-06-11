import random
import string

class RandomDataGenerator:
    def __init__(self):
        pass

    def generate_random_data(self, structure):
        """
        该函数根据给定的数据结构生成随机数据

        参数：
        structure (dict)：包含数据类型和相关范围等信息的数据结构
        """
        result = []

        if isinstance(structure, dict):
            data_type = structure['data_type']
            subs = structure.get('subs', {})

            if data_type == tuple:
                sub_results = [self.generate_random_data(sub) for sub in subs.values()]
                result.append(tuple(sub_results))
            elif data_type == list:
                sub_results = [self.generate_random_data(sub) for sub in subs.values()]
                result.append(list(sub_results))

            for key, sub_structure in subs.items():
                result.extend(self.generate_random_data(sub_structure))
        elif data_type in [int, float, str, bool]:
            if data_type == int:
                if isinstance(structure['data_range'], list) and structure['data_range']:
                    result.append(random.choice(structure['data_range']))
                elif isinstance(structure['data_range'], tuple) and len(structure['data_range']) == 2:
                    result.append(random.randint(*structure['data_range']))
            elif data_type == float:
                if isinstance(structure['data_range'], tuple) and len(structure['data_range']) == 2:
                    result.append(random.uniform(*structure['data_range']))
            elif data_type == str:
                if isinstance(structure['data_range'], (str, list)) and 'len' in structure:
                    result.append(''.join(random.choice(structure['data_range']) for _ in range(structure['len'])))
            elif data_type == bool:
                result.append(random.choice([True, False]))
        return result