def nesting_score(string):
  return _nesting_score(list(string))

def _nesting_score(s):
    if not s:
        return 0

    balance = 0
    for i, char in enumerate(s):
        if char == "[":
            balance += 1
        else: 
            balance -= 1

        if balance == 0:
            left = s[:i + 1]
            rest = s[i + 1:]

            if left == "[]":
                return 1 + _nesting_score(rest)

            inner = left[1:-1]
            return 2 * _nesting_score(inner) + _nesting_score(rest)
