import random

def class_decorator(cls):
    class DecoratedClass(cls):
        def __init__(self, datatypes):
            super().__init__(datatypes)

        def generate_random_lists(self, num_lists):
            print("Generating random lists using the decorated class...")
            super().generate_random_lists(num_lists)

        def print_random_lists(self):
            print("Printing random lists using the decorated class...")
            super().print_random_lists()

        def calculate_sum(self):
            print("Calculating sum using the decorated class...")
            super().calculate_sum()

        def calculate_average(self):
            print("Calculating average using the decorated class...")
            super().calculate_average()

    return DecoratedClass

@class_decorator
class RandomListGenerator:
    def __init__(self, datatypes):
        self.datatypes = datatypes
        self.random_lists = []

    def generate_random_lists(self, num_lists):
        for _ in range(num_lists):
            random_list = []
            for _ in range(10):
                datatype = random.choice(self.datatypes)
                if datatype == 'str':
                    random_list.append(random.choice(['a', 'b', 'c']))
                elif datatype == 'int':
                    random_list.append(random.randint(1, 10))
                elif datatype == 'float':
                    random_list.append(random.uniform(1.0, 10.0))
                elif datatype == 'bool':
                    random_list.append(random.choice([True, False]))
                elif datatype == 'list':
                    random_list.append(random.sample(range(1, 10), 3))
            self.random_lists.append(random_list)

    def print_random_lists(self):
        for idx, random_list in enumerate(self.random_lists):
            print(f"列表{idx+1}: {random_list}")

    def calculate_sum(self):
        int_sum = 0
        float_sum = 0
        for random_list in self.random_lists:
            for var in random_list:
                if isinstance(var, int):
                    int_sum += var
                elif isinstance(var, float):
                    float_sum += var
        print(f"整数型变量总和: {int_sum}")
        print(f"浮点型变量总和: {float_sum}")

    def calculate_average(self):
        int_sum = 0
        int_count = 0
        float_sum = 0
        float_count = 0
        for random_list in self.random_lists:
            for var in random_list:
                if isinstance(var, int):
                    int_sum += var
                    int_count += 1
                elif isinstance(var, float):
                    float_sum += var
                    float_count += 1

        if int_count > 0:
            int_average = int_sum / int_count
            print(f"整数型变量平均值: {int_average}")
        if float_count > 0:
            float_average = float_sum / float_count
            print(f"浮点型变量平均值: {float_average}")

def main():
    # 提示用户输入要生成的列表数
    num_lists = int(input("请输入要生成的列表数："))

    # 生成包含不同数据类型的列表
    datatypes = ['str', 'int', 'float', 'bool', 'list']

    # 使用RandomListGenerator类创建对象
    generator = RandomListGenerator(datatypes)

    # 使用generator对象生成随机列表
    generator.generate_random_lists(num_lists)

    # 使用generator对象打印随机列表
    generator.print_random_lists()

    # 提示用户选择求和或求均值
    option = input("请选择要进行的操作（sum求和/average求均值）：")

    # 使用generator对象根据用户选择计算列表中int型和float型变量的和或平均值，并输出结果
    if option == "sum":
        generator.calculate_sum()
    elif option == "average":
        generator.calculate_average()
    else:
        print("无效的选项，请重新运行程序并选择正确的操作。")

if __name__ == "__main__":
    main()
