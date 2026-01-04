def semesters_required(num_courses, prereqs):
  adj_list = {}
  cache = {}
  min_semesters = 1
  
  for prereqs, course in prereqs:
    if prereqs not in adj_list:
      adj_list[prereqs] = [course]
    else:
      adj_list[prereqs].append(course)

  for node in adj_list:
    min_semesters = max(min_semesters, _semesters_required(node, adj_list, cache))

  return min_semesters


def _semesters_required(node, adj_list, cache):
  if node not in adj_list:
    return 1

  if node in cache:
    return cache[node]

  min_semesters = 0
  for neighbour_node in adj_list[node]:
    min_semesters = max(min_semesters, 1 + _semesters_required(neighbour_node, adj_list, cache))

  cache[node] = min_semesters

  return cache[node]
  