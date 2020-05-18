import collections
from collections import Counter


class Solution:
    count, keylist = 0, []

    def Add(self, value):
        self.count += 1
        self.keylist.append(value)

    def Remove(self, value):
        self.count -= 1
        self.keylist.remove(value)

    def slidingWindowUniqueElementsSum2(self, nums, k):
        res = 0
        if len(nums) <= k:
            d = Counter(nums)
            for key in d:
                if d[key] == 1:
                    res += 1
        else:
            dic = Counter(nums[:k])
            for key in dic:
                if dic[key] == 1:
                    self.Add(key)
            start, end = 0, k - 1
            res += self.count
            while end + 1 < len(nums):
                v, u = nums[start], nums[end + 1]
                dic[v] -= 1
                if dic[v] == 0 and v in self.keylist:
                    del dic[v]
                    self.Remove(v)
                if u not in dic and u not in self.keylist:
                    dic[u] = 0
                    self.Add(u)
                dic[u] += 1
                if dic[u] == 2 and u in self.keylist:
                    self.Remove(u)
                if v in dic and dic[v] == 1 and v not in self.keylist:
                    self.Add(v)
                res += self.count
                start += 1
                end += 1
        return res

    def slidingWindowUniqueElementsSum(self, nums, k):
        size = len(nums)
        sum = 0
        queue = collections.deque()
        for i in range(k):
            queue.append(nums[i])
        sum += self.weiyi(queue)
        print(self.weiyi(queue))
        for i in range(k, size):
            queue.popleft()
            queue.append(nums[i])
            sum += self.weiyi(queue)
            print(self.weiyi(queue))
        return sum

    def weiyi(self, queue):
        sum = 0
        counts = collections.Counter(queue)
        for key, val in counts.items():
            if counts[key] == 1:
               sum += key
        return sum if sum < len(queue) else len(queue)

# 主函数
if __name__ == "__main__":
    nums = [1, 2, 1, 3, 3]
    k = 3
    # 创建对象
    solution = Solution()
    print("输入的数组是nums=：", nums, "滑动窗口的大小k=", k)
    print("每一个窗口内唯一元素的个数和是:", solution.slidingWindowUniqueElementsSum(nums, k))
