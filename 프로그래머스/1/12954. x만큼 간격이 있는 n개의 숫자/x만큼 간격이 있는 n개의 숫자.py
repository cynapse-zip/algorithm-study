def solution(x, n):
    answer = []
    for num in range(1, n+1):
        answer.append(x * num)
    return answer