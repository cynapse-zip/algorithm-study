import sys
input = sys.stdin.readline

def solution():
    N, K = map(int, input().split())
    lst = list(input().strip())
    
    eaten = 0    # 햄버거 먹은 사람
    
    for i in range(N):
        if lst[i] == 'P':
            for j in range(max(0, i-K), min(N-1, i+K)+1):    # 인덱스 범위제한 !!!
                if lst[j] == 'H':
                    lst[j] = 'X'    # 바로 먹기
                    eaten += 1
                    break   
    print(eaten)
solution()