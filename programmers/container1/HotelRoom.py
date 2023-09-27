import sys
sys.setrecursionlimit(10000)

def find_room(check, rooms):
    if check not in rooms:
        rooms[check] = check+1
        return check
    empty = find_room(rooms[check], rooms)
    rooms[check] = empty + 1
    return empty

def solution(k, room_number):
    rooms = dict()
    for num in room_number:
        find_room(num, rooms)
    return list(rooms)