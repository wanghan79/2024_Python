import random
import string


class DataProcessor:
    def __init__(self):
        self.result = []

    def generate_data(self, data_spec, **kwargs):
        if 'dataType' in data_spec:
            data_type = data_spec['dataType']
            if data_type == int:
                daterange = kwargs.get('daterange', (0, 100))
                self.result.append(random.randint(daterange[0], daterange[1]))
            elif data_type == float:
                daterange = kwargs.get('daterange', (0.0, 1.0))
                self.result.append(random.uniform(daterange[0], daterange[1]))
            elif data_type == str:
                datarange = kwargs.get('datarange', string.ascii_letters)
                length = kwargs.get('len', 5)
                self.result.append(''.join(random.choices(datarange, k=length)))
            elif data_type == bool:
                self.result.append(random.choice([True, False]))
            elif data_type == list:
                size = kwargs.get('size', 5)
                sub_spec = data_spec.get('subs', {}).get('sub', {})  # 假设 'subs' 下有一个 'sub' 键
                self.result.append([self.generate_data(sub_spec, **sub_spec.get('kwargs', {})) for _ in range(size)])
            elif data_type == tuple:
                subs = data_spec.get('subs', {})
                sub_data = [self.generate_data(sub_spec, **sub_spec.get('kwargs', {})) for sub_name, sub_spec in
                            subs.items()]
                self.result.append(tuple(sub_data))

    def data_sampling(self, data_structure, num_samples=1):
        for _ in range(num_samples):
            self.result.clear()
            self._generate_nested_data(data_structure)
            print(self.result)

    def _generate_nested_data(self, data_structure):
        if isinstance(data_structure, dict) and 'dataType' in data_structure:
            self.generate_data(data_structure, **data_structure.get('kwargs', {}))
        elif isinstance(data_structure, (list, tuple)):
            for item in data_structure:
                self._generate_nested_data(item)

            # 示例用法


data_structure = {
    "dataType": tuple,
    "subs": {
        "sub1": {
            "dataType": int,
            "kwargs": {"daterange": (1, 10)}
        },
        "sub2": {
            "dataType": str,
            "kwargs": {"datarange": string.ascii_lowercase, "len": 3}
        },
        "sub3": {
            "dataType": list,
            "subs": {
                "sub": {
                    "dataType": float,
                    "kwargs": {"daterange": (0.5, 1.5)}
                }
            },
            "kwargs": {"size": 2}
        }
    }
}

processor = DataProcessor()
processor.data_sampling(data_structure, num_samples=3)