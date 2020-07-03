class Node:
    def __init__(self, key = 0, val = 0): # 这样的话相当于兼容了默认构造函数的作用
        self.key = key
        self.val = val
        self.pre = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()         # map, key是节点的key，val是节点
        self.capacity = capacity    # 最大容量
        self.size = 0               # 初始容量
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail  # 双向链表
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.moveToHead(node)
        else:
            newNode = Node(key, value)
            if self.size <= self.capacity:
                self.putToHead(newNode)
                self.cache[key] = newNode  # map和双向列表都要加入
            else:
                self.removeTail()
                self.putToHead(newNode)
                self.cache[key] = newNode

    def removeTail(self):
        last = self.tail.pre
        lastSec = last.pre
        lastSec.next = last.next
        self.tail.pre = lastSec

    def putToHead(self, node):
        node.next = self.head.next
        self.head.next.pre = node
        node.pre = self.head
        self.head.next = node

    def moveToHead(self, node):
        pre = node.pre
        post = node.next
        pre.next = post
        post.pre = pre    # 先要删除节点
        node.next = self.head.next
        self.head.next.pre = node
        node.pre = self.head
        self.head.next = node  # 再插入节点
