def solution(n):
    N = 1234567
    
    if n == 1:
        return 1
    if n == 2:
        return 2

    now, next = 1, 2
    
    # 한칸 갈 때 -> 한가지 방법, 두칸 갈 때 -> 두가지 방법
    # 3칸 가기 위해서 -> 1 + 1 + 1 / 1 + 2 / 2 + 1 (세가지 방법)
    # 4칸 가기 위해서 -> 다섯가지 방법
    # 다음 칸의 경우의 수는 (이전 칸) + (그 이전 칸)
    for _ in range(3, n + 1):
        answer = (now + next) % N  # 다음 칸 값
        now = next                   # 한 칸 밀기
        next = answer                # next도 갱신

    return next