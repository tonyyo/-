class Solution:
    def rotate(self, nums: [int], k: int) -> None:
        k = k % len(nums)  # k可大于数组长度
        self.reverseList(nums, 0, len(nums) - 1)
        self.reverseList(nums, 0, k - 1)
        self.reverseList(nums, k, len(nums) - 1)

    def reverseList(self, List, start, end):
        while start < end:
            List[start], List[end] = List[end], List[start]
            start += 1
            end -= 1
if __name__ == '__main__':
    solution = Solution()
    solution.rotate([-1], 2)