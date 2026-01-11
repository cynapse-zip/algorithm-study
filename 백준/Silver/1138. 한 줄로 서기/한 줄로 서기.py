import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    ppl = list(map(int, input().split()))

    line = [0] * N  # 0 = 빈 칸

    # 키 작은 사람부터
    for h in range(1, N + 1):
        cnt = ppl[h - 1]      # 왼쪽에 있어야 하는 키 큰 사람 수
        for i in range(N):
            if line[i] == 0:  # 빈 칸
                if cnt == 0:
                    line[i] = h    # 해당 칸에 배치
                    break
                cnt -= 1

    print(*line)

solve()
