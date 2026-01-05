## nesting score

Write a function, *nesting\_score*, that takes in a string of brackets as an argument. The function
should return the score of the string according to the following rules:

- [] is worth 1 point
- XY is worth X + Y points where X, Y are substrings of well-formed brackets
- [S] is worth S * 2 points where S is a substring of well-formed brackets

For example: 

[[][][]] is equivalent to (1 + 1 + 1) * 2 = 6

You may assume that the input only contains well-formed square brackets.

#### test_00:

```python
nesting_score("[]") # -> 1
```

#### test_01:

```python
nesting_score("[][][]") # -> 3
```

#### test_02:

```python
nesting_score("[[]]") # -> 2
```

#### test_03:

```python
nesting_score("[[][]]") # -> 4
```

#### test_04:

```python
nesting_score("[[][][]]") # -> 6
```

#### test_05:

```python
nesting_score("[[][]][]") # -> 5
```

#### test_06:

```python
nesting_score("[][[][]][[]]") # -> 7
```

#### test_07:

```python
nesting_score("[[[[[[[][]]]]]]][]") # -> 129
```

#### test_08:

```python
nesting_score("") # -> 0
```