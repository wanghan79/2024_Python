import random
import string

class RandomDataGenerator:
    def __init__(self):
        pass

    def generate_random_data(self, **kwargs):
        datatype = kwargs.get("datatype")
        if datatype == int:
            drange = kwargs.get("drange")
            return random.randint(drange[0], drange[1])
        elif datatype == float:
            drange = kwargs.get("drange")
            return random.uniform(drange[0], drange[1])
        elif datatype == str:
            len = kwargs.get("len")
            chars = kwargs.get("drange", string.ascii_lowercase)
            return ''.join(random.choices(chars, k=len))
        elif datatype == list or datatype == tuple or datatype == set:
            subs = kwargs.get("subs")
            if subs is None:
                return [] if datatype == list else tuple() if datatype == tuple else set()
            result = []
            for sub_key, sub_kwargs in subs.items():
                result.append(self.generate_random_data(**sub_kwargs))
            return result if datatype == list else tuple(result) if datatype == tuple else set(result)
    def generate_num_sampling(self,**kwargs):
        results = list()
        n = kwargs.get("num")
        for _ in range(int(n)):
            result = self.generate_random_data(**kwargs['struct'])
            results.append(result)
        return results


    def process_data(self, data, args):
        def traverse(item, total, count):
            if args[1] == 'int':
                if isinstance(item, int):
                    if args[0] == 'sum':
                        total += item
                    elif args[0] == 'mean':
                        total += item
                        count += 1
                elif isinstance(item, (tuple, list, set)):
                    for sub_item in item:
                        total, count = traverse(sub_item, total, count)
                return total, count
            elif args[1] == 'float':
                if isinstance(item, float):
                    if args[0] == 'sum':
                        total += item
                    elif args[0] == 'mean':
                        total += item
                        count += 1
                elif isinstance(item, (tuple, list, set)):
                    for sub_item in item:
                        total, count = traverse(sub_item, total, count)
                return total, count


        total = 0
        count = 0
        for item in data:
            total, count = traverse(item, total, count)
        if args[0] == 'sum':
            return total
        elif args[0] == 'mean':
            if count == 0:
                return 0
            return total / count
para = {
    "num": 5,
    "struct": {
        "datatype": tuple,
        "subs": {
            "sub1": {
                "datatype": list,
                "subs": {
                    "sub1": {
                        "datatype": int,
                        "drange": (0, 50),
                    },
                    "sub2": {
                        "datatype": str,
                        "drange": string.ascii_lowercase,
                        "len":8
                    },
                },
            },
            "sub2": {
                "datatype": float,
                "drange": (0, 100),
            },
        },
    },
}
if __name__ == '__main__':
    generator=RandomDataGenerator()
    results=generator.generate_num_sampling(**para)
    print(results)
    sum_result=generator.process_data(results,('sum','int'))
    average_result=generator.process_data(results,('mean','float'))
    print("sum=",sum_result)
    print("average=",average_result)