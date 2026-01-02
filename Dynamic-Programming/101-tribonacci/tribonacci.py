def tribonacci(n):
  cache = {}

  return _tribonacci(n, cache)

def _tribonacci(n, cache):
  if n == 0 or n == 1:
    return 0

  if n == 2:
    return 1

  if n in cache:
    return cache[n]

  value = _tribonacci(n-1) + _tribonacci(n-2) + _tribonacci(n-3)

  cache[n] = value

  return value