import random
import string

class DataSampler:
    def dataSampling(self, kwargs):
        if kwargs['datatype'] == 'int':
            it = iter(kwargs['datarange'])
            return random.randint(next(it), next(it))
        elif kwargs['datatype'] == 'float':
            it = iter(kwargs['datarange'])
            return random.uniform(next(it), next(it))
        elif kwargs['datatype'] == 'str':
            if isinstance(kwargs['datarange'], str):
                return random.choice(kwargs['datarange'])
            elif isinstance(kwargs['datarange'], int):
                return ''.join(random.SystemRandom().choice(string.ascii_letters) for _ in range(kwargs['datarange']))
        elif kwargs['datatype'] in ('list', 'tuple'):
            elements = []
            for sub_key, sub_kwargs in kwargs['subs'].items():
                elements.append(self.dataSampling(sub_kwargs))
            if kwargs['datatype'] == 'list':
                return elements
            else:
                return tuple(elements)

    def apply(self, **kwargs):
        results = []
        for i in range(kwargs['num']):
            result = self.dataSampling(kwargs['struct'])
            results.append(result)
        return results

    def count_data(self, results):
        count = 0
        for result in results:
            if isinstance(result, (int, float)):
                count += 1
            elif isinstance(result, (list, tuple)):
                count += self.count_data(result)
        return count

    def sum_data(self, results):
        total_sum = 0
        for result in results:
            if isinstance(result, (int, float)):
                total_sum += result
            elif isinstance(result, (list, tuple)):
                total_sum += self.sum_data(result)
        return total_sum

    def mean_data(self, results):
        total_sum = self.sum_data(results)
        count = self.count_data(results)
        return total_sum / count if count else 0

    def operation(self, results, **kwargs):
        if kwargs['operation'] == 'both':
            Sum=self.sum_data(results)
            Mean=self.mean_data(results)
        elif kwargs['operation'] == 'sum':
            Sum=self.sum_data(results)
            Mean='do not need to calculate'
        elif kwargs['operation'] == 'mean':
            Sum='do not need to calculate'
            Mean=self.mean_data(results)
        elif kwargs['operation'] == 'none':
            Sum = 'do not need to calculate'
            Mean = 'do not need to calculate'
        print(f"Sum: {Sum}\nMean:{Mean}")


para = {
    "num": 5,
    "operation": "both",
    "struct": {
        "datatype": "tuple",
        "subs": {
            "sub1": {
                "datatype": "tuple",
                "subs": {
                    "sub1": {
                        "datatype": "int",
                        "datarange": (0, 100)
                    },
                    "sub2": {
                        "datatype": "str",
                        "datarange": "abcd"
                    }
                }
            },
            "sub2": {
                "datatype": "tuple",
                "subs": {
                    "sub1": {
                        "datatype": "float",
                        "datarange": (0, 5000)
                    },
                    "sub2": {
                        "datatype": "int",
                        "datarange": (1, 200)
                    }
                }
            },
            "sub3": {
                "datatype": "str",
                "datarange": "efgh"
            }
        }
    }
}

sampler = DataSampler()
results = sampler.apply(**para)
for index,value in enumerate(results):
    print(f"random structure {index} :{value}")

sampler.operation(results,**para)