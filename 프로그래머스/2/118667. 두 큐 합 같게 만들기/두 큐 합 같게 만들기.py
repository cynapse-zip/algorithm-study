from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)

    sum1 = sum(q1)
    sum2 = sum(q2)
    total = sum1 + sum2

    # 전체 합이 홀수면 불가능
    if total % 2 == 1:
        return -1

    target = total // 2

    # 어떤 원소가 target보다 크면 불가능
    # (그 원소가 포함된 큐는 합이 target이 될 수 없음)
    if max(max(q1), max(q2)) > target:
        return -1

    n = len(q1)
    limit = 4 * n  # 무한루프 방지용 상한
    cnt = 0

    while cnt <= limit:
        if sum1 == target:
            return cnt

        if sum1 > target:
            x = q1.popleft()
            q2.append(x)
            sum1 -= x
            sum2 += x
        else:
            x = q2.popleft()
            q1.append(x)
            sum2 -= x
            sum1 += x

        cnt += 1
        
    # 어떤 방법으로도 각 큐의 원소 합을 같게 만들 수 없는 경우
    return -1