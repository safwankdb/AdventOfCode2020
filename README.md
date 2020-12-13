# Advent of Code 2020
Solutions for [Advent of Code](https://adventofcode.com/) 2020 in Python.

## Q1
Simple hash table.

## Q2
Use ```parse``` library for parsing string in specific format.

## Q6
Used ```set()``` is python for union and intersection.

## Q8
Parse instruction, simulate, maintain hash table to check for loops.

## Q10
Apply depth first search.
```
def dfs(u, t):
	if u == t:
		return 1
	if not u.npaths:
		u.npaths = sum(dfs(c, t) for c in u.children)
	return u.npaths
```

## Q12
Used [petyr](https://github.com/safwankdb/petyr) library for rotating the vectors.

## Q13
Notice that all numbers are prime, use Chinese Remaider Theorem. [CRT implementation](https://www.geeksforgeeks.org/using-chinese-remainder-theorem-combine-modular-equations/) from geeksforgeeks.
