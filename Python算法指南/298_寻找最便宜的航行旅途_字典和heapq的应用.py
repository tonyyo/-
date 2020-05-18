import heapq
class Solution:
    def findCheapestPrice1(self, n, flights, src, dst, K):
        map = {}
        for start, end, cost in flights:
            if start not in map:
                map[start] = [(cost, end)]
            else:
                map[start].append((cost, end))
        if src not in map:
            return -1
        hq = []
        for cost, next_stop in map[src]:
            heapq.heappush(hq, (cost, next_stop, 0))
        while hq:
            cml_cost, cur_stop, level = heapq.heappop(hq)
            if level > K:
                continue
            elif cur_stop == dst:
                return cml_cost
            if cur_stop in map:
                for next_cost, next_stop in map[cur_stop]:
                    heapq.heappush(hq, (cml_cost + next_cost, next_stop, level + 1))
        return -1

    def findCheapestPrice(self, n, flights, src, dst, K):
        dict = {}
        for start, end, cost in flights:
            if start not in dict:
                dict[start] = [[cost, end]]
            else:
                dict[start].append([cost, end])
        if src not in dict:  #  没有始发站
            return -1
        hp = []
        for cost, nextStop in dict[src]:
            heapq.heappush(hp, (cost, nextStop, 0))
        while hp:
            cur_cost, cur_stop, level = heapq.heappop(hp)
            if level > K:
                continue
            elif cur_stop == dst:
                return cur_cost
            if cur_stop in dict:
                for next_cost, nextStop in dict[cur_stop]:
                    heapq.heappush(hp, (cur_cost + next_cost, nextStop, level + 1))
        return -1

#主函数
if __name__ == '__main__':
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1
    print("城市总数 = ", n, "每条线路的价格 = ", flights, "出发站 = ", src, "终点站 = ", dst, "中转站 = ", k)
    solution = Solution()
    print("航班的价格是：", solution.findCheapestPrice(n, flights, src, dst, k))