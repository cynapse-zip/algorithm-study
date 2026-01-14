import sys
input = sys.stdin.readline

N, game = input().split()
N = int(N)
games = {"Y":1, "F":2, "O":3}      # 임스 제외한 인원

players = set()
for _ in range(N):
    players.add(input().strip())

# 중복 제거된 사람 수 // 게임에 필요한 인원 수
ans = len(players) // games[game]
print(ans)
        