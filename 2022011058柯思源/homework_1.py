import random
import string

#生成随机数
def generate_random_data(**kwargs):
    datatype = kwargs.get("datatype")
    if datatype == int:
        drange = kwargs.get("drange")
        return random.randint(drange[0],drange[1])
    elif datatype == float:
        drange = kwargs.get("drange")
        return random.uniform(drange[0],drange[1])
    elif datatype == str:
        len=kwargs.get("len")
        chars = kwargs.get("drange", string.ascii_lowercase)
        return ''.join(random.choices(chars,k=len))
    elif datatype == list or datatype == tuple or datatype == set:
        subs = kwargs.get("subs")
        if subs is None:
            return [] if datatype == list else tuple() if datatype == tuple else set()
        result = []
        for sub_key, sub_kwargs in subs.items():
            result.append(generate_random_data(**sub_kwargs))
        return result if datatype == list else tuple(result) if datatype == tuple else set(result)
#生成给定数量的随机数
def generate_num_sampling(**kwargs):
    results=list()
    n=kwargs.get("num")
    for _ in range(int(n)):
        result=generate_random_data(**kwargs['struct'])
        results.append(result)
    return  results
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
# 调用函数并打印结果
    random_data = generate_num_sampling(**para)
    print(random_data)
