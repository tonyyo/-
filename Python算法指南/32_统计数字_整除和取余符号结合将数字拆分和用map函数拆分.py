import collections
class Solution:
    def digitCounts(self, k, n):  # 利用封装的函数实现
        count = 0
        for i in range(n + 1):
            list = map(int, str(i))  # 将数字转化为列表, 第二个参数必须为字符串
            dict = collections.Counter(list)  # 返回的是一个字典, 键具体类型由list中值的类型决定
            count += dict[k]
        return count

    def digitCounts2(self, k, n):
        count = 0
        for i in range(n + 1):
            j = i
            while True:
                if j % 10 == k:
                    count += 1
                j //= 10
                if j == 0:
                    break
        return count

if __name__ == '__main__':
    temp = Solution()
    k1 = 1
    n1 = 11
    k2 = 2
    n2 = 22
    print(("输入："+str(k1)+"  "+str(n1)))
    print(("输出："+str(temp.digitCounts(k1,n1))))
    print(("输入："+str(k2)+"  "+str(n2)))
    print(("输出："+str(temp.digitCounts2(k2,n2))))