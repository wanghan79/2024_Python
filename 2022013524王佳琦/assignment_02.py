class NumberCalculator:
    def __init__(self):
        self.numbers = []

    def get_numbers(self):
        while True:
            try:
                num = input("请输入一个整数或者浮点数（按q退出）：")
                if num.lower() == 'q':
                    break
                self.numbers.append(float(num))
            except ValueError:
                print("输入无效，请重新输入。")

    def calculate_average(self):
        if not self.numbers:
            print("没有输入数字。")
        else:
            total = sum(self.numbers)
            average = total / len(self.numbers)
            print("平均数为:", average)

    def calculate_sum(self):
        if not self.numbers:
            print("没有输入数字。")
        else:
            total = sum(self.numbers)
            print("总和为:", total)

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