# coding=<euc-kr>
from SLS import SinglyLinkedList
class Queue(object):
    IsInstance = SinglyLinkedList()
    def Enque(self,value):
        return self.IsInstance.insertAt(value,0)
    def Deque(self):
        size = self.IsInstance.getSize()
        return self.IsInstance.removeAt(size - 1)
    def QueStatus(self):
        return self.IsInstance.printStatus()

queue = Queue()
queue.Enque("a")
queue.Enque("b")
queue.Enque("c")
queue.Enque("d")
queue.Deque()
queue.Deque()
print(queue.QueStatus())