## count compounds

You are a chemist and have to figure out how many ways you can make a given compound.

Write a function, _count\_compounds_, that takes in a target compound and a list of elements. The function should return the number
of ways we can make the compound with the given elements.

A compound is made by concatenating one or more elements together.

You may reuse elements of the list as many times as needed to make a compound.

#### test_00:

```python
count_compounds("neco", [
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
]) # -> 2
```

#### test_01:

```python
count_compounds("nerco", [
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
]) # -> 0
```

#### test_02:

```python
count_compounds("sir", [
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
]) # -> 1
```

#### test_03:

```python
count_compounds("hocli", [
  "C",
  "Cl",
  "I",
  "Ho",
  "Li",
  "La",
  "H",
  "O"
]) # -> 4
```

#### test_04:

```python
count_compounds("noses", [
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
]) # -> 0
```


#### test_05:

```python
count_compounds("onbeinos", [
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
]) # -> 2
```

#### test_06:

```python
count_compounds("necoonbeinos", [
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
]) # -> 4
```

#### test_07:

```python
count_compounds("cocococococococococococococococococococococococococococococox", [
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
]) # -> 0
```
