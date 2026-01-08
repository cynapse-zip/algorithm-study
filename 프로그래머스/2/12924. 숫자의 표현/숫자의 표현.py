def solution(n):
    answer = 0
    
    # 연속한 자연수들의 합 -> 투 포인터
    # 시작점 = [1]
    left, right = 1, 1
    cur_sum = 1
    
    # 시작 숫자가 n보다 크지 않은 경우,
    while left <= n:
        # 현재까지의 합 == 주어진 수
        if cur_sum == n:
            answer += 1
            # 다음 경우 찾기
            cur_sum -= left
            left += 1            
        
        # 현재까지의 합이 주어진 수보다 작은 경우,
        # 오른쪽 큰 수를 더해줘야 함
        elif cur_sum < n:
            right += 1
            cur_sum += right
    
        # 현재까지의 합이 주어진 수보다 큰 경우,
        # 왼쪽의 작은 수 부터 뺀다
        else: 
            cur_sum -= left
            left += 1
    
    return answer