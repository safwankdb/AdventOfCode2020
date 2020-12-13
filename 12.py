from petyr import Affine
import numpy as np

with open("12.in") as f:
    data = f.readlines()

theta = 0
pos = np.array([0.0, 0.0])


def length(x):
    return np.sqrt(x[0] ** 2 + x[1] ** 2)


def forward(pos, theta, x):
    x = x * np.array([1, 0])
    x = Affine().rotate(theta) * x[None, :]
    pos += x[0]
    return pos, theta


def right(pos, theta, x):
    theta -= x
    return pos, theta


def left(pos, theta, x):
    theta += x
    return pos, theta


def north(pos, theta, x):
    pos += [0, x]
    return pos, theta


def south(pos, theta, x):
    pos += [0, -x]
    return pos, theta


def east(pos, theta, x):
    pos += [x, 0]
    return pos, theta


def west(pos, theta, x):
    pos += [-x, 0]
    return pos, theta


transform = {
    "F": forward,
    "R": right,
    "L": left,
    "N": north,
    "S": south,
    "E": east,
    "W": west,
}
for command in data:
    dirn = command[0]
    mag = int(command[1:].strip())
    pos, theta = transform[dirn](pos, theta, mag)
print(round(abs(pos[0]) + abs(pos[1])))
