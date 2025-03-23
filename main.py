from Graph import Graph
from Tree import Tree
from TreeDecomposition import TreeDecomposition
from EliminationOrder import DynamicMinimumDegree
import copy

with open('./data.txt', 'r') as file:
    data = file.readlines()

graph = Graph()
for line in data:
  values = line.strip().split(" ")
  graph.addNode(int(values[1]))
  graph.addNode(int(values[2]))
  graph.connectNodes(int(values[1]), int(values[2]), float(values[3]))

tree = TreeDecomposition(graph, DynamicMinimumDegree(copy.deepcopy(graph)))
tree.draw()