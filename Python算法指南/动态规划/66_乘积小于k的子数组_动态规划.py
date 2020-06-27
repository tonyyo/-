import collections
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        queue = collections.deque()
        product = 1
        ans = 0
        for i in range(len(nums)):
            queue.append(nums[i])
            product *= nums[i]
            while product >= k: # 添加一个元素后，始终保持乘积小于k
                remove = queue.popleft()
                product /= remove
            if queue:
                ans += len(queue) # 跟新添加的元素有关的情况始终是queue的长度
        return ans

if __name__ == '__main__':
    temp = Solution()
    List1 = [8, 4, 3, 6, 10]
    num = 100
    print("输入：" + str(List1) + "  " + str(num))
    print(("输出：" + str(temp.numSubarrayProductLessThanK(List1, num))))
