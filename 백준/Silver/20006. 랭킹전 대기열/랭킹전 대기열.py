import sys
input = sys.stdin.readline

def solution():
    p, m = map(int, input().split())

    rooms = []    # 방 관리 (기준 레벨 base, 플레이어 정보 players)
    
    for _ in range(p):
        level, name = input().split()
        level = int(level)
        
        matched = False    # 해당 플레이어의 매칭 여부 관리
        # 방이 있는 경우, 들어갈 방 찾기
        for room in rooms:
            # 1) 정원이 다 차지 않은 경우
            if len(room["players"]) < m:
                base = room["base"]
                
                # 2) 입장 가능 레벨 체크
                if base - 10 <= level <= base + 10:
                    room["players"].append((level, name))
                    matched = True
                    break     # 방에 들어갔으니 멈추고 다음 사람으로 넘어가기
        
        # 방이 없는 경우 - 새 방 생성하고 입장시킴
        if not matched:
            rooms.append({"base": level, "players": [(level, name)]})
        
    # 출력 모아서 관리
    answer = []
    for room in rooms:
        if len(room["players"]) == m:
            answer.append("Started!")
        else:
            answer.append("Waiting!")
            
        # 닉네임 사전순
        for level, name in sorted(room["players"], key=lambda x: x[1]):
            answer.append(f"{level} {name}")
    print("\n".join(answer))
solution()
        