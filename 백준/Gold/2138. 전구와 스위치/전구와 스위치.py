import sys
input = sys.stdin.readline

def press(arr, i):
    n = len(arr)    # n개의 배열
    # i번 스위치를 누르면 i-1, i, i+1 전구 상태 토글
    for j in (i - 1, i, i + 1):
        if 0 <= j < n:
            if arr[j] == '0':    # 0인 경우
                arr[j] = '1'
            else: arr[j] = '0'

def toggle(cur, tgt, first_pressed):
    arr = cur[:]  # 복사
    cnt = 0

    # 첫 스위치 누른 경우 가정
    if first_pressed:
        press(arr, 0)
        cnt += 1
        
    # 첫 스위치 안 누른 경우 가정
    for i in range(1, len(arr)):
        if arr[i-1] != tgt[i-1]:    # 스위치를 누를 수 있는 마지막 기회일때, 스위치 상태가 다르다면 토글해야 함.
            press(arr, i)
            cnt += 1

    if arr == tgt:
        return cnt
    else:
        return float('inf')    # 숫자끼리 비교해야하므로 임시의 큰수로 리턴

N = int(input().strip())
cur = list(input().strip())
tgt = list(input().strip())

min_cnt = min(toggle(cur, tgt, False), toggle(cur, tgt, True))

if min_cnt == float('inf'):
    print(-1)
else:
    print(min_cnt)
