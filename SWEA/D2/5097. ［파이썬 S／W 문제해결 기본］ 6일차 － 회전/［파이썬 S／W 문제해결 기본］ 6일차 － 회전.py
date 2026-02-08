# queue 없이 풀기 : 나머지 개념이랑 같음
T = int(input().strip())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f"#{tc} {arr[M % N]}")