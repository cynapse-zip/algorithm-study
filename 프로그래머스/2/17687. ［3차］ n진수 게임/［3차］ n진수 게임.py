# N진법 : n으로 계속 나눈 나머지를 뒤에서부터 읽는다
def num_convert(num, n):
    digits = '0123456789ABCDEF'     # 문제에 주어진 가장 큰 16진법 기준
    if num == 0:
        return "0"
    
    converted = []
    while num > 0:
        converted.append(digits[num % n])
        num //= n
    
    return ''.join(reversed(converted)) # 거꾸로 뒤집고 하나의 문자열로 반환
        
    
def solution(n, t, m, p):
    num = 0     # 숫자는 0부터 시작
    cur = ''    # 현재까지 모든 사람이 말한 문자 저장
    
    # t*m개를 말할때까지 숫자 변환 (참여한 사람들이 말할 모든 글자수)
    while len(cur) < t * m:
        cur += num_convert(num, n)
        num += 1
    
    # cur에서 튜브가 말할 글자만 추출
    answer = ''
    for i in range(t):
        answer += cur[(p-1) + i * m]    # 인덱스 기준이므로 p-1, m칸마다 점프
        
    return answer