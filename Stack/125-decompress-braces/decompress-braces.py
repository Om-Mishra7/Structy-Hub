def decompress_braces(string):
    stack = []
    result = ""

    for char in string:
        if char == "{":
            continue

        elif char == "}":
            count = int(stack[0])
            segment = ''.join(stack[1:])
            result += count * segment
            stack = []

        elif char.isdigit():
            stack.append(char)

        else:
            if stack and stack[0].isdigit():
                stack.append(char)
            else:
                result += char

    return result
