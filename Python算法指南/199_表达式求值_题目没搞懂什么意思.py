class Solution:
    def evaluateExpression(self, expression):
        if expression is None or len(expression) == 0:
            return 0
        integers = []
        symbols = []
        for c in expression:
            if c.isdigit():
                integers.append(int(c))
            elif c == "(":
                symbols.append(c)
            elif c == ")":
                while symbols[-1] != "(":
                    self.calculate(integers, symbols)
                symbols.pop()
            else:
                if symbols and symbols[-1] != "(" and self.get_level(c) >= self.get_level(symbols[-1]):
                    self.calculate(integers, symbols)
                symbols.append(c)
        while symbols:
            print(integers, symbols)
            self.calculate(integers, symbols)
        if len(integers) == 0:
            return 0
        return integers[0]
    def get_level(self, c):
        if c == "+" or c == "-":
            return 2
        if c == "*" or c == "/":
            return 1
        return sys.maxsize
    def calculate(self, integers, symbols):
        if integers is None or len(integers) < 2:
            return False
        after = integers.pop()
        before = integers.pop()
        symbol = symbols.pop()
        # print(after, before, symbol)
        if symbol == "-":
            integers.append(before - after)
        elif symbol == "+":
            integers.append(before + after)
        elif symbol == "*":
            integers.append(before * after)
        elif symbol == "/":
            integers.append(before // after)
        return True
#主函数
if __name__=="__main__":
    str="(2*6-(23+7)/(1+2))"
    num=["2", "*", "6", "-", "(", "23", "+", "7", ")", "/","(", "1", "+", "2", ")"]
    #创建对象
    solution=Solution()
    print("输入的表达式为：", str)
    print("其表达式对应的数组是：", num)
    print("表达式的值是：",solution.evaluateExpression(num))