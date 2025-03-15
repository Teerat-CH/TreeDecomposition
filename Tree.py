from Node import Node
from Graph import Graph
from Bag import Bag

import copy
import networkx as nx
from matplotlib import pyplot as plt

# An inherited class from Graph to represent Tree

class Tree(Graph):
  def __init__(self):
    super().__init__()
    self.nodes = {}
    self.width = -1
    self.root = None

  def addNode(self, bagID: int, processedNode: Node, processedNodeID: int) -> None:
    if bagID not in self.nodes:
      self.nodes[bagID] = Bag(copy.deepcopy(processedNode), processedNodeID, bagID)
      bagSize = processedNode.getDegree() + 1
      if bagSize > self.width:
        self.width = bagSize - 1

  def listNodes(self) -> list[int]:
    return [bag.toString() for bag in self.nodes.values()]

  def getTreeWidth(self) -> int:
    return self.width

  def draw(self):
    edgeList = []
    for node in self.nodes.values():
        for connection in node.getConnections():
            edge = tuple(sorted((node.toString(), self.getNode(connection).toString())))
            edgeList.append(edge)
    G = nx.Graph()
    G.add_edges_from(edgeList)
    nx.draw_spring(G, with_labels=True)
    plt.show()