import numpy as np

values = {".": 0, "L": -1, "#": 1}
with open("11.in") as f:
    x = np.array([[values[i] for i in line[:-1]] for line in f.readlines()])

grid = np.zeros((2 + len(x), 2 + len(x[0])))
grid[1:-1, 1:-1] = x

while True:
    new = grid.copy()
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if grid[i, j] == 0:
                continue
            neighbours = (grid[i - 1 : i + 2, j - 1 : j + 2] > 0).sum() - (
                grid[i, j] > 0
            )
            if grid[i, j] == -1 and neighbours == 0:
                new[i, j] = 1
            elif neighbours > 3:
                new[i, j] = -1
    if np.all(new == grid):
        break
    grid = new

print(np.sum(grid == 1))


grid = np.zeros((2 + len(x), 2 + len(x[0])))
grid[1:-1, 1:-1] = x
r, c = grid.shape

while True:
    new = grid.copy()
    for i in range(1, r - 1):
        for j in range(1, c - 1):
            if grid[i, j] == 0:
                continue
            neighbours = 0
            a, b = i - 1, j - 1
            while a > 0 and b > 0:
                if grid[a, b] == 1:
                    neighbours += 1
                    break
                if grid[a, b] == -1:
                    break
                a -= 1
                b -= 1
            a, b = i - 1, j + 1
            while a > 0 and b < c - 1:
                if grid[a, b] == 1:
                    neighbours += 1
                    break
                if grid[a, b] == -1:
                    break
                a -= 1
                b += 1
            a, b = i + 1, j + 1
            while a < r - 1 and b < c - 1:
                if grid[a, b] == 1:
                    neighbours += 1
                    break
                if grid[a, b] == -1:
                    break
                a += 1
                b += 1
            a, b = i + 1, j - 1
            while a < r - 1 and b > 0:
                if grid[a, b] == 1:
                    neighbours += 1
                    break
                if grid[a, b] == -1:
                    break
                a += 1
                b -= 1
            a, b = i - 1, j
            while a > 0:
                if grid[a, b] == 1:
                    neighbours += 1
                    break
                if grid[a, b] == -1:
                    break
                a -= 1
            a, b = i + 1, j
            while a < r - 1:
                if grid[a, b] == 1:
                    neighbours += 1
                    break
                if grid[a, b] == -1:
                    break
                a += 1
            a, b = i, j - 1
            while b > 0:
                if grid[a, b] == 1:
                    neighbours += 1
                    break
                if grid[a, b] == -1:
                    break
                b -= 1
            a, b = i, j + 1
            while b < c - 1:
                if grid[a, b] == 1:
                    neighbours += 1
                    break
                if grid[a, b] == -1:
                    break
                b += 1
            if grid[i, j] == 1 and neighbours > 4:
                new[i, j] = -1
            elif grid[i, j] == -1:
                if neighbours == 0:
                    new[i, j] = 1
    if np.all(new == grid):
        break
    grid = new

print(np.sum(grid == 1))
