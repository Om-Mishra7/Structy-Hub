def count_compounds(compound, elements):
  return _can_concat(compound, elements, {})

def _can_concat(s, words, cache):
  if s in cache:
    return cache[s]

  if len(s) == 0:
    return 1

  is_possible = 0

  for word in words:
    if s[:len(word)] == word.lower():
      is_possible += is_possible + _can_concat(s[len(word):], words, cache)

  cache[s] = is_possible

  return cache[s]
