## valid compound

You are a chemist and have to figure out if you can make a compound from some given elements!

Write a function, _valid\_compound_, that takes in a target compound and a list of elements. The function should return a boolean
indicating whether or not the compound can be created from the given elements.

A compound is made by concatenating one or more elements together.

You may reuse elements of the list as many times as needed to make a compound.

#### test_00:

```python
valid_compound("neco", [
  "Ne",
  "O",
  "Be",
  "I",
  "N",
  "Os",
  "Si",
  "S",
  "Co",
  "C",
  "Ir",
]) # -> True
```

#### test_01:

```python
valid_compound("nerco", [
  "Ne",
  "O",
  "Be",
  "I",
  "N",
  "Os",
  "Si",
  "S",
  "Co",
  "C",
  "Ir",
]) # -> False
```

#### test_02:

```python
valid_compound("sir", [
  "Ne",
  "O",
  "Be",
  "I",
  "N",
  "Os",
  "Si",
  "S",
  "Co",
  "C",
  "Ir",
]) # -> True
```

#### test_03:

```python
valid_compound("noses", [
  "Ne",
  "O",
  "Be",
  "I",
  "N",
  "Os",
  "Si",
  "S",
  "Co",
  "C",
  "Ir",
]) # -> False
```

#### test_04:

```python
valid_compound("onbeinos", [
  "Ne",
  "O",
  "Be",
  "I",
  "N",
  "Os",
  "Si",
  "S",
  "Co",
  "C",
  "Ir",
]) # -> True
```

#### test_05:

```python
valid_compound("cocococococococococococococococococococococococococococococox", [
  "Ne",
  "O",
  "Be",
  "I",
  "N",
  "Os",
  "Si",
  "S",
  "Co",
  "C",
  "Ir",
]) # -> False
```
