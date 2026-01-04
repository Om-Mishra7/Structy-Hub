def can_concat(s, words):
    print(f"\nStarting can_concat with string: '{s}'")
    return _can_concat(s, words, {})

def _can_concat(s, words, cache):
    print(f"\nChecking substring: '{s}'")

    if s in cache:
        print(f"  Cache hit for '{s}' → {cache[s]}")
        return cache[s]

    if len(s) == 0:
        print("  Reached empty string → True")
        return True

    is_possible = False

    for word in words:
        print(f"  Trying word '{word}' with '{s}'")

        if s.startswith(word):
            print(f"    Match found. Recursing on '{s[len(word):]}'")
            is_possible = is_possible or _can_concat(s[len(word):], words, cache)

            if is_possible:
                print(f"    ✔ Possible using '{word}' → stopping further checks")
                break
        else:
            print(f"    No match")

    cache[s] = is_possible
    print(f"  Caching result for '{s}' → {is_possible}")

    return is_possi_
