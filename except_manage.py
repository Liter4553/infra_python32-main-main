try:
    # 사용자로부터 숫자를 입력받아 정수로 변환
    number = int(input("숫자를 입력하세요"))
    
    # 100을 입력받은 숫자로 나눔
    result = 100 / number
    print(result)

except ZeroDivisionError:
    # 사용자가 0을 입력했을 때 발생하는 에러 처리
    print("0은 쓰지마... 제발ㅠㅠ 그건 나눌 수 없어")

except Exception as e:
    # 그 외 모든 예외 상황(예: 문자 입력 등) 발생 시 처리
    print(f"사고다 사고 사고 내용은 {e}")

# 예외 처리 후 정상적으로 실행되는 다음 코드
print("또 다른 중요작업을 시작합니다.")

#   try:
#       실행할 코드
#   except:
#       특정 예외에 실행할 코드
#   finally:
#       무조건 실행할 코드


#else 없이 try 안에 다 넣으면 안됨
#예외를 최소화 해서 어디서 에러가 발생하는지 쉽게 파악하기 위해
#위험한 코드와 안전한 코드를 명확히 분리하는 데에 의의가 있다.