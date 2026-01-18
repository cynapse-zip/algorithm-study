def solution(msg):
    answer = []
    
    # 1) ord 함수 : 문자 -> 숫자로 변환
    dic = {}
    for i in range(26):
        dic[chr(ord('A') + i)] = i + 1 
    next_idx = 27

    i = 0       # msg 인덱스 관리
    n = len(msg)

    # 2) LZW 압축 시뮬레이션
    while i < n:
        j = i + 1       # 포인터 잡기

        # 사전에 있는 가장 긴 문자열 w 찾기 (i에서 시작)
        while j <= n and msg[i:j] in dic:
            j += 1

        # j가 한 칸 더 나아간 상태이므로, w는 i에서 (j-1)까지
        w = msg[i:j-1]
        answer.append(dic[w])

        # 다음 글자가 남아있다면 w+c를 사전에 추가 (i~j가 w+c)
        if j <= n:
            dic[msg[i:j]] = next_idx
            next_idx += 1

        # w 길이만큼 이동
        i += len(w)

    return answer