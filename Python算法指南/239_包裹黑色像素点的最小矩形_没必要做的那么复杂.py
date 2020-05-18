class Solution(object):
    def minArea1(self, image, x, y):
        m = len(image)
        if m == 0:
            return 0
        n = len(image[0])
        if n == 0:
            return 0
        start = y
        end = n - 1
        while start < end:
            mid = start + (end - start) // 2 + 1
            if self.checkColumn(image, mid):
                start = mid
            else:
                end = mid - 1
        right = start
        start = 0
        end = y
        while start < end:
            mid = start + (end - start) // 2
            if self.checkColumn(image, mid):
                end = mid
            else:
                start = mid + 1
        left = start
        start = x
        end = m - 1
        while start < end:
            mid = start + (end - start) // 2 + 1
            if self.checkRow(image, mid):
                start = mid
            else:
                end = mid - 1
        down = start
        start = 0
        end = x
        while start < end:
            mid = start + (end - start) // 2
            if self.checkRow(image, mid):
                end = mid
            else:
                start = mid + 1
        up = start
        return (right - left + 1) * (down - up + 1)

    def checkColumn(self, image, col):
        for i in range(len(image)):
            if image[i][col] == '1':
                return True
        return False

    def checkRow(self, image, row):
        for j in range(len(image[0])):
            if image[row][j] == '1':
                return True
        return False

    def minArea(self, image):
        minX, minY, maxX, maxY = 65536, 65536, 0, 0
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == '1':
                    minX = min(minX, i)
                    minY = min(minY, j)
                    maxX = max(maxX, i)
                    maxY = max(maxY, j)
        return (maxX - minX + 1) * (maxY - minY + 1)


if __name__ == '__main__':
    temp = Solution()
    image = ["1000", "1100", "0110"]
    x = 1
    y = 2
    print(("输入：" + str(image)))
    print(("输入：" + str(x) + "," + str(y)))
    print(("输出：" + str(temp.minArea(image))))
