def solution(m, musicinfos):
    answer = []
    melodies = {}
    # 각 음악 별 악보 구하기 (재생 시간)
    for music in musicinfos:
        s, e, title, melody = music.split(',')
        melody = melody.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f')
        melody = melody.replace('G#', 'g').replace('A#', 'a')
        music_length = len(melody)
        s, e = list(map(int, s.split(':'))), list(map(int, e.split(':')))
        runtime = (e[0]-1-s[0]) * 60 + (60+e[1])-s[1]
        total_melody = runtime // music_length * melody + melody[:runtime % music_length+1]
        melodies[title] = [runtime, total_melody]
    # 기억하는 악보에 해당하는 음악 확인하기
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f')
    m = m.replace('G#', 'g').replace('A#', 'a')
    for t, info in melodies.items():
        runtime, melody = info
        if m in melody:
            answer.append([t, runtime, melody])
    answer = sorted(answer, key=lambda x: x[1], reverse=True)
    print(answer)
    return answer[0][0] if answer else "(None)"
