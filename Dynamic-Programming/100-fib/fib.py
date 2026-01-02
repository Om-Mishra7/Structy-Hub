def fib(n):

  cache = {}

  return find_fib(n, cache)

def find_fib(n, cache):
  if n == 0:
    return 0
  if n == 1:
    return 1
    
  if n in cache:
    return cache[n]

  value = find_fib(n-1, cache) + find_fib(n-2, cache)

  cache[n] = value

  return value
