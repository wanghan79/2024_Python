import random
import string

def random_data_generator_decorator(cls):
    class DecoratedRandomDataGenerator(cls):
        def make_random_data(self, struct):
            res = []

            if isinstance(struct, dict):
                data_type = struct['data_type']
                subs = struct.get('subs', {})

                if data_type == tuple:
                    sub_res = [self.make_random_data(sub) for sub in subs.values()]
                    res.append(tuple(sub_res))
                elif data_type == list:
                    sub_res = [self.make_random_data(sub) for sub in subs.values()]
                    res.append(list(sub_res))

                for key, sub_struct in subs.items():
                    res.extend(self.make_random_data(sub_struct))
            elif data_type in [int, float, str, bool]:
                if data_type == int:
                    if isinstance(struct['data_range'], list) and struct['data_range']:
                        res.append(random.choice(struct['data_range']))
                    elif isinstance(struct['data_range'], tuple) and len(struct['data_range']) == 2:
                        res.append(random.randint(*struct['data_range']))
                elif data_type == float:
                    if isinstance(struct['data_range'], tuple) and len(struct['data_range']) == 2:
                        res.append(random.uniform(*struct['data_range']))
                elif data_type == str:
                    if isinstance(struct['data_range'], (str, list)) and 'len' in struct:
                        res.append(''.join(random.choice(struct['data_range']) for _ in range(struct['len'])))
                elif data_type == bool:
                    res.append(random.choice([True, False]))
            return res

    return DecoratedRandomDataGenerator

@random_data_generator_decorator
class RandomDataGeneratorBeginner:
    pass

# 使用示例
random_gen = RandomDataGeneratorBeginner()
print(random_gen.make_random_data(example))