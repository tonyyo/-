class Solution:
    def nextGreaterElement(self, nums1: [int], nums2: [int]) -> [int]:
        M, N = len(nums1), len(nums2)
        result = [0] * M
        for i in range(M):
            flag = False
            index = nums2.index(nums1[i]) # 不是对应位置，而是对应元素
            for j in range(index + 1, N):
                if nums2[j] > nums1[i]:
                    result[i] = nums2[j]
                    flag = True
                    break
            if not flag:
                result[i] = -1
        return result
if __name__ == '__main__':
    solution = Solution()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    print(solution.nextGreaterElement(nums1, nums2))