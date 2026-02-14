def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        i = 0       # skill에서 다음에 배워야 할 스킬 위치
        ok = True   # 스킬트리 가능 여부
        
        for char in skill_tree:
            if char not in skill:   # skill에 없는 스킬이면 pass
                continue
                
            # 이미 다 배웠거나, 기다리는 스킬이 아닐 경우
            if i == len(skill) or char != skill[i]:
                ok = False
                break
                
            # 포인팅 중인 스킬 == 현재 가리키는 스킬
            i += 1
                
        if ok:
            answer += 1
            
    return answer