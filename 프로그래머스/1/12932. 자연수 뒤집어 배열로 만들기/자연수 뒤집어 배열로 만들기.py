def solution(n):
    answer = []
    
    for char in list(str(n)):
        answer.append(int(char))
    
    return answer[::-1]