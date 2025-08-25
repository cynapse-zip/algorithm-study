def solution(n, lost, reserve):

    # 정렬
    lost = sorted(lost)
    reserve = sorted(reserve)
    
    # 여벌 체육복을 가져온 학생이 체육복을 도난당했을 경우 빌려줄 수 없다
    both = []
    for i in lost:
        if i in reserve:
            both.append(i)

    for i in both:
        lost.remove(i)
        reserve.remove(i)

    # 빌려주기
    for r in reserve:
        if r - 1 in lost:
            lost.remove(r - 1)
        elif r + 1 in lost:
            lost.remove(r + 1)

    answer = (n - len(lost))
    return answer