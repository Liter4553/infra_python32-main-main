beverage_dict = {
    1 : {"name" : "콜라", "price": 500},
    2 : {"name" : "사이다", "price": 600},
    3 : {"name" : "환타", "price": 700},
    4 : {"name" : "밀키스", "price": 800},
    5 : {"name" : "포카리스웨트", "price": 900},
}

money = 0

# def 로 분할
def show_menu():
    print("="*60)
    for k, v in beverage_dict.items():
        print(f"{k} : {v["name"]}")
    print("="*60)

def get_money(money):
    input_money = int(input("금액을 넣으세요"))
    return money + input_money
    #만약 input_money에 숫자가 아니면 예외처리

def input_beverage():
    beverage_num = int(input("마시고 싶은 음료를 선택하세요! 종료는 0번"))
    # 입력 예외 처리
    if not beverage_num:
       
    elif beverage_num < 1 or beverage_num > 5:
        pass
    return beverage_dict[beverage_num]

    beverage_name = beverage_dict[beverage_num]["name"]
    beverage_price = beverage_dict[beverage_num]["price"]
    print(f"내가 선택한 음료 {beverage_name} {beverage_price}")
    # print(f"덜컹! {beverage_name}이/가 나왔습니다.")

def give_change(beverage_price):
    change = money - beverage_price
    #잔돈이 0원이면 잔돈 줄 필요 없음
    #잔돈이 -면 음료를 주면 안됨
    #잔돈이 +면 잔돈 줘야됨
    print(f"땡그랑! 잔돈 {change}원 입니다.")

    def serve_bevarage(beverage):
        print(f"덜컹! {beverage['name']}이/가 나왔습니다.")
        if money >= beverage["price"]:
            print(f"{beverage}")
        else:
            print("금액이 부족합니다")
        return money
while True:
    money = get_money(money)
    print(f"입금 금액: {money}원")
    
    #단순 메뉴 출력
    show_menu()
    #음료 입력 받기
    while True:
        try:
            
            selected_beverage = input_beverage()
            break
        except Exception as e:
            print(e)
            continue

    #음료 제공
    print(f"덜컹! {selected_beverage['name']}이/가 나왔습니다.")

    #잔돈 계산
    give_change(selected_beverage["price"]) 
