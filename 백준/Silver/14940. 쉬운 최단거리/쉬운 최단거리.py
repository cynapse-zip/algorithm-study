import sys
from collections import deque

input = sys.stdin.readline

# 최단거리 -> BFS
def solution ():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    
    # 거리 메모
    dist = [[-1] * m for _ in range(n)]
    q = deque()
    
    # 1. 시작점 찾기
    sx = sy = -1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                sx, sy = i, j
                break
        if sx != -1:
            break

    dist[sx][sy] = 0
    q.append((sx, sy))

     # 2. BFS
    dirs = [(1,0), (0,1), (-1,0), (0,-1)]
    while q:    
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] != 0 and dist[nx][ny] == -1:     # 이동가능하고 방문한 적 없는 경우
                    dist[nx][ny] = dist[x][y] + 1               # 이동하기
                    q.append((nx, ny))

    # 출력 규칙
    answer = []
    for i in range(n):
        row = []
        for j in range(m):
            if grid[i][j] == 0:
                row.append("0")
            else:
                row.append(str(dist[i][j]))
        answer.append(" ".join(row))
    print("\n".join(answer))
    
    
solution()