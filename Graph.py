from Node import Node
import heapq
from typing import NewType

Distance = NewType('Distance', float)
NodeID = NewType('NodeID', int)

import networkx as nx
import matplotlib.pyplot as plt

# Graph contains all nodes in the graph

class Graph:
  def __init__(self):
    self.nodes = {}
    self.heap = []

  def getSize(self) -> int:
    return len(self.nodes)

  def getNode(self, nodeID: int) -> Node:
    if nodeID not in self.nodes:
      raise Exception('Node ' + str(nodeID) + ' is not in this graph')
    return self.nodes[nodeID]

  def addNode(self, nodeID: int) -> None:
    if nodeID not in self.nodes:
      self.nodes[nodeID] = Node(nodeID)

    # TODO add the node representation to heap with degree = 0
    heapq.heappush(self.heap, (0, nodeID))

  def removeNode(self, nodeID: int) -> None:
    if nodeID not in self.nodes:
      raise Exception('Node ' + str(nodeID) + ' is not in this graph')
    for node in self.getNode(nodeID).getConnections():
      self.disconnectNodes(nodeID, node)
    del self.nodes[nodeID]

  def connectNodes(self, initialNodeID: NodeID, finalNodeID: NodeID, distance: Distance) -> None:
    if initialNodeID not in self.nodes:
      raise Exception('Initial node does not exist')
    if finalNodeID not in self.nodes:
      raise Exception('Final node does not exist')
    self.getNode(initialNodeID).connect(finalNodeID, distance)
    self.getNode(finalNodeID).connect(initialNodeID, distance)

    # TODO readd all the nodes representation to the heap with their update degree
    heapq.heappush(self.heap, (self.getDegree(initialNodeID), initialNodeID))
    heapq.heappush(self.heap, (self.getDegree(finalNodeID), finalNodeID))

  def disconnectNodes(self, initialNodeID: NodeID, finalNodeID: NodeID) -> None:
    self.getNode(initialNodeID).disconnect(finalNodeID)
    self.getNode(finalNodeID).disconnect(initialNodeID)

    # TODO readd all the nodes representation to the heap with their updated degree
    heapq.heappush(self.heap, (self.getDegree(initialNodeID), initialNodeID))
    heapq.heappush(self.heap, (self.getDegree(finalNodeID), finalNodeID))

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
    # return min(self.nodes.keys(), key=lambda node: self.nodes[node].getDegree())
  
    # TODO rewrite this to pop the lowest degree node from the heap. Check if the popped one has the correct degree from your dict. If yes keep it. If not keep popping.
    while self.heap:
      print(self.heap)
      degree, nodeID = self.heap[0]
      if nodeID in self.nodes:
        if degree == self.getDegree(nodeID):
          return nodeID
      heapq.heappop(self.heap)
    raise ValueError("Graph is empty")

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