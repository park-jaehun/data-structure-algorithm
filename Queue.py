# coding=<euc-kr>
from collections import deque

deq = deque([2,3,4,5,6])
print(deq)
deq.appendleft(1)
print(deq)
deq.appendleft(3)
print(deq)
deq.popleft()
print(deq)

#
# from SLS import SinglyLinkedList
# class Queue(object):
#     IsInstance = SinglyLinkedList()
#     def Enque(self,value):
#         return self.IsInstance.insertAt(value,0)
#     def Deque(self):
#         size = self.IsInstance.getSize()
#         return self.IsInstance.removeAt(size - 1)
#     def QueStatus(self):
#         return self.IsInstance.printStatus()
#
# queue = Queue()
# queue.Enque("a")
# queue.Enque("b")
# queue.Enque("c")
# queue.Enque("d")
# queue.Deque()
# queue.Deque()
# print(queue.QueStatus())