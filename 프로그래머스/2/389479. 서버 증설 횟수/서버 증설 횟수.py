def solution(players, m, k):
    answer = 0
    active = 0                  # 현재 운영 중인 증설 서버 수
    added = [0] * 24            # 각 시간에 몇 대 증설했는지 기록

    for i in range(24):
        # k시간이 지난 서버 반납
        if i - k >= 0:
            active -= added[i - k]

        # 현재 시간에 필요한 증설 서버 수
        need = players[i] // m

        # 부족하면 그만큼만 추가 증설
        if active < need:
            new_server = need - active
            added[i] = new_server
            active += new_server
            answer += new_server

    return answer