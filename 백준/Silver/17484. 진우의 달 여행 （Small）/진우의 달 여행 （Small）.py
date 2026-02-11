import sys
import heapq
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    INF = float('inf')    # 임의의 큰 수
    dist = [[[INF] * 3 for _ in range(M)] for _ in range(N)]    # 최소 연료 기록

    # 방향 설정
    dy = [-1, 0, 1]
    
    # 우선순위 큐 (현재까지 연료, x, y, 이전 방향)
    pq = []
    
    # 첫 행은 어떤 방향으로든 시작 가능
    for y in range(M):
        for dir in range(3):
            dist[0][y][dir] = grid[0][y]
            heapq.heappush(pq, (grid[0][y], 0, y, dir))
    
    # 다익스트라
    while pq:
        cost, x, y, prev_dir = heapq.heappop(pq)

        # 이미 더 작은 비용으로 방문한 상태라면 스킵
        if cost > dist[x][y][prev_dir]:
            continue

        # 마지막 행이면 더 내려갈 필요 없음
        if x == N - 1:
            continue

        # 3가지 방향 탐색
        for dir in range(3):

            # 같은 방향 연속 사용 불가
            if dir == prev_dir:
                continue

            nx = x + 1
            ny = y + dy[dir]

            # 범위 체크
            if 0 <= nx < N and 0 <= ny < M:
                new_cost = cost + grid[nx][ny]

                # 더 작은 비용이면 갱신
                if new_cost < dist[nx][ny][dir]:
                    dist[nx][ny][dir] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny, dir))

    answer = float('inf')

    for y in range(M):
        for d in range(3):
            answer = min(answer, dist[N-1][y][d])
    print(answer)
        
solution()