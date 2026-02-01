import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    
    # 단어 입력 & 빈도 카운트
    words_cnt = {}
    for _ in range(N):
        word = input().strip()
        if len(word) < M:
            continue
        else:
            words_cnt[word] = words_cnt.get(word, 0) + 1    # 단어가 없으면 0을 넣고, 있으면 +1
            
    # 정렬 (빈도, 길이, 알파벳)
    words = list(words_cnt.keys())    # 단어들만 가져오기
    # 빈도 내림차순, 길이 내림차순, 단어 오름차순
    words.sort(key=lambda w: (-words_cnt[w], -len(w), w))    
    
    # 출력
    for word in words:
        print(word)
    
solution()