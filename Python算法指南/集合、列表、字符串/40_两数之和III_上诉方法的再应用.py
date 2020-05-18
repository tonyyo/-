class TwoSum:
    data = []
    def add(self, number):
        self.data.append(number)
        #参数value是一个整数
        #返回值是找到存在的任意一对数字，使其和等于value值
    def find(self, value):
        self.data.sort()  # 这里进行了排序，表明要用二分法，而不是hash映射法。
        left, right = 0, len(self.data) - 1
        while left < right:
            if self.data[left] + self.data[right] == value:
                return True
            if self.data[left] + self.data[right] < value:
                left += 1
            else:
                right -= 1
        return False
# 主函数
if __name__ == "__main__":
    list = []
    # 创建对象
    solution = TwoSum()
    solution.add(1)
    solution.add(3)
    solution.add(5)
    list.append(solution.find(4))
    list.append(solution.find(7))
    print("初始化的输入顺序是add(1),add(2),add(3),find(4),find(7)")
    print("输出的结果是：", list)