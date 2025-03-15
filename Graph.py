from Node import Node

from typing import NewType

Distance = NewType('Distance', float)
NodeID = NewType('NodeID', int)

import networkx as nx
import matplotlib.pyplot as plt

# Graph contains all nodes in the graph

class Graph:
  def __init__(self):
    self.nodes = {}

  def getSize(self) -> int:
    return len(self.nodes)

  def getNode(self, nodeID: int) -> Node:
    if nodeID not in self.nodes:
      raise Exception('Node ' + str(nodeID) + ' is not in this graph')
    return self.nodes[nodeID]

  def addNode(self, nodeID: int) -> None:
    if nodeID not in self.nodes:
      self.nodes[nodeID] = Node(nodeID)

  def removeNode(self, nodeID: int) -> None:
    if nodeID not in self.nodes:
      raise Exception('Node ' + str(nodeID) + ' is not in this graph')
    for node in self.getNode(nodeID).getConnections():
      self.getNode(node).disconnect(nodeID)
    del self.nodes[nodeID]

  def connectNodes(self, initialNodeID: NodeID, finalNodeID: NodeID, distance: Distance) -> None:
    if initialNodeID not in self.nodes:
      raise Exception('Initial node does not exist')
    if finalNodeID not in self.nodes:
      raise Exception('Final node does not exist')
    self.getNode(initialNodeID).connect(finalNodeID, distance)
    self.getNode(finalNodeID).connect(initialNodeID, distance)

  def disconnectNodes(self, initialNodeID: NodeID, finalNodeID: NodeID) -> None:
    self.getNode(initialNodeID).disconnect(finalNodeID)
    self.getNode(finalNodeID).disconnect(initialNodeID)

  def getConnections(self, nodeID: NodeID) -> list[NodeID]:
    return self.getNode(nodeID).getConnections()

  def connectAll(self, nodeList: list[NodeID]) -> None: # Strongly connect all node in the list
    for i in range(len(nodeList)):
      for j in range(i + 1, len(nodeList)):
        self.connectNodes(nodeList[i], nodeList[j], 1)

  def listNodes(self) -> list[NodeID]:
    return list(self.nodes.keys())

  def isConnected(self, initialNode: int, finalNode: int) -> bool:
    if initialNode in self.nodes:
      return self.nodes[initialNode].isConnectedTo(finalNode);
    return False

  def getDistance(self, initialNodeID: int, finalNodeID: int) -> float:
    return self.getNode(initialNodeID).getDistanceTo(finalNodeID)

  def getDegree(self, nodeID: int) -> int:
    if nodeID not in self.nodes:
      raise Exception('Node ' + str(nodeID) + ' is not in this graph')
    return self.nodes[nodeID].getDegree()

  def getLowestDegree(self) -> int:
    if not self.nodes:
        raise ValueError("Graph is empty")
    return min(self.nodes.keys(), key=lambda node: self.nodes[node].getDegree())

  def draw(self):
    edgeList = []
    for node in self.nodes.values():
        for connection in node.getConnections():
            edge = tuple(sorted((node.toString(), str(connection))))
            edgeList.append(edge)
    G = nx.Graph()
    G.add_edges_from(edgeList)
    nx.draw_spring(G, with_labels=True)
    plt.show()