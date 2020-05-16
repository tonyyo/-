class Solution:
    def missingString(self, str1, str2):
        result = []
        dict = set(str2.split())
        for word in str1.split():
            if word not in dict:
                result.append(word)
        return result

    def missingString(self, str1, str2):
        listStr1 = str1.strip().split()
        listStr2 = str2.strip().split()
        listSet = list(set(listStr1) - set(listStr2))
        return listSet


if __name__ == "__main__":
    str1 = "This is an example"
    str2 = "is example"

    solution = Solution()
    print("输入的两个字符串是str1=", str1, "str2=", str2)
    print("输出的结果是：", solution.missingString(str1, str2))
