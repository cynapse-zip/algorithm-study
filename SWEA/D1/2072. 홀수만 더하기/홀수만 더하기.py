T = int(input())
for tc in range(1, T+1):
    ans = 0
    nums = list(map(int, input().split()))
    for num in nums:
        if num % 2 != 0:
            ans += num
            
    print(f'#{tc} {ans}')