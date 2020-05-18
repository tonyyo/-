class CircularQueue:
    def __init__(self, n):
        self.queue = [] # 循环数组
        self.size = n
        self.head = 0
    def isFull(self):
        return len(self.queue) - self.head == self.size
    def isEmpty(self):
        return len(self.queue) - self.head == 0
    def enqueue(self, element):
        self.queue.append(element) # 增加一个元素
#返回值是队列中弹出的元素
    def dequeue(self):
        self.head += 1   # 头指针+1后，表示删除了第一个元素
        return self.queue[self.head - 1] # 返回删除的元素
#主函数
if __name__=="__main__":
    #创建对象
    cir=CircularQueue(5)
    print("isFull()=>",cir.isFull())
    print("isEmpty() =>",cir.isEmpty())
    cir.enqueue(1)
    print("dequeue()  =>",cir.dequeue())