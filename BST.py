class TreeNode:
    nodeLHS = None
    nodeRHS = None
    nodeParent = None
    value = None

    def __init__(self,value, nodeParent):
        self.value = value
        self.nodeParent = nodeParent

    def getLHS(self):
        return self.nodeLHS
    def getRHS(self):
        return self.nodeRHS
    def getValue(self):
        return self.value
    def getParent(self):
        return self.nodeParent
    def setLHS(self,LHS):
        self.nodeLHS = LHS
    def setRHS(self,RHS):
        self.nodeRHS = RHS
    def setValue(self,value):
        set.value = value
    def setParent(self, nodeParent):
        self.nodeParent = nodeParent

class BinarySearchTree:
    root = None

    def __init__(self):
        pass
    def insert(self, value, node = None):
        if node is None:
            node = self.root
        if self.root is None:
            self.root = TreeNode(value, None)
            return
        if value == node.getValue():
            return

        if value > node.getValue():
            if node.getRHS() is None:
                node.setRHS(TreeNode(value,node))
            else:
                self.insert(value, node.getRHS())


        if value < node.getValue():
            if node.getLHS() is None:
                node.setLHS(TreeNode(value,node))

            else:
                self.insert(value, node.getLHS())

        return





