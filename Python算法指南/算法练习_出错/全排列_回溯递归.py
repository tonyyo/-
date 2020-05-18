class Solution:
    def quanpailie(self, List, start, results):
        size = len(List)
        if start == size:
            results.append(list(List))  # 必须加上这个, 不然会默认排序
        for i in range(start, size):  # 以不同位置的元素作为开头进行全排列
            List[i], List[start] = List[start], List[i]
            self.quanpailie(List, start + 1, results)
            List[i], List[start] = List[start], List[i]
        return results


if __name__ == '__main__':
    List = ['a', 'a', 'b', 'b']
    result = []
    solution = Solution()
    result = solution.quanpailie(List, 0, result)
    for x in result:
        print(x)