import random

def class_decorator(cls):
    class DecoratedClass(cls):
        def __init__(self, datatypes):
            super().__init__(datatypes)

        def generate_random_pages(self, num_pages, page_size):
            print(f"Generating random pages using the decorated class with {num_pages} pages and {page_size} elements per page...")
            pages = []
            for _ in range(num_pages):
                page = [self.generate_random_list() for _ in range(page_size)]
                pages.append(page)
            return pages

        def print_random_pages(self, pages):
            print("Printing random pages using the decorated class...")
            for idx, page in enumerate(pages):
                print(f"Page {idx+1}:")
                for random_list in page:
                    print(random_list)

        def calculate_sum_and_average(self, pages):
            print("Calculating sum and average using the decorated class...")
            int_sum, int_count, float_sum, float_count = 0, 0, 0, 0
            for page in pages:
                for random_list in page:
                    for var in random_list:
                        if isinstance(var, int):
                            int_sum += var
                            int_count += 1
                        elif isinstance(var, float):
                            float_sum += var
                            float_count += 1

            if int_count > 0:
                int_average = int_sum / int_count
                print(f"整数型变量总和: {int_sum}")
                print(f"整数型变量平均值: {int_average}")
            if float_count > 0:
                float_average = float_sum / float_count
                print(f"浮点型变量总和: {float_sum}")
                print(f"浮点型变量平均值: {float_average}")

    return DecoratedClass

def page_generator(generator, num_pages, page_size):
    for page in generator.generate_random_pages(num_pages, page_size):
        yield page

@class_decorator
class RandomListGenerator:
    def __init__(self, datatypes):
        self.datatypes = datatypes

    def generate_random_list(self):
        return [self.generate_random_variable() for _ in range(10)]

    def generate_random_variable(self):
        datatype = random.choice(self.datatypes)
        if datatype == 'str':
            return random.choice(['a', 'b', 'c'])
        elif datatype == 'int':
            return random.randint(1, 10)
        elif datatype == 'float':
            return round(random.uniform(1.0, 10.0), 2)
        elif datatype == 'bool':
            return random.choice([True, False])
        elif datatype == 'list':
            return random.sample(range(1, 10), 3)

# 提示用户输入要生成的页数和每页的元素数
num_pages = int(input("请输入要生成的页数："))
page_size = int(input("请输入每页的元素数："))

# 生成包含不同数据类型的列表的页生成器
datatypes = ['str', 'int', 'float', 'bool', 'list']
generator = RandomListGenerator(datatypes)
pages = page_generator(generator, num_pages, page_size)

# 使用generator对象打印随机页
generator.print_random_pages(pages)

# 使用generator对象计算列表中int型和float型变量的和和平均值，并输出结果
generator.calculate_sum_and_average(pages)
