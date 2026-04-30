#여러 개의 인자 *args / 출력 횟수 = 기본값1
# xxxx("최인규", "박건우", "전은지")
# xxxx("최인규", "박건우", "전은지")
# xxxx("최인규", "박건우", "전은지")



def print_numbers(*args, count = 1):    #항상 매개 변수는 앞에 적기 (불필요한 동작을 사전에 막기 위함)
    for _ in range(count):  #필요하지 않은 함수는 언더바_로 처리
        print(*args)

print_numbers(3, 3, 3, count = 3)