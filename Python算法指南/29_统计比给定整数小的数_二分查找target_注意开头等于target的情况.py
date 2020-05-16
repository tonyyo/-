class Sollution:
    def countOfSmallerNumber(self, A, queries):
        ans = []
        for x in queries:
            ans.append(self.count(A, x))
        return ans
    def count(self, A, x):
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] < x:
                left = mid
            else:
                right = mid
        if A[left] == x:  # 有一种特殊情况left会指向target, 就是target等于开头时
            return A.index(A[left])
        return A.index(A[right])

if __name__ == '__main__':
    A = [1,2,3,4,5,6,7,8,9]
    A = sorted(A)
    solution = Sollution()
    print(solution.countOfSmallerNumber(A, [1, 8, 5]))