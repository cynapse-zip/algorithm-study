import sys
input = sys.stdin.readline

def solution():  
    N, new_score, P = map(int, input().split())
    
    # 랭킹이 비어있는 경우
    if N == 0:
        print(1)
        return

    scores = list(map(int, input().split()))
    
    # 내림차순 정렬
    scores.sort(reverse=True)

    # 랭킹이 꽉 찼고, 새 점수가 꼴등보다 작거나 같으면 탈락
    if N == P and new_score <= scores[-1]:
        print(-1)
        return
    
    # 등수 계산 (나보다 큰 점수 개수 + 1)
    rank = 1
    for score in scores:
        if score > new_score:
            rank += 1
        else:
            break
    
    print(rank)

solution()