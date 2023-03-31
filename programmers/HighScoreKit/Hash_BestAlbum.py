'''
장르별 2곡씩 모아 앨범 제작 (고유 번호 저장)
1. 장르별 많이 재생된 순서
2. 장르 내에서 많이 재생된 곡 순서
3. 같은 재생 횟수인 경우 고유번호 낮은 순서
'''

def solution(genres, plays):
    album = []
    cnt_by_song_dict = {}
    cnt_by_genre_dict = {}
    for i, g in enumerate(genres):
        # 장르별 재생횟수
        if g in cnt_by_genre_dict:
            cnt_by_genre_dict[g] += plays[i]
        else:
            cnt_by_genre_dict[g] = plays[i]
        # 장르 내 곡별 재생횟수
        if g in cnt_by_song_dict:
            cnt_by_song_dict[g].append((plays[i], i))
        else:
            cnt_by_song_dict[g] = [(plays[i], i)]
    # 장르 정렬
    cnt_by_genre_dict = dict(sorted(cnt_by_genre_dict.items(), key=lambda x: x[1], reverse=True))
    for genre in cnt_by_genre_dict.keys():
        cnt_by_song_dict[genre] = sorted(cnt_by_song_dict[genre], key=lambda x: (-x[0], x[1]))
        album += [i for p, i in cnt_by_song_dict[genre][:2]]
    return album