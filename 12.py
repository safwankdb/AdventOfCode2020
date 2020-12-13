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

## Part 2

pos = np.array([0.0, 0.0])
waypoint = np.array([10.0, 1.0])
for command in data:
    dirn = command[0]
    mag = int(command[1:].strip())
    if dirn == "N":
        waypoint += [0, mag]
    elif dirn == "S":
        waypoint -= [0, mag]
    elif dirn == "E":
        waypoint += [mag, 0]
    elif dirn == "W":
        waypoint -= [mag, 0]
    elif dirn == "F":
        pos += waypoint * mag
    elif dirn == "R":
        x = waypoint
        x = Affine().rotate(-mag) * x[None, :]
        waypoint = x[0]
    elif dirn == "L":
        x = waypoint
        x = Affine().rotate(mag) * x[None, :]
        waypoint = x[0]
print(round(abs(pos[0]) + abs(pos[1])))
