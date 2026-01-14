def solution(topping):
    
    # 투포인터 + dict
    # 1) dict로 동생의 토핑 갯수 관리하기
    brother = {}
    for i in range(len(topping)):
        key = topping[i]
        brother[key] = brother.get(key, 0) + 1  # key값이 없으면 0
        
    # 2) 컷 이동
    cheolsu = set()
    answer = 0
    for i in range(len(topping)-1):     # 맨 끝은 제외하고 컷 이동
        topp = topping[i]
        
        # 왼쪽에 있는 철수 몫에 추가
        cheolsu.add(topp)
        # 남은 토핑에서 빼주기
        brother[topp] -= 1
        if brother[topp] == 0:    # 토핑 수가 0이면 dict에서 제거
            del brother[topp]
        
        # 철수와 동생의 토핑 갯수 비교
        if len(cheolsu) == len(brother):
            answer += 1
        
    return answer