import collections
import copy


class Solution:
    def canCompleteCircuit(self, gas, cost):
        size = len(gas)
        tempQueue1 = collections.deque()  # 模板
        tempQueue2 = collections.deque()
        result = []
        for j in range(size):
            tempQueue1.append(gas[j])
            tempQueue2.append(cost[j])
        for i in range(size):
            queue1, queue2 = copy.deepcopy(tempQueue1), copy.deepcopy(tempQueue2)
            flag = True
            for _ in range(i):  # 从不同的起点出发
                temp1 = queue1.popleft()
                temp2 = queue2.popleft()
                queue1.append(temp1)
                queue2.append(temp2)
            carOil = 0
            for j in range(len(gas)):
                carOil += queue1[j] - queue2[j]
                if carOil < 0:
                    flag = False
                    break
            if flag:
                result.append(i)
        return result[0] if len(result) != 0 else -1


if __name__ == '__main__':
    temp = Solution()
    List1 = [3,3,4]
    List2 = [3,4,4]
    print(("输入："+str(List1)+"  "+str(List2)))
    print(("输出："+str(temp.canCompleteCircuit(List1,List2))))