import sys
input = sys.stdin.readline

N, X = map(int, input().split())
arr = list(map(int, input().split()))

cur_sum = sum(arr[:X])    # X일 동안 방문자 수의 합 (슬라이딩 윈도우)
max_sum = 0
cnt = 0    # 기간

# 첫 구간 처리
if cur_sum > max_sum:
    max_sum = cur_sum
    cnt = 1
elif cur_sum == max_sum:
    cnt += 1

for i in range(X, N):    # X일차일때부터 슬라이딩 시작
    cur_sum = cur_sum - arr[i - X] + arr[i]
    
    # 최댓값 갱신
    if cur_sum > max_sum:
        max_sum = cur_sum
        cnt = 1    # 최댓값을 새로 찾았을 경우 기간 리셋 필요
    elif cur_sum == max_sum:
        cnt += 1
        
if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(cnt)