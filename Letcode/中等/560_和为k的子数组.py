from collections import defaultdict


class Solution:
    def subarraySum(self, nums: [int], k: int) -> int:
        N, count, hash = len(nums), 0, defaultdict(int) # 设置初始值
        preSum = [0] * (N + 1) # preSum[n]代表前n项和
        hash[0] = 1
        for i in range(1, N + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]
            if preSum[i] - k in hash:
                count += hash[preSum[i] - k]
            hash[preSum[i]] = hash[preSum[i]] + 1  # 防止k为0的情况，所以放在后面
        return count


if __name__ == '__main__':
    nums = [1]
    k = 0
    solution = Solution()
    print(solution.subarraySum(nums, k))