class Solution:
    def canJump(self, A):
        p = 0
        ans = 0
        for item in A[:-1]: # 舍去了最后一个字符，很聪明
            ans = max(ans, p + item)
            if (ans <= p): # 如果item是0的话就返回False，但这里有一个bug，当item是负数的话也会返回False
                return False # 其实为负数是可以跳出的，例如2,4,1,-2,1,1
            p += 1
        return True

if __name__ == '__main__':
    temp = Solution()
    List1 = [1, 1, 0, 2]
    List2 = [1, 2, 0, 1, 2, 1]
    print(("输入：" + str(List1)))
    print(("输出：" + str(temp.canJump(List1))))
