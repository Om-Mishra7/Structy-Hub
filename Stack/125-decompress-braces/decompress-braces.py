def decompress_braces(s):
  stack = []

  for char in s:
    if char not in ["{", "}"]:
      stack.append(char)
    elif char == "}":
      sub_stack = []
      while True:
        last_element = stack.pop()
        sub_stack.append(last_element)

        if last_element.isdigit():
          break

      stack.append(int(sub_stack[-1]) * "".join(sub_stack[-2:-1:-1]))

      print(stack)

  return "".join(stack)