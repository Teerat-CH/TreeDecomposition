# A node contains the number of its degree and its edges (connection and distance) to other nodes

from typing import NewType

Distance = NewType('Distance', float)
NodeID = NewType('NodeID', int)

class Node:
  def __init__(self, nodeID: int) -> None:
    self.degree: int = 0
    self.connection: dict[NodeID, Distance] = {}
    self.head = nodeID

  def connect(self, nodeToConnect: int, distance: float) -> None:
    if nodeToConnect not in self.connection:
      self.connection[nodeToConnect] = distance
      self.degree += 1

  def disconnect(self, nodeToDisconnect: int) -> None:
    if nodeToDisconnect in self.connection:
      del self.connection[nodeToDisconnect]
      self.degree -= 1

  def isConnectedTo(self, ID: int) -> bool:
    return ID in self.connection

  def getDegree(self) -> int:
    return self.degree

  def getConnections(self) -> list[NodeID]:
    return list(self.connection.keys())

  def getDistanceTo(self, nodeID: int) -> Distance:
    if nodeID not in self.connection:
      raise Exception('Node ' + str(nodeID) + ' is not connected to this node')
    return self.connection[nodeID]

  def toString(self):
    return str(self.head)