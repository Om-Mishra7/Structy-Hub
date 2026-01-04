def longest_path(graph):
  cache = {}
  longest_path = 0
  
  for node in graph:
    longest_path = max(longest_path, _longest_path(node, graph, cache))

  return longest_path

def _longest_path(node, graph, cache):
  if len(graph[node]) == 0:
    cache[node] = 0

  if node in cache:
    return cache[node]

  longest_path = 0

  for neighbour_node in graph[node]:
    longest_path =  max(longest_path, 1 + _longest_path(neighbour_node, graph, cache))

  return cache[node]
    
    