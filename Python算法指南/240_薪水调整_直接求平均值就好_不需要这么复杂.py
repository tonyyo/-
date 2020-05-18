class Solution:
    def getCap(self, a, target):
        a.sort()
        l, r = a[0], a[len(a)-1]
        while l+1<r:
            mid = l + ((r-l)>>1)
            ans = self.total(a, mid)
            if ans > target:
                r = mid
            elif ans < target:
                l = mid
            else:
                return mid
        if self.total(a, l) == target:
            return l
        if self.total(a, r) == target:
            return r
    def total(self, a, mid):
        res = 0
        for n in a:
            res += max(n, mid)
        return res
if __name__ == '__main__':
    temp = Solution()
    A = [1,2,3,4,5]
    target = 25
    print("输入："+str(A))
    print("输入："+str(target))
    print("输出："+str(temp.getCap(A,target)))