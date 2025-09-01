def solution(sizes):
    
    max_height = 0
    max_width = 0
    
    for size in sizes:
        # 정렬
        size = sorted(size)
        
        # 앞 / 뒤 각각 가장 큰 숫자 찾기        
        if size[0] > max_height:
            max_height = size[0]
        
        if size[1] > max_width:
            max_width = size[1]
            
    answer = max_height * max_width
    
    return answer