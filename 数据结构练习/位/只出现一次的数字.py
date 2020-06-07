class Solution():
    def singleNumber(self, arr):
        res = 0
        for i in range(64):
            number = 0  # 每一位上1的个数
            for j in range(len(arr)):
                if (arr[j] & (1 << i)) != 0:
                    number += 1
            res |= number % 3 << i
        return res

if __name__ == '__main__':
    solution = Solution()
    arr = [1,1,1,2]
    print(solution.singleNumber(arr))