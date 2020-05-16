class Solution:
    def reOrderArray(self, array):
        for i in range(1,len(array)):
            if array[i] % 2 == 1:  # 如果第i个树为奇数，开始往前插入
                for j in range(i - 1, -1, -1): # 从第i-1个数开始判断是否为偶数
                    if array[j] % 2 == 0:
                        array[j], array[j + 1] = array[j + 1], array[j]

if __name__ == '__main__':
    solution = Solution()
    array = [1,2,3,4,5,6,7]
    print(array)
    solution.reOrderArray(array)
    print(array)