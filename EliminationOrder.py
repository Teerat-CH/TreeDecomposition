import random

def RandomEliminationOrder(graph, seed=None):
  if seed is not None:
    random.seed(seed)
  listNodes = graph.listNodes();
  random.shuffle(listNodes)
  return listNodes

def StaticMinimumDegree(graph):
  SMD = []
  while graph.getSize() > 0:
    lowestDegree = graph.getLowestDegree()
    SMD.append(lowestDegree)
    del graph.nodes[lowestDegree]
  return SMD

def DynamicMinimumDegree(graph):
  DMD = []
  while graph.getSize() > 0:
    lowestDegree = graph.getLowestDegree()
    DMD.append(lowestDegree)
    graph.connectAll(graph.getNode(lowestDegree).getConnections())
    graph.removeNode(lowestDegree)
  return DMD