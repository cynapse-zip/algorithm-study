def solution(n):
    answer = 0

    while n > 0:
        left = n % 10       # 나머지 연산자 활용
        answer += left
        n = (n - left) // 10

    return answer