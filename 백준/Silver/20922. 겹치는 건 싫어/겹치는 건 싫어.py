import sys
input = sys.stdin.readline

def solution():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = [0] * 100001
    l = 0
    ans = 0

    for r in range(N):
        x = arr[r]
        cnt[x] += 1

        # K개보다 많아지면, l 이동
        while cnt[x] > K:
            cnt[arr[l]] -= 1
            l += 1

        ans = max(ans, r - l + 1)

    print(ans)

solution()
