class Node:
    nodeNext = None
    nodePrev = ''
    objValue =''
    binHead = False
    binTail = False
    def __init__(self, objValue='', nodeNext = None, binHead = False, binTail=False):
        self.nodeNext = nodeNext
        self.objValue = objValue
        self.binHead = binHead
        self.binTail = binTail
    def getValue(self):
        return self.objValue
    def setValue(self, objValue):
        self.objValue = objValue
    def getNext(self):
        return self.nodeNext
    def setNext(self,nodNext):
        self.nodeNext = nodNext
    def isHead(self):
        return self.binHead
    def isTail(self):
        return self.binTail

node1 = Node(objValue = 'a')
nodeTail = Node(binTail = True)
nodeHead = Node(binHead = True, nodeNext = node1)


class SinglyLinkedList:
    nodeHead = ''
    nodeTail = ''
    size = 0
    def __init__(self):
        self.nodeTail = Node(binTail=True)
        self.nodeHead = Node(binHead = True, nodeNext = self.nodeTail)

    def insertAt(self, objInsert, idxInsert):
        nodeNew = Node(objValue=objInsert)
        nodePrev = self.get(idxInsert - 1)
        nodeNext = nodePrev.getNext()
        nodePrev.setNext(nodeNew)
        nodeNew.setNext(nodeNext)
        self.size = self.size + 1

    def removeAt(self, idxRemove):
        nodePrev = self.get(idxRemove - 1)
        nodeRemove = nodePrev.getNext()
        nodeNext = nodeRemove.getNext()
        nodePrev.setNext(nodeNext)
        self.size = self.size - 1
        return nodeRemove.getValue()


    def get(self,idxRetrive):
        nodeReturn = self.nodeHead
        for itr in range(idxRetrive + 1):
            nodeReturn = nodeReturn.getNext()
        return nodeReturn

    def printStatus(self):
        nodeCurrent = self.nodeHead
        while nodeCurrent.getNext().isTail() == False:
            nodeCurrent = nodeCurrent.getNext()
            print(nodeCurrent.getValue(),)
        print("")

    def getSize(self):
        return self.size

list1 = SinglyLinkedList()
list1.insertAt("a", 0)
list1.insertAt("b", 1)
list1.insertAt("c", 2)
list1.insertAt("d",3)
list1.printStatus()

list1.insertAt("e",4)
list1.printStatus()

list1.removeAt(3)
list1.printStatus()





