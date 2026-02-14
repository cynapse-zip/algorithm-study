def solution(numbers):
    n = len(numbers)
    answer = [-1] * n   # 탐색할때마다 답을 덮어씌운다
    
    max_num = -1
    # 순서가 있으니 스택 활용
    stack = []
    
    for i in range(n):
        # stack에 숫자가 있고, 가장 최근에 뒷큰수를 못 찾은 숫자부터 확인, 그 숫자가 지금 값보다 작으면 해결
        while stack and numbers[stack[-1]] < numbers[i]:
            idx = stack.pop()
            answer[idx] = numbers[i]

        stack.append(i)

    return answer