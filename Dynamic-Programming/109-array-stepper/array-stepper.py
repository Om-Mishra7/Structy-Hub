def array_stepper(numbers):
  return _array_stepper(numbers, 0, {})

def _array_stepper(numbers, position, cache):
  if position in cache:
    return cache[position]

  if position > len(numbers) - 1:
    return False

  route_exists = False
  
  for i in range(1, numbers[position]+ 1):
    route_exists = route_exists or _array_stepper(numbers, position + i, cache)

  cache[position] = route_exists

  return route_exists
    
  

