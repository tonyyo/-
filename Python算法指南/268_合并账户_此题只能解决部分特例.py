import collections


class Solution:
    def accountsMerge(self, account):
        rowNum = len(account)
        queue = collections.deque()
        for i in range(rowNum):
            queue.append(account[i])
        while not self.NoRepeat(queue):
            first, sec = queue.popleft(), queue.popleft()  # 缺陷是两者必须是有交叉的, 才能继续, 而很遗憾, 此题排序的元素还不能排序
            if first[1] == sec[1]:
                tempFir, tempSec = first[1:], sec[1:]
                if set(tempFir) & set(tempSec):
                    temp = [first[0]] + list(set(tempFir) | set(tempSec))
                    queue.append(temp)
                else:
                    queue.append(first)
                    queue.append(sec)
            else:
                queue.append(first)
                queue.append(sec)
        return queue
    def NoRepeat(self, queue):
        rowNum = len(queue)
        for i in range(rowNum):
            for j in range(i + 1, rowNum):
                if queue[i][0] == queue[j][0]:
                    tempList1 = queue[i][1:]
                    tempList2 = queue[j][1:]
                    if set(tempList1) & set(tempList2):
                        return False
        return True

if __name__ == '__main__':
    accounts1 = [["John", "johnsmith@mail.com", "john00@mail.com"],
                 ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                 ["John", "johnnybravo@mail.com"],
                 ["Mary", "mary@mail.com"]]
    solution = Solution()
    result = solution.accountsMerge(accounts1)
    for x in result:
        print(x)
