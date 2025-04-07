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

def contractSubsetNode(tree: Tree, bag: Bag):
  # if the bag is subset of one of its children
  for connection in bag.getConnections():
    connection = tree.getNode(connection)

    # get parent's name
    parentToString = ""
    if bag.parent is not None:
      parentsName = bag.parent.toString()

    if connection.toString() != parentToString and bag.isSubsetOf(connection):
      # if the bag to be remove is root, change the root to the replacer
      if bag.name == tree.root.name:
        tree.root = connection
      # set the connection parent to be the bag parent
      connection.parent = bag.parent
      # change all the bag's connection to connect to the replacer
      for connection2 in bag.getConnections():
        if connection2 != connection.name:
          tree.connectNodes(connection2, connection.name, 1)
      # remove the bag from the tree
      tree.removeNode(bag.name)
      contractSubsetNode(tree, connection)
      break

def removeSubsetNode(tree: Tree):
  keys = list(tree.nodes.keys()) 
  for key in keys:
    if key in tree.nodes:
      bag = tree.getNode(key)
      contractSubsetNode(tree, bag)

def TreeDecomposition(graph: Graph, eliminationOrder: list[int], fully = False) -> Tree:
  bagIDCount = 1
  tree = Tree()
  for nodeID in eliminationOrder:
    # add that node and its connections to the tree as a bag
    node = graph.getNode(nodeID)
    tree.addNode(bagIDCount, copy.deepcopy(node), nodeID)
    bagIDCount += 1
    # strongly connect node's connections
    graph.connectAll(node.getConnections())
    # remove that node from the graph
    graph.removeNode(nodeID)

  # Connecting the generated bags
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

  if fully: # to fully form a final tree decomposition. This is not necessary to get a treewidth. 
  # TODO: Need to look into this part more as it might not work in the case that we have a forest rather than a tree.
    randomNode = tree.nodes[1] # find the root by traversing through parents of each node
    while randomNode.parent is not None:
      randomNode = randomNode.parent
    tree.root = randomNode

    # remove node that are subset of its connections
    removeSubsetNode(tree)

  return tree