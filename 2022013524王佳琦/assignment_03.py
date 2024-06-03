"""
第三次作业:修饰器的使用
求和、求平均数
"""

import functools
import random

def input_validation(func):
    @functools.wraps(func)
    def wrapper(self):
        self.numbers = [random.uniform(-100, 100) if random.random() > 0.5 else random.randint(-100, 100) for _ in range(random.randint(5, 20))]
        return func(self)
    return wrapper

def output_decorator(func):
    @functools.wraps(func)
    def wrapper(self):
        result = func(self)
        print(f"基于以下数字进行计算: {self.numbers}")
        print("结果为:", result)
    return wrapper

class NumberCalculator:
    def __init__(self):
        self.numbers = []

    @input_validation
    def generate_numbers(self):  # 修改方法名称为 generate_numbers
        pass

    @output_decorator
    def calculate_average(self):
        if not self.numbers:
            return "没有输入数字。"
        else:
            total = sum(self.numbers)
            average = total / len(self.numbers)
            return f"平均数为: {average:.2f}"

    @output_decorator
    def calculate_sum(self):
        if not self.numbers:
            return "没有输入数字。"
        else:
            total = sum(self.numbers)
            return f"总和为: {total:.2f}"

    def perform_calculation(self):
        self.generate_numbers()
        self.calculate_sum()
        self.calculate_average()

calculator = NumberCalculator()
calculator.perform_calculation()