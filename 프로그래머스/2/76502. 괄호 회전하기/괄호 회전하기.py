# 짝이 맞는지 확인하는 함수
def is_valid(brackets):
    stack = []

    for br in brackets:
        # 여는 괄호면 스택에 넣기
        if br == '(' or br == '[' or br == '{':
            stack.append(br)

        # 닫는 괄호면
        else:
            # 스택이 비어 있으면 실패
            if len(stack) == 0:
                return False

            top = stack[-1]

            # 짝이 안 맞으면 실패
            if br == ')' and top != '(':
                return False
            if br == ']' and top != '[':
                return False
            if br == '}' and top != '{':
                return False

            # 짝이 맞으면 pop
            stack.pop()

    # 끝났을 때 스택이 비어 있어야 성공
    if len(stack) == 0:
        return True
    else:
        return False


def solution(s):
    n = len(s)

    # 길이가 홀수면 절대 불가능
    if n % 2 == 1:
        return 0

    answer = 0

    for x in range(n):
        rotated = ""

        # x번부터 끝
        for i in range(x, n):
            rotated += s[i]
            
        # 앞 x글자를 잘라서 뒤에 붙이기
        for i in range(0, x):
            rotated += s[i]

        # 올바르다면?
        if is_valid(rotated):
            answer += 1

    return answer