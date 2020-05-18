class LinkedNode:
    def __init__(self, val=None, next=None):
        self.value = val
        self.next = next
class DataStream:
    def __init__(self):
        # do intialization if necessary
        self.dic = {}
        self.head = LinkedNode()
        self.tail = self.head
        self.visited = set()
#参数num是数据流中的下一个数字
#没有返回值
    def add(self, num):
        if num in self.visited:
            return
        else:
            if num in self.dic:
                self.remove(num)
                self.visited.add(num)
            else:
                self.dic[num] = self.tail  # 存的是前一个node的信息
                node = LinkedNode(num)
                self.tail.next = node
                self.tail = node
    #返回数据流中第一个独特的数字
    def firstUnique(self):
        # print(self.dic)
        # print(self.head.next.next.value)
        if self.head.next != None:
            return self.head.next.value
        return -1
    def remove(self, num):
        prev = self.dic[num]
        prev.next = prev.next.next
        del self.dic[num]
        #改变dic中对应的信息
        if prev.next != None:
            self.dic[prev.next.value] = prev
        else:
            self.tail = prev
#主函数
if __name__=="__main__":
    list1=[]
    solution=DataStream()
    solution.add(1)
    solution.add(2)
    list1.append(solution.firstUnique())
    solution.add(1)
    list1.append(solution.firstUnique())
    print("输入的内容分别是：add(1),add(2),firstUnique(),add(1),firstUnique()")
    print("最终得到的结果是：",list1)