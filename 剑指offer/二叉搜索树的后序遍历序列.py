class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        length = len(sequence)
        if length == 0:
            return False
        if length == 1:
            return True
        root = sequence[-1]
        left = 0
        while sequence[left] < root:
                left += 1
        for j in range(left, length-1):
            if sequence[j] < root:
                return False
        return self.VerifySquenceOfBST(sequence[:left]) or self.VerifySquenceOfBST(sequence[left:length-1])
if __name__ == '__main__':
    sequence = [7,4,6,5]
    solution = Solution()
    print(solution.VerifySquenceOfBST(sequence))