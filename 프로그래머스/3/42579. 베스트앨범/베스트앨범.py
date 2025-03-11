from collections import defaultdict
def solution(genres, plays):
    n = len(genres)
    songs = defaultdict(list)
    answer = []
    for i in range(n):
        songs[genres[i]].append((i, plays[i]))
    songs = list(songs.values())
    songs.sort(reverse = True, key = lambda x: sum([p[1] for p in x]))
    for song in songs:
        song.sort(reverse = True, key = lambda x: (x[1], -x[0]))
        
    answer = [i[0] for song in songs for i in song[:2]]
    

    return answer