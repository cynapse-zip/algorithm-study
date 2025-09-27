import math     # 시간 입력받기 위함

def solution(fees, records):
    
    base_time, base_fee, unit_time, unit_fee = fees # 기본요금 / 단위요금 입력 받기
    in_time = {}    # 차량번호 : key, 입차 시간: value
    total_time = {}     # 누적 주차 시간
    
    # 시 -> 분으로 전환하는 함수
    def time_convert(t):
        h, m = map(int, t.split(":"))   # :기준으로 잘라서 시, 분 저장
        return h*60 + m
    
    for record in records:
        time, car, IO = record.split()
        time = time_convert(time)       # 시 -> 분으로 변환
        
        if IO == "IN":
            in_time[car] = time     # key(차량번호)로 입차시간 가져옴
        else:   # 출차 시간 계산 (OUT일 경우)
            charged = time - in_time[car]   # 주차한 시간의 길이
            if car in total_time:       # 여러번 입/출차 한 경우 합산해야 함.
                total_time[car] += charged
            else:
                total_time[car] = charged
            del in_time[car]    # 계산 완료했으면 입차 시간지움
            
    # 자동 출차 처리
    auto_out = time_convert("23:59")    
    for car, time in in_time.items():
        charged = auto_out - time
        if car in total_time:
            total_time[car] += charged
        else:
            total_time[car] = charged
    
    # 기본요금 초과 여부 판단
    answer = [] # 차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return
    for car in sorted(total_time.keys()):
        parked = total_time[car]    # 차량 번호 별 주차 시간
        if parked <= base_time:
            fee = base_fee
        else:
            over_parked = parked - base_time
            fee = base_fee + math.ceil(over_parked / unit_time) * unit_fee
        answer.append(fee)
    
    return answer