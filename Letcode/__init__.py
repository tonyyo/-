import heapq
queue = [1, 2, 3, 4]
heapq.heapify(queue)
print(heapq.heappop(queue))
print(queue)