def quickest_concat(s, words):
  return _quickest_concat(s, words, {})

def _quickest_concat(s, words, cache):


  if s in cache:
    return cache[s]

  if len(s) == 0:
    return 0

  quickest_concat = float("inf")

  for word in words:
    if s[:len(word)] == word:
      result = _quickest_concat(s[len(word):], words, cache)
      if result != -1:
        quickest_concat = min(quickest_concat, 1 + result)

  if quickest_concat == float("inf"):
    cache[s] = -1
    return -1

  cache[s] = quickest_concat
  return quickest_concat
