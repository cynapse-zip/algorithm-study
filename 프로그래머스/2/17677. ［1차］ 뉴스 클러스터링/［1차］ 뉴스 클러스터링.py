def solution(str1, str2):
    # 대소문자 일치시키기
    str1 = str1.lower()
    str2 = str2.lower()
    
    # 두 글자씩 잘라서 집합으로 만든다
    str1_lst = []
    str2_lst = []
    
    for i in range(len(str1) - 1):
        pair = str1[i] + str1[i+1]
        # 문자열 조합만 추가한다.
        if pair.isalpha():
            str1_lst.append(pair)

    for i in range(len(str2) - 1):
        pair = str2[i] + str2[i+1]
        if pair.isalpha():
            str2_lst.append(pair)

    # 중복제거 없이 합집합 & 교집합으로 접근
    # 1) 교집합의 수 구하기
    intersection = 0
    str2_copy = str2_lst.copy()     # 비교를 위해 복사하여 사용
    
    for pair in str1_lst:           # str1에서 특정 문자쌍이
        if pair in str2_copy:       # 만약 str2에 존재한다면
            intersection += 1       # 교집합
            str2_copy.remove(pair)  # 교집합 처리한 문자쌍은 제거하여 중복카운트 방지
            
    # 2) 합집합의 수 구하기
    union = len(str1_lst) + len(str2_lst) - intersection
    
    # 3) 집합 A와 집합 B가 모두 공집합일 경우 1로 정의
    if union == 0:
        answer = 1
    else:
        answer = intersection/union
    
    # 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력
    return int(answer * 65536)