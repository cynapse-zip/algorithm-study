from collections import deque

def solution(board):
    n, m = len(board), len(board[0])    # 세로, 가로 길이
    
    # 1. 시작점, 도착점 찾기
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                sx, sy = i, j
            elif board[i][j] == 'G':
                gx, gy = i, j
                
    # 2. BFS
    q = deque()             # 방문 순서 관리
    q.append((sx, sy,0))    # 좌표, 이동횟수
    visited = [[0] * m for _ in range(n)]
    visited[sx][sy] = 1     # 시작점 방문체크
    
    # 4방향 (우 하 좌 상)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    while q:                        # 방문할 곳이 존재할 동안
        x, y, dist = q.popleft()    # 가까운 곳부터 이동한다
        
        # 4방향 탐색
        for dir in range(4):
            cx, cy = x, y           # 현재 좌표 기록

            nx, ny = cx + dx[dir], cy + dy[dir]   # 이동할 방향 정함
            # 범위 제한 (board 범위 안이면서 D가 아닌 경우 이동 가능) - 유효하다면 이동
            while 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 'D':
                cx, cy = nx, ny
                nx += dx[dir]
                ny += dy[dir]

            # 움직임이 없었다면
            if (cx, cy) == (x, y):
                continue

            # 목표를 찾았다면
            if board[cx][cy] == 'G':
                return dist + 1

            # 방문 체크
            if visited[cx][cy] == 0:
                visited[cx][cy] = 1
                q.append((cx, cy, dist+1))
                
    # 도달 불가
    return -1
