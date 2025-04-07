# A node contains the number of its degree and its edges (connection and distance) to other nodes

from typing import NewType
from sortedcontainers import SortedDict
import networkx as nx
import matplotlib.pyplot as plt
import copy

from Graph import Graph
from Tree import Tree
from Bag import Bag

from EliminationOrder import DynamicMinimumDegree
from TreeDecomposition import TreeDecomposition

if __name__ == "__main__":
  file_path = 'data.txt'
  with open(file_path, 'r') as file:
    data = file.readlines()

  graph = Graph()
  for line in data:
    values = line.strip().split(" ")
    graph.addNode(int(values[1]))
    graph.addNode(int(values[2]))
    graph.connectNodes(int(values[1]), int(values[2]), float(values[3]))
  order = DynamicMinimumDegree(copy.deepcopy(graph))
  tree = TreeDecomposition(copy.deepcopy(graph), order, fully=True)
  tree.draw()