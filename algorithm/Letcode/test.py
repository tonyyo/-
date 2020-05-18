class Solution():
    def mirror(self, Str):
        N = len(Str)
        mid = (N - 1) // 2
        if N % 2 == 0:
            return Str[:mid + 1] + Str[mid::-1]
        else:
            return Str[:mid + 1] + Str[mid - 1::-1]

    def get_small(self, Str):
        if int(self.mirror(Str)) < int(Str):  # 镜像回文串小于原数，就是小回文串
            return self.mirror(Str)
        N = len(Str)
        mid = (N - 1) // 2
        if N % 2 == 0:
            LeftHalf = str(int(Str[:mid + 1]) - 1)
            return LeftHalf + LeftHalf[::-1]
        else:
            LeftHalf = str(int(Str[:mid]) -1)
            return LeftHalf + Str[mid] + LeftHalf[::-1]

    def get_big(self, Str):
        if int(self.mirror(Str)) > int(Str):
            return self.mirror(Str)
        N = len(Str)
        mid = (N - 1) // 2
        if N % 2 == 0:
            LeftHalf = str(int(Str[:mid + 1]) + 1)
            return LeftHalf + LeftHalf[::-1]
        else:
            LeftHalf = str(int(Str[:mid + 1]) + 1)
            return LeftHalf + Str[mid] + LeftHalf[::-1]

if __name__ == '__main__':
    solution = Solution()
    Str = "123101"
    print(solution.get_small(Str))
    print(solution.get_big(Str))
