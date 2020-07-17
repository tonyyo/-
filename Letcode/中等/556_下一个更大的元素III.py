import math


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        strN = str(n)
        nums = [int(x) for x in strN]
        N = len(nums)
        for i in range(N - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                nums[i:] = sorted(nums[i:])
                for j in range(i, N):
                    if nums[i - 1] < nums[j]:
                        nums[i - 1], nums[j] = nums[j], nums[i - 1]
                        result = int("".join(str(x) for x in nums))
                        if result >= math.pow(2, 32) // 2: # 1999999999 ---> 9199999999
                            return -1
                        else:
                            return result
        return -1
if __name__ == '__main__':
    solution = Solution()
    print(solution.nextGreaterElement(2147483647))
