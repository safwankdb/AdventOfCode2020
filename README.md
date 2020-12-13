# Advent of Code

## Q1
SImple hash table.

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

## Q13
Notice that all numbers are prime, se Chinese Remaider Theorem. [CRT implementation](https://www.geeksforgeeks.org/using-chinese-remainder-theorem-combine-modular-equations/) from geeksforgeeks.
