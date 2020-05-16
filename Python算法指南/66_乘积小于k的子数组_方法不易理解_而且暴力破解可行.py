class Solution:
    def numSubarrayProductLessThanK2(self, nums, mx):
        ans = []
        size = len(nums)
        count = 0
        for i in range(1, size + 1): # 不同长度的子数组
            for j in range(size - i + 1):  # 不同的起始位置
                chengji = 1
                for k in range(j, j + i):
                    chengji = chengji * nums[k]
                if chengji < mx:
                    count += 1
                    temp = []
                    for k in range(j, j + i):
                        temp.append(nums[k])
                    ans.append(temp)
        print(ans)
        return count

if __name__ == '__main__':
    temp = Solution()
    List1 = [8, 4, 3, 6, 10]
    num = 100
    print("输入：" + str(List1) + "  " + str(num))
    print(("输出：" + str(temp.numSubarrayProductLessThanK2(List1, num))))
