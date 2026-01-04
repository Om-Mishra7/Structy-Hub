def max_palin_subsequence(string):
  return _max_palin_subsequence(string, {})

def _max_palin_subsequence(string, cache):
  if len(string) == 0:
    return 0
    
  if len(string) == 1:
    return 1

  if string in cache:
    return cache[string]

  if string[0] == string[-1]:
    cache[string] = 2 + _max_palin_subsequence(string[1:-1], cache)

  cache[string] = max(_max_palin_subsequence(string[1:], cache), _max_palin_subsequence(string[:-1], cache))

  return cache[string]