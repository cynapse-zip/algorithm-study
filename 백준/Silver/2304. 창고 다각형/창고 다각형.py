import sys
input = sys.stdin.readline

N = int(input())
pillars = []

for _ in range(N):
    L, H = map(int, input().split())
    pillars.append((L, H))

pillars.sort()

# 최고 기둥 찾기
max_height = 0
max_idx = 0

for i in range(N):
    if pillars[i][1] > max_height:
        max_height = pillars[i][1]
        max_idx = i

area = 0

# 왼쪽 -> 최고
cur = pillars[0][1]
for i in range(max_idx):
    cur = max(cur, pillars[i][1])
    width = pillars[i+1][0] - pillars[i][0]
    area += cur * width

# 오른쪽 -> 최고
cur = pillars[N-1][1]
for i in range(N-1, max_idx, -1):
    cur = max(cur, pillars[i][1])
    width = pillars[i][0] - pillars[i-1][0]
    area += cur * width

# 최고 기둥
area += max_height

print(area)