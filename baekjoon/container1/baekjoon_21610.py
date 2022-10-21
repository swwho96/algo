import sys

def MoveCloud(N, cloud_area, direction, distance):
    direction_command = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
    visited = [[False for _ in range(N)] for _ in range(N)]
    for c in cloud_area:
        c[0] = (c[0] + distance * direction_command[direction-1][0]) % N
        c[1] = (c[1] + distance * direction_command[direction-1][1]) % N
        visited[c[0]][c[1]] = True
    return cloud_area, visited


def Rainning(cloud_area, maps):
    for c in cloud_area:
        maps[c[0]][c[1]] += 1
    return maps


def WaterCopy(N, cloud_area, maps):
    check_list = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
    for c in cloud_area:
        bucket_cnt = 0
        for check in check_list:
            nx = c[0] + check[0]
            ny = c[1] + check[1]
            if 0 <= nx < N and 0 <= ny < N and maps[nx][ny] >= 1:
                bucket_cnt += 1
        maps[c[0]][c[1]] += bucket_cnt
    return maps


def NewCloudArea(maps, cloud_area, visited):
    new_cloud_area = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] >= 2 and visited[i][j] is False:
                maps[i][j] -= 2
                new_cloud_area.append([i, j])
    return new_cloud_area


N, M = map(int, sys.stdin.readline().rstrip().split())
maps = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
command_list = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]
cloud = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
total_water_cnt = 0

for command in command_list:
    cloud_area, visited = MoveCloud(N, cloud, command[0], command[1])
    new_maps = Rainning(cloud_area, maps)
    new_maps = WaterCopy(N, cloud_area, new_maps)
    cloud = NewCloudArea(new_maps, cloud_area, visited)

for i in range(N):
    total_water_cnt += sum(maps[i])

print(total_water_cnt)