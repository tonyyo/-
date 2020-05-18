class Solution:
    def sameNumber(self, nums, k):
        vis = {}
        for i in range(len(nums)):
            x = nums[i]
            if x in vis:
                if vis[x] - i < k:
                    return "YES"
            vis[x] = i
        return "NO"
# 主函数
if __name__ == "__main__":
     nums=[1,2,3,1,5,9,3]
     k=4
     #创建对象
     solution=Solution()
     print("输入的数是：",nums,"给定的k=",k)
     print("输出的结果是：",solution.sameNumber(nums,k))