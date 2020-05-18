class Solution:
    def hashCode(self, key, HASH_SIZE):
        ans = 0
        for x in key:
            ans = (ans * 33 + ord(x)) % HASH_SIZE
        return ans
#主函数
if __name__ == "__main__":
    key = "abcd"
    size = 100
    #创建对象
    solution = Solution()
    print("输入的字符串是 ", key, "哈希表的大小是:", size)
    print("输出的结果是：", solution.hashCode(key, size))
