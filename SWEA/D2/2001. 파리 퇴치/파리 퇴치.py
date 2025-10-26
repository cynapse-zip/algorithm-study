T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0  # 최댓값

    for i in range(N - M + 1):  # 시작점 board[i][j]
        for j in range(N - M + 1): 
            sum_v = 0
            for k in range(M):  # MxM 크기의 영역을 탐색
                for l in range(M):
                    sum_v += board[i + k][j + l]  # 부분합 계산

            if max_v < sum_v:
                max_v = sum_v

    print(f'#{tc} {max_v}')