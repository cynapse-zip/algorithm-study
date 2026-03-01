# 최대공약수 (유클리드 호제법)
# 숫자의 크기에 상관없이, 계속 나눈다. (자동 크기 정렬)
def gcd(w, h):
    while h:
        w, h = h, w % h
    return w


def solution(w,h):
    # 사용 가능 = 전체 - 대각선이 지나가는 칸 수
    answer = w * h - (w + h - gcd(w, h))
    return answer