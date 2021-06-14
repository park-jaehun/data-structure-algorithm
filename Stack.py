from SLS import SinglyLinkedList
class Stack(object):
    IstIstance = SinglyLinkedList()
    def pop(self):
        return self.IstIstance.removeAt(0)
    def push(self,value):
        return self.IstIstance.insertAt(value, 0)
    def printStack(self):
        return self.IstIstance.printStatus()

stack = Stack()
stack.push("a")
stack.push("b")
stack.push("c")

print(stack.pop())
print(stack.printStack())
