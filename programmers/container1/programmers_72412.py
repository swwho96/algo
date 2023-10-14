from bisect import bisect_left
def solution(info, query):
    answer = []
    
    info_dict = {}
    for i in info:
        string = ' '.join(i.split()[:-1])
        score = int(i.split()[-1])
        if string not in info_dict:
            info_dict[string] = [score]
        else:
            info_dict[string].append(score)
    for i in info_dict: info_dict[i].sort()
    l, o, t, s = [], [], [], []
    for q in query:
        cnt = 0
        tmp = q.replace('and','').split()
        l = ['cpp', 'java', 'python'] if tmp[0] == '-' else [tmp[0]]
        o = ['backend','frontend'] if tmp[1] == '-' else [tmp[1]]
        t = ['junior', 'senior'] if tmp[2] == '-' else [tmp[2]]
        s = ['chicken', 'pizza'] if tmp[3] == '-' else [tmp[3]]
        for L in l:
            for O in o:
                for T in t:
                    for S in s:
                        if ' '.join([L,O,T,S]) in info_dict:
                            N = len(info_dict[' '.join([L,O,T,S])])
                            idx = bisect_left(info_dict[' '.join([L,O,T,S])], int(tmp[-1]))
                            cnt += N-idx
        answer.append(cnt)
    return answer