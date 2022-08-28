from collections import defaultdict
def solution(genres, plays):
    album = []
    genre_dict = defaultdict(int) 
    play_by_genre_dict = defaultdict(list)

    for i in range(len(genres)):
        genre_dict[genres[i]] += plays[i]
        play_by_genre_dict[genres[i]].append((i, plays[i]))

    genre_dict = dict(sorted(genre_dict.items(), key = lambda x: x[1], reverse = True))

    for g in genre_dict.keys():
        play_by_genre_dict[g] = sorted(play_by_genre_dict[g], key = lambda x: (-x[1], x[0]))
        album += [i for i, p in play_by_genre_dict[g][:2]]

    return album