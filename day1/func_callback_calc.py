#계산기

#더하기 함수, 빼기 함수, 곱하기 함수, 나누기 함수

def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    
    if b == 0:
        print("0으로는 나눌 수 없습니다.")
        return None
    return a / b


def calculator():
    input_a = int(input("숫자를 입력하세요"))
    input_b = int(input("숫자를 입력하세요"))
    input_action = input("행동 입력 (더하기, 빼기, 곱하기, 나누기): ")
    if input_action == "더하기":
        real_action = sum
    elif input_action == "빼기":
        real_action = sub
    elif input_action == "곱하기":
        real_action = mul
    elif input_action == "나누기":
        real_action = div
    else:
        real_action =None

    return [input_a, input_b, real_action]


def real_calc(input_a, input_b, real_action):
    return real_action(input_a, input_b)
    

# 구조 분해 할당 (리스트의 요소 3개를 각각 a, b, c에 담음)
[a, b, c] = calculator()

# 결과 출력
print(f"결과: {real_calc(a, b, c)}")