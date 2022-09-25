def solution(dirs):
    answer = 0
    x,y = 0,0
    visited = []
    opposite_dir_dict = {'L':'R', 'R':'L', 'U':'D', 'D':'U'}
    directions_dict = {'L':[-1,0], 'R':[1,0], 'U':[0,1], 'D':[0,-1]}
    for d in dirs:
        nx = x + directions_dict[d][0]
        ny = y + directions_dict[d][1]
        if -5<=nx<=5 and -5<=ny<=5:
            x, y = nx, ny
            if (d, nx, ny) not in visited or (opposite_dir_dict[d], x, y) not in visited:
                visited.append((d,nx,ny))
                visited.append((opposite_dir_dict[d], x, y))
                answer += 1
    return answer