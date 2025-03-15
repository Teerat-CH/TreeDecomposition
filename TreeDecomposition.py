from Graph import Graph
from Tree import Tree
from Bag import Bag

from collections import deque 
import copy

def generateRank(eliminationOrder):
    rank = [-1] * (len(eliminationOrder)*2)
    for i, e in enumerate(eliminationOrder):
        rank[e] = i
    return rank


def TreeDecomposition(graph: Graph, eliminationOrder: list[int]) -> Tree:
  bagIDCount = 1
  tree = Tree()
  for nodeID in eliminationOrder:
    # add that node and its connections to the tree as a bag
    node = graph.getNode(nodeID)
    tree.addNode(bagIDCount, copy.deepcopy(node), nodeID)
    bagIDCount += 1
    # strongly connect node's connections
    # graph.connectAll(node.getConnections())
    # remove that node from the graph
    graph.removeNode(nodeID)

  rank = generateRank(eliminationOrder) # for faster checking which bag got eliminate first

  # Connecting the generated bags
  for bag in tree.nodes.values(): # For each bag, look for the connection that got eliminate first except itself and set it as a parent
    eliminateFirstRank = float('inf')
    for connection in bag.node.getConnections():
      if rank[connection] < eliminateFirstRank:
        eliminateFirstRank = rank[connection]
    if eliminateFirstRank != float('inf'):
      tree.connectNodes(rank[bag.head] + 1, eliminateFirstRank + 1, 1)
      tree.nodes[rank[bag.head] + 1].parent = tree.nodes[eliminateFirstRank + 1]

  # assigned the root to the tree
  randomNode = tree.nodes[1] # find the root by traversing through parents of each node
  while randomNode.parent is not None:
    randomNode = randomNode.parent
  tree.root = randomNode

  # TODO removing bags that are subset of other bag
  # BFS Search the tree to remove the node that are subset of its connection
  
  return tree