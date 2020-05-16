class Solution:
    def search(self, A, target):
        for num in A:
            if num == target:
                return True
        return False
if __name__ == '__main__':
    temp = Solution()
    List1 = [1,2,4,5,6,7,8]
    target = 5
    print(("输入："+str(List1)+"  "+str(target)))
    print(("输出："+str(temp.search(List1,target))))