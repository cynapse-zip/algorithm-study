T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M):      # M번만큼 반복
        # deQueue
        first_num = arr.pop(0)
        # enQueue
        arr.append(first_num) 
 
    print(f'#{tc} {arr[0]}')