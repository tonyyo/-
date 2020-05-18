import collections
class Solution:
    def slidingWindowUniqueElementsSum(self, nums, k):
        size = len(nums)
        sum = 0
        queue = collections.deque()
        for i in range(k): # k不到
            queue.append(nums[i])
        sum += self.weiyi(queue)  # 第一个窗口额外计算
        for i in range(k, size): # 正好取到k
            queue.popleft()
            queue.append(nums[i])
            sum += self.weiyi(queue)
        return sum

    def weiyi(self, queue):
        sum = 0
        counts = collections.Counter(queue) #没想到我居然会想到用Counter进行计数，记得返回的是字典
        for key, val in counts.items():
            if counts[key] == 1:
               sum += val
        return sum

# 主函数
if __name__ == "__main__":
    nums = [1, 2, 1, 3, 3]
    k = 3
    # 创建对象
    solution = Solution()
    print("输入的数组是nums=：", nums, "滑动窗口的大小k=", k)
    print("每一个窗口内唯一元素的个数和是:", solution.slidingWindowUniqueElementsSum(nums, k))
