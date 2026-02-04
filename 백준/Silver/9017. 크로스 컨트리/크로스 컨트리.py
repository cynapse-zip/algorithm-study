import sys
input = sys.stdin.readline

def solution():
    T = int(input().strip())
    for _ in range(T):
        N = int(input().strip())
        arr = list(map(int, input().split()))

        # 1) 팀별 인원수 세기
        cnt = [0] * 201  # 팀 번호 1~200
        for team in arr:
            cnt[team] += 1

        # 2) 자격 팀(정확히 6명)만 표시
        qualified = [False] * 201
        for team in range(1, 201):
            if cnt[team] == 6:
                qualified[team] = True

        # 3) 점수 부여 + 팀 점수 계산
        sum4 = [0] * 201
        fifth = [0] * 201
        got = [0] * 201  # 자격 팀 선수 몇 명 점수 받았는지(1~6)

        score = 1
        for team in arr:
            if not qualified[team]:
                continue

            got[team] += 1
            k = got[team]

            if k <= 4:
                sum4[team] += score
            elif k == 5:
                fifth[team] = score

            score += 1

        # 4) 우승 팀 선택: (sum4, fifth) 최소
        winner = -1
        best_sum = 10**18
        best_fifth = 10**18

        for team in range(1, 201):
            if qualified[team]:
                if (sum4[team] < best_sum) or (sum4[team] == best_sum and fifth[team] < best_fifth):
                    best_sum = sum4[team]
                    best_fifth = fifth[team]
                    winner = team

        print(winner)

solution()
