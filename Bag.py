from Node import Node

# An inherited class from Node to represent tree bag

class Bag(Node):
  def __init__(self, node: Node, nodeID: int, bagID: int) -> None:
    super().__init__(nodeID)
    self.node = node
    self.name = bagID
    self.parent = None

  def getMember(self) -> set:
    memberSet = {int(self.head)}
    for connection in self.node.getConnections():
      memberSet.add(int(connection))
    return memberSet
  
  def isSubsetOf(self, bag2): # return true if bag1 is the subset of bag2
    return self.getMember().issubset(bag2.getMember())

  def toString(self) -> str:
    name = '(' + str(self.head)
    for connection in self.node.getConnections():
      name += ', ' + str(connection)
    return name + ')'