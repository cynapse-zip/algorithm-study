import sys
from collections import deque

input = sys.stdin.readline

def solution():
    n, m, v = map(int, input().split())
    adj = [[] for _ in range(n+1)]    # 인접 리스트
    
    # 간선 정보 입력
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
        
    # 방문할 수 있는 정점이 여러 개인 경우, 번호가 작은 것부터 (정렬)
    for i in range(1, n+1):
        adj[i].sort()
    
    # =================================================================
    # DFS
    visited = [-1] * (n+1)
    dfs_order = []    # 방문 순서 저장
    
    def dfs(x):
        # (1) 현재 정점 방문 처리
        visited[x] = 1
        dfs_order.append(x)
        
        # (2) 인접한 정점 중, 아직 방문하지 않은 정점으로 이동
        for nx in adj[x]:
            if visited[nx] == -1:
                dfs(nx)    # 재귀 : 계속해서 탐색
                
    dfs(v)    # 호출
    
    # =================================================================
    # BFS
    visited = [-1] * (n+1)
    bfs_order = []
    q = deque()
    
    # (1) 시작점 큐에 삽입
    q.append(v)
    visited[v] = 1    # 방문처리
    
    # (2) 큐가 빌 때까지 반복
    while q:
        x = q.popleft()    # 가장 먼저 들어온 정점 꺼냄
        bfs_order.append(x)
        
        # (3) 현재 정점과 인접한 정점 확인
        for nx in adj[x]:
            if visited[nx] == -1:    # 방문한 적 없다면, 방문처리
                visited[nx] = 1
                q.append(nx)         # 다음 지점 탐색을 위해 큐에 추가
                
    # =================================================================
    # 결과 출력
    print(*dfs_order)
    print(*bfs_order)

solution()