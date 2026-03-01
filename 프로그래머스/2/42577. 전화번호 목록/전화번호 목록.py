def solution(phone_book):
    # 길이 순으로 정렬
    phone_book.sort()
    
    # startwswith 함수 활용하여 인접한 번호끼리 확인
    for i in range(len(phone_book)-1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True