class Sollution:
    def countSmaller(self, A, q):  # 在有序列表中找到一个数
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] < q:
                left = mid
            else:
                right = mid
        if left == 0:  # 只有这种情况, left才可能等于要查找的数, 不然要查找的数一定是大于这个位置的值的
            return 0
        return left + 1

    def countOfSmallerNumber(self, A, queries):
        ans = []
        for i in queries:
            ans.append(self.countSmaller(A, i))
        return ans

if __name__ == '__main__':
    A = [1,2,3,4,5,6,7,8,9,0]
    A = sorted(A)
    solution = Sollution()
    print(solution.countOfSmallerNumber(A, [1, 8, 5]))

# class Sollution:
#     def countSmaller(self, A, q):
#         if len(A) == 0 or A[-1] < q: #如果给定数组的长度等于0, 或者要查询的数大于数组中的最大数, 返回整个数组长度
#             return len(A)
#         start, end = 0, len(A) - 1
#         while start + 1 < end:  #等start与end左右相邻时跳出循环, 当查找值可能不在数组中时, 循环跳出条件不能是start == end
#             mid = (start + end) // 2
#             if A[mid] < q:
#                 start = mid
#             else:
#                 end = mid
#         if A[start] >= q: #当start和end相邻时,说明二者中肯定有一个是大于或等于q的, 所以先判断start, 后判断end
#             return start
#         if A[end] >= 1:
#             return end
#         return end + 1  # 可有可无
#
#     def countOfSmallerNumber(self, A, queries):
#         A = sorted(A)  #排序直接用sorted
#         results = []
#         for q in queries:
#             results.append(self.countSmaller(A, q))
#         return results