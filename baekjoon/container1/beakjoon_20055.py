import sys
from collections import deque


def BeltRotate(belt, robot):
    b = deque(belt)
    r = deque(robot)
    b.rotate(1)
    r.rotate(1)
    if r[-1] == 1:
        r[-1] = 0
    return b, r


def RobotShift(belt, robot):
    n = len(robot)
    for i in range(n-2, -1, -1):
        if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] >= 1:
            robot[i+1] += 1
            robot[i] -= 1
            belt[i+1] -= 1
    if robot[-1] == 1:
        robot[-1] = 0
    return belt, robot


def RobotAdd(belt, robot):
    if belt[0] >= 1:
        belt[0] -= 1
        robot[0] += 1
    return belt, robot


def BeltCheck(K, belt):
    if belt.count(0) >= K:
        return False
    return True


N, K = map(int, sys.stdin.readline().rstrip().split())
belt = list(map(int, sys.stdin.readline().rstrip().split()))
robot = [0 for i in range(N)]
step = 0

while True:
    step += 1
    belt, robot = BeltRotate(belt, robot)
    belt, robot = RobotShift(belt, robot)
    belt, robot = RobotAdd(belt, robot)
    if BeltCheck(K, belt) is False: break

print(step)