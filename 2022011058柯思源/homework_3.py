import random
import string

def Sat(operation, datatype):
    def decorator(func):
        def wrapper(*func_args, **func_kwargs):
            results = func(*func_args, **func_kwargs)
            def traverse(item, total, count):
                if datatype == 'int':
                    if isinstance(item, int):
                        if operation == 'sum':
                            total += item
                        elif operation == 'mean':
                            total += item
                            count += 1
                    elif isinstance(item, (tuple, list, set)):
                        for sub_item in item:
                            total, count = traverse(sub_item, total, count)
                    return total, count
                elif datatype == 'float':
                    if isinstance(item, float):
                        if operation == 'sum':
                            total += item
                        elif operation == 'mean':
                            total += item
                            count += 1
                    elif isinstance(item, (tuple, list, set)):
                        for sub_item in item:
                            total, count = traverse(sub_item, total, count)
                    return total, count

            total = 0
            count = 0
            for item in results:
                total, count = traverse(item, total, count)
            print(results)
            if operation == 'sum':
                print("sum=")
                return total
            elif operation == 'mean':
                print("average=")
                return total / max(count, 1)
            elif operation == 'none':
                pass
            return None
        return wrapper
    return decorator

@Sat('sum', 'int')
def generate_num_sampling(**kwargs):
    results = []
    n = kwargs.get("num")
    for _ in range(int(n)):
        result = generate_random_data(**kwargs['struct'])
        results.append(result)
    return results

def generate_random_data(**kwargs):
    datatype = kwargs.get("datatype")
    if datatype == int:
        drange = kwargs.get("drange")
        return random.randint(drange[0], drange[1])
    elif datatype == float:
        drange = kwargs.get("drange")
        return random.uniform(drange[0], drange[1])
    elif datatype == str:
        length = kwargs.get("len")
        chars = kwargs.get("drange", string.ascii_lowercase)
        return ''.join(random.choices(chars, k=length))
    elif datatype in (list, tuple, set):
        subs = kwargs.get("subs")
        result = [generate_random_data(**sub_kwargs) for sub_key, sub_kwargs in subs.items()]
        if datatype == list:
            return result
        elif datatype == tuple:
            return tuple(result)
        elif datatype == set:
            return set(result)

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
                        "len": 8
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
    print(generate_num_sampling(**para))