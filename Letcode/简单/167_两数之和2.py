class Solution:
    def twoSum(self, numbers: [int], target: int) -> [int]:
        N = len(numbers)
        if N < 2:
            return []
        left, right = 0, N - 1
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        return []
if __name__ == '__main__':
    solution = Solution()
    numbers = [2,7,11,15]
    target = 9
    print(solution.twoSum(numbers, target))
