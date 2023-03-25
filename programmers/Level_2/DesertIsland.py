from collections import deque
def solution(maps):
    maps = [list(m) for m in maps]
    answer = []
    def bfs(s:tuple)->int:
        q = deque([s])
        days = int(maps[s[0]][s[1]])
        maps[s[0]][s[1]] = 'V'
        while q:
            x,y = q.popleft()
            for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x+i, y+j
                if 0<=nx<len(maps) and 0<=ny<len(maps[0]):
                    if maps[nx][ny].isdigit():
                        days += int(maps[nx][ny])
                        maps[nx][ny] = 'V'
                        q.append((nx, ny))
        return days
                    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j].isdigit():
                tmp = bfs((i,j))
                answer.append(tmp)
    return [-1] if not answer else sorted(answer)

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))