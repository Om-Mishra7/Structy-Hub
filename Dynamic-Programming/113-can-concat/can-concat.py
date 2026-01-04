def can_concat(s, words):
  return _can_concat(s, words, {})

def _can_concat(s, words, cache):
  if s in cache:
    return cache[s]

  if len(s) == 0:
    return True

  is_possible = False

  for word in words:
    if s[:len(word)] == word:
      is_possible = is_possible or _can_concat(s[len(word)], words, cache)

  cache[s] = is_possible

  return cache[s]
