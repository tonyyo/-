class Solution:
    def DeleteDigits(self, A, k):
        A = list(A)
        while k > 0:  #删除k个数
            f = True  # 只能删掉一个数
            for i in range(len(A)-1):
                if A[i] > A[i+1]:   #从左向右遍历, 删除左边更大的值, 因为要尽量保证左边高位上的数尽可能小
                    del A[i]  # del可以指定删除列表某个位置的元素
                    f = False
                    break    #因为这个地方已经改变了len的长度, 循环的条件已经改变,所以要用break
            if f and len(A)>1: #如果始终右边比左边大, 说明这是一个有序列表, 那么就删除最后一个数
                A.pop()
            k -= 1
        while len(A)>1 and A[0]=='0':  #如果第一位是0, 那么就删掉, 这也是为啥说删掉k个数, 而不是保留n-k个数
            del A[0]
        return ''.join(A)

if __name__ == '__main__':
    temp = Solution()
    num_str = "178542"
    k = 4
    print(("输入："+num_str+"  "+str(k)))
    print(("输出："+str(temp.DeleteDigits(num_str,k))))


