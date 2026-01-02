def count_paths(grid):
  return _count_paths(grid, (0,0), {})


def _count_paths(grid, current_node, cache):
  if current_node == (len(grid)-1, len(grid[0]) - 1):
    return 1

  if current_node in cache:
    return cache[current_node]

  possible_ways = 0

  if current_node[0] < len(grid) - 1 and grid[current_node[0]+1][current_node[1]] != "X":
    possible_ways += _count_paths(grid, (current_node[0]+1, current_node[1]), cache)

  if current_node[1] < len(grid[0]) - 1 and grid[current_node[0][current_node[1]+1] != "X":
    possible_ways += _count_paths(grid, (current_node[0],current_node[1]+ 1), cache)

  cache[current_node] = possible_ways

  return possible_ways                                       
