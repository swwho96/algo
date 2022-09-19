from collections import defaultdict

def ParkingTime(time_list:list)->int:
    parking_time = 0
    if len(time_list) % 2 != 0:
        time_list.append('23:59')
    for i in range(1,len(time_list),2):
        IN = list(map(int, time_list[i-1].split(':')))
        OUT = list(map(int, time_list[i].split(':')))
        if OUT[1] < IN[1]:
            OUT[0], OUT[1] = OUT[0]-1, OUT[1]+60
        parking_time += (OUT[0]-IN[0])*60 + OUT[1]-IN[1]
    return parking_time

def HowMuchFee(fees, parking_time):
    fee = fees[1]
    if parking_time > fees[0]:
        if (parking_time - fees[0]) / fees[2] != int((parking_time - fees[0]) / fees[2]):
            fee += (int((parking_time - fees[0]) / fees[2]) + 1) * fees[3]
        else:
            fee += (int((parking_time - fees[0]) / fees[2])) * fees[3]
    return fee
    

def solution(fees, records):
    answer = {}
    InOutByCar = defaultdict(list)
    # 자동차별 입차/출차 확인
    for info in records:
        information = info.split()
        InOutByCar[information[1]].append(information[0])
    # 자동차별 요금 확인
    for k,v in InOutByCar.items():
        parking_time = ParkingTime(v)
        answer[k] = HowMuchFee(fees, parking_time)
    return [fee[1] for fee in sorted(answer.items())] 