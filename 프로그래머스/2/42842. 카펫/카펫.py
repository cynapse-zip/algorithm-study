def solution(brown, yellow):    
    # brown + yellow의 가장 차이가 적은 두 수의 곱
    # 이라고 생각했으나.. 반례 존재
    total = brown + yellow
    
    # 약수 쌍 찾기 (제곱근까지만 확인)
    for h in range(1, int(total**0.5) + 1):
        if total % h != 0:
            continue
        w = total // h
        if w < h:
            continue
            
        # brown과 w, h 차이가 2씩 나는지 확인
        if (w - 2) * (h - 2) == yellow:
            return [w, h]