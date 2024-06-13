import random
import string

class DataSampler:
    def __init__(self, kwargs):
        self.kwargs = kwargs

    def _sample_int(self, datarange):
        it = iter(datarange)
        return random.randint(next(it), next(it))

    def _sample_float(self, datarange):
        it = iter(datarange)
        return random.uniform(next(it), next(it))

    def _sample_string(self, datarange):
        return ''.join(random.SystemRandom().choice(datarange) for _ in range(7))

    def _sample_data(self, kwargs):
        datatype = kwargs["datatype"]
        if datatype == int:
            return self._sample_int(kwargs["datarange"])
        elif datatype == float:
            return self._sample_float(kwargs["datarange"])
        elif datatype == str:
            return self._sample_string(kwargs["datarange"])
        elif datatype in (list, tuple):
            elements = []
            for sub_key, sub_value in kwargs["subs"].items():
                elements.append(self._sample_data(sub_value))
            if datatype == list:
                return elements
            else:
                return tuple(elements)

    def sample(self):
        return self._sample_data(self.kwargs)

    def sample_int(self, datarange):
        return self._sample_int(datarange)

    def sample_float(self, datarange):
        return self._sample_float(datarange)

    def sample_string(self, datarange):
        return self._sample_string(datarange)

kwargs = {
    "num": 5,
    "datatype": tuple,
    "subs": {
        "sub1": {
            "datatype": list,
            "subs": {
                "sub1": {
                    "datatype": int,
                    "datarange": (0, 100)
                },
                "sub2": {
                    "datatype": str,
                    "datarange": string.ascii_letters
                },
            },
        },
        "sub2": {
            "datatype": tuple,
            "subs": {
                "sub1": {
                    "datatype": float,
                    "datarange": (0, 100)
                },
                "sub2": {
                    "datatype": int,
                    "datarange": (0, 100)
                },
            },
        },
        "sub3": {
            "datatype": str,
            "datarange": string.ascii_letters
        }
    }
}

sampler = DataSampler(kwargs)
print(sampler.sample())
print(sampler.sample_int((0, 10)))
print(sampler.sample_float((0, 10)))
print(sampler.sample_string(string.ascii_letters))
