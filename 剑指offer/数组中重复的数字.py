class Solution:
    def duplicate(self, numbers, duplication):
        N = len(numbers)
        i = 0
        while True:
            if numbers[i] == i:
                i += 1
                if i >= N:
                    break
            if numbers[i] == numbers[numbers[i]]:
                # duplication.append(numbers[i])
                duplication[0] = numbers[i]
                return True
            tmp = numbers[i]
            numbers[i] = numbers[tmp]
            numbers[tmp] = tmp
        return False

if __name__ == '__main__':
    solution = Solution()
    numbers = [3,4,5,1,2,0]
    solution.duplicate(numbers, [])
    print numbers