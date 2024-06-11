import random
import string

def random_data_generator_decorator(cls):
    class DecoratedRandomDataGenerator(cls):
        def make_random_datas(self, the_struct):
            if isinstance(the_struct, dict):
                the_data_type = the_struct['data_type']
                the_subs = the_struct.get('subs', {})

                if the_data_type == tuple:
                    for sub in the_subs.values():
                        yield from self.make_random_datas(sub)
                elif the_data_type == list:
                    for sub in the_subs.values():
                        yield from self.make_random_datas(sub)

                for key, the_sub_struct in the_subs.items():
                    yield from self.make_random_datas(the_sub_struct)
            elif the_data_type in [int, float, str, bool]:
                if the_data_type == int:
                    if isinstance(the_struct['data_range'], list) and the_struct['data_range']:
                        yield random.choice(the_struct['data_range'])
                    elif isinstance(the_struct['data_range'], tuple) and len(the_struct['data_range']) == 2:
                        yield random.randint(the_struct['data_range'][0], the_struct['data_range'][1])
                elif the_data_type == float:
                    if isinstance(the_struct['data_range'], tuple) and len(the_struct['data_range']) == 2:
                        yield random.uniform(the_struct['data_range'][0], the_struct['data_range'][1])
                elif the_data_type == str:
                    if isinstance(the_struct['data_range'], (str, list)) and 'len' in the_struct:
                        yield ''.join(random.choice(the_struct['data_range']) for _ in range(the_struct['len']))
                elif the_data_type == bool:
                    yield random.choice([True, False])

    return DecoratedRandomDataGenerator

@random_data_generator_decorator
class RandomDataGeneratorBeginnerStyleWithYield:
    pass

# 使用示例
random_gen_yield = RandomDataGeneratorBeginnerStyleWithYield()
for random_num in random_gen_yield.make_random_datas(example):
    print(random_num)