# 상한값에 대한 이분탐색
import sys

def solution():
    input = sys.stdin.readline

    N, M = map(int, input().split())

    names = []   # 칭호 이름
    limits = []  # 전투력 상한값

    prev_limit = -1
    for _ in range(N):
        title, limit = input().split()
        limit = int(limit)

        # 같은 상한값이면 처음 이름 유지
        if limit == prev_limit:
            continue

        prev_limit = limit
        names.append(title)
        limits.append(limit)

    result = []

    for _ in range(M):
        power = int(input())

        # 이분 탐색 시작
        left = 0
        right = len(limits) - 1

        # limits[mid] >= power 를 처음 만족하는 위치 찾기
        while left < right:
            mid = (left + right) // 2

            if limits[mid] >= power:
                # mid는 가능하니까 더 왼쪽에 답이 있을 수도 있음
                right = mid
            else:
                # mid는 불가능 → 오른쪽으로
                left = mid + 1

        # left가 최종 위치
        result.append(names[left])

    print("\n".join(result))

solution()
        