"""
学习修饰器的使用
"""
import functools

def input_validation(func):
    @functools.wraps(func)
    def wrapper(self):
        while True:
            try:
                num = input("请输入一个整数或者浮点数（按q退出）：")
                if num.lower() == 'q':
                    break
                self.numbers.append(float(num))
            except ValueError:
                print("输入无效，请重新输入。")
        return func(self)
    return wrapper

def output_decorator(func):
    @functools.wraps(func)
    def wrapper(self):
        result = func(self)
        print("结果为:", result)
    return wrapper

class NumberCalculator:
    def __init__(self):
        self.numbers = []

    @input_validation
    def get_numbers(self):
        pass

    @output_decorator
    def calculate_average(self):
        if not self.numbers:
            return "没有输入数字。"
        else:
            total = sum(self.numbers)
            average = total / len(self.numbers)
            return average

    @output_decorator
    def calculate_sum(self):
        if not self.numbers:
            return "没有输入数字。"
        else:
            total = sum(self.numbers)
            return total

    def perform_calculation(self):
        choice = input("请选择要执行的操作（1-求和，2-求平均数，3-求和和平均数）：")
        if choice == '1':
            self.calculate_sum()
        elif choice == '2':
            self.calculate_average()
        elif choice == '3':
            self.calculate_sum()
            self.calculate_average()
        else:
            print("无效的选择。请重新选择。")

calculator = NumberCalculator()
calculator.get_numbers()
calculator.perform_calculation()