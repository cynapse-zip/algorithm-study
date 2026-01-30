def dectobin(num):
    if num == 0:    # 마지막 나머지가 0일 경우
        return '0'
    
    bin = ''
    while num > 0:
        bin += str(num % 2)
        num //= 2

    return bin[::-1]


def solution(n):
    # 다음 큰 숫자가 되려면? '01' -> '10'
    # 단, '01'이 없는 경우는 맨 앞에 '0' 붙여서 처리
    bin_num = list('0' + dectobin(n))
    
    for i in range(len(bin_num)-1, 0, -1):  # 뒤에서부터 탐색
        if bin_num[i-1] == '0' and bin_num[i] == '1':
            bin_num[i-1], bin_num[i] = '1', '0'
            
            # 오른쪽 부분 전부 재정렬 (1의 갯수 맞추고 오른쪽으로 다 밀어서 작은 수로 만들기)
            right = bin_num[i+1:]
            cnt_one = right.count('1')          # 1의 갯수
            cnt_zero = len(right) - cnt_one     # 0의 갯수
            bin_num[i+1:] = ['0'] * cnt_zero + ['1'] * cnt_one
            
            break
        
    answer = int(''.join(bin_num), 2)       # int("문자열", 진법)
    
    return answer