class Solution:
    def parseTernary(self, expression):
        objects = []
        i = len(expression) - 1
        while i >= 1:
            if expression[i] == '?':
                left, right = objects.pop(-1), objects.pop(-1)
                objects.append(left if expression[i - 1] == 'T' else right)
                i -= 1   # 多走一位
            elif expression[i] != ':':
                objects.append(expression[i])
            i -= 1
        print(objects)
        return objects[0]

#主函数
if __name__ == "__main__":
    expression = "T?T?F:5:3"
    #创建对象
    solution = Solution()
    print("输入的表达式是：", expression)
    print("表达式的结果是：", solution.parseTernary(expression))