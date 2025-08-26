import math

def solution(progresses, speeds):
    N = len(progresses)
    
    # (100 - progress) // speeds => days
    days = []
    for i in range(N):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    # 각 배포별 기능의 갯수
    answer = []
    i = 0       # 기준 인덱스 시작점
    
    while i < N:       # 인덱스 범위 벗어나지 않도록
        j = i + 1      # 비교할 인덱스 시작점
        feat = 1
        
        while j < N and days[i] >= days[j]:    # 더 큰 숫자를 만나기 전까지
            feat += 1       # 배포할 기능이 한개 늘어나고
            j += 1          # 다음 비교로 넘어감
            
        answer.append(feat) # while문 종료 후 (더 큰 숫자를 만나면 비교 중지)
        i = j       # 멈춘 지점에서부터 다시 비교 시작
    
    return answer