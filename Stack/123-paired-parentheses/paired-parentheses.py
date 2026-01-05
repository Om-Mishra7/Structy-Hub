def paired_parentheses(string):
  stack = []
  for char in string:
    if char in ["(", ")"]:
      if stack:
        if stack[-1] != char:
          stack.pop()
        else:
          stack.append(char)
      else:
        stack.append(char)

  return len(stack) == 0
