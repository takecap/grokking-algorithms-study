graph = {}
graph['start'] = {'a': 6, 'b': 2}
graph['a'] = {'finish': 1}
graph['b'] = {'a': 3, 'finish': 5}
graph['finish'] = {}

infinity = float('inf')
consts = {'a': 6, 'b': 2, 'finish': infinity}
parents = {'a': 'start', 'b': 'start', 'finish': None}

def init_tables(graph):
  costs = {}
  parents = {}
  start_edges = graph['start']
  for node in graph.keys():
    if node == 'start':
      continue
    if node in start_edges:
      costs[node] = start_edges[node]
      parents[node] = 'start'
    else:
      costs[node] = infinity
      parents[node] = None
  return costs, parents

def findLowestCostNode(costs, processed):
  lowest_cost = infinity
  lowest_node = None
  for node in costs:
    cost = costs[node]
    if cost < lowest_cost and node not in processed:
      lowest_cost = cost
      lowest_node = node
  return lowest_node

def searchDijkstra(graph):
  costs, _ = init_tables(graph)
  return costs