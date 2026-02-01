def parse(filename):
    # 인덱스를 저장해서 슬라이싱
    i = 0
    n = len(filename)
    
    # HEAD
    while i < n and not filename[i].isdigit():
        i += 1
    head = filename[:i]
    
    # NUMBER
    j = i       # 문자가 끊기는 시점부터 인덱스 카운트 시작
    while j < n and filename[j].isdigit() and j - i < 5:
        j += 1
    number = filename[i:j]

    return head, number


def solution(files):
    parsed = []
    
    for file in files:
        head, number = parse(file)
        
        # 정렬
        key = (head.lower(), int(number))
        parsed.append((key, file))      # 기준과 결과물을 함께 묶어서 관리
        
    parsed.sort(key=lambda x: x[0])
    return [file for key, file in parsed]