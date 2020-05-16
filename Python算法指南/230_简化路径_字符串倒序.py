class Solution:
    def simplifyPath1(self, path):
        stack = []
        i = 0
        res = ''
        while i < len(path):
            end = i+1
            while end < len(path) and path[end] != "/":
                end += 1
            sub=path[i+1:end]
            if len(sub) > 0:
                if sub == "..":
                    if stack != []: stack.pop()
                elif sub != ".":
                    stack.append(sub)
            i = end
        if stack == []: return "/"
        for i in stack:
            res += "/"+i
        return res

    def simplifyPath(self, path):
        path = path[::-1]
        index1 = path.index("/", 1)
        print("/" + path[1: index1][::-1])

#主函数
if __name__=="__main__":
    path="/x/"
    #创建对象
    solution=Solution()
    print("输入的路径是：",path)
    print("路径简化后的结果：",solution.simplifyPath(path))