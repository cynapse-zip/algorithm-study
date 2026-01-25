# 완전탐색 DFS
def dfs(idx, discount, users, emoticons, answer):
    percents = [10, 20, 30, 40]
    m = len(emoticons)
    
    if idx == m:
        service = 0
        sales = 0
        
        for min_rate, limit_price in users:
            total = 0
            for j in range(m):
                # user가 정한 할인율보다 높을 경우에만 구매한다
                if discount[j] >= min_rate:
                    total += emoticons[j] * (100 - discount[j]) // 100
            
            # 전체 가격이 구매한도를 벗어나면 서비스 가입
            if total >= limit_price:
                service += 1
            # 구매한도 내에서는 매출액에 더함
            else:
                sales += total
                
        # answer = [max_service, max_sales] 최댓값 갱신
        # 1. 서비스 가입자 최대
        # 2. 가입자 수 같을 경우, 판매액 최대
        if (service > answer[0]) or (service == answer[0] and sales > answer[1]):                
            answer[0] = service
            answer[1] = sales        
        return
    
    # 각 case마다 할인율 붙여보고 -> 다음 idx로 넘어갔다가 -> 돌아옴 (백트래킹)
    for p in percents:
        discount.append(p)
        dfs(idx + 1, discount, users, emoticons, answer)
        discount.pop()


def solution(users, emoticons):

    answer = [-1, -1]
    dfs(0, [],users, emoticons, answer)
    
    return answer