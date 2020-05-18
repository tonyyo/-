class Solution:
    def smallestDifference(self, A, B):
        C = []
        for x in A:
            C.append((x, 'A'))
        for x in B:
            C.append((x, 'B'))
        C.sort()
        diff = 0x7fffffff
        cnt = len(C)
        for i in range(cnt - 1):
            if  C[i][1] != C[i + 1][1]:  # 比较字母是否相同, 不相同则条件成立
                diff = min(diff, C[i + 1][0] - C[i][0])  # C相当于一个len(A) + len(B)行和两列的数组
        return diff
if __name__ == '__main__':
    temp = Solution()
    List1 = [5,6,4,2,3]
    List2 = [1,1,1,1,1]
    print(("输入："+str(List1)+"  "+str(List2)))
    print(("输出："+str(temp.smallestDifference(List1,List2))))