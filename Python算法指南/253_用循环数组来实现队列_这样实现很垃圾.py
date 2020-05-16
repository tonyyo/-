class CircularQueue:
    def __init__(self, n):
        self.queue = []
        self.size = n
        self.head = 0
    def isFull(self):
        return len(self.queue) - self.head == self.size
    def isEmpty(self):
        return len(self.queue) - self.head == 0
    def enqueue(self, element):
        self.queue.append(element)
#返回值是队列中弹出的元素
    def dequeue(self):
        self.head += 1
        return self.queue[self.head - 1]
#主函数
if __name__=="__main__":
    #创建对象
    cir=CircularQueue(5)
    print("isFull()=>",cir.isFull())
    print("isEmpty() =>",cir.isEmpty())
    cir.enqueue(1)
    print("dequeue()  =>",cir.dequeue())