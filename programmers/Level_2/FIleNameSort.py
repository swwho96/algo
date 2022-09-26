def HeadNumberTail(file:str)->list:
    HNT_list = []
    left, right = 0, 1
    while True:
        if len(HNT_list) >= 2 or right > len(file)-1:
            HNT_list.append(file[left:])
            break
        if file[left].isdigit(): # NUMBER
            if file[right] == ' ' or (file[right].isdigit() and (right-left+1) <= 5):
                right += 1
            else:
                HNT_list.append(file[left:right])
                left = right
                right = left + 1
        else: # HEAD
            if file[right] == ' ' or not file[right].isdigit():
                right += 1
            else:
                HNT_list.append(file[left:right])
                left = right
                right = left + 1
    return HNT_list

def solution(files):
    answer = []
    file_list = []
    # file name to H.N.T
    for file in files:
        file_list.append(HeadNumberTail(file))
    # sorting
    file_list = sorted(file_list, key=lambda x: (x[0].lower(), int(x[1].replace(' ', ''))))
    return [''.join(f) for f in file_list]