def hello_names(count = 1, *names):
    # 전달받은 이름들(names 튜플)을 하나씩 꺼내서 반복
    for name in names:
        # "Hello"를 count 횟수만큼 반복해서 출력
        print("Hello" * count, name)

# [실행 예시]
# 1. 첫 번째 인자 2는 count에, 나머지는 names에 할당됩니다.
hello_names(2, '손흥민', '이강인', '황희찬')

# [주석 처리된 코드들 (주의사항)]
# hello_names('손흥민', '이강인', '황희찬', 2) 
# -> '손흥민'이 count에 할당되어 문자열 곱셈 에러 발생 가능

# hello_names(count = 2, '손흥민', '이강인', '황희찬')
# -> 가변 인자 앞에 키워드 인자를 쓰면 문법 에러(SyntaxError) 발생

# hello_names('손흥민', '이강인', '황희찬', count = 2)
# -> 위치상 '손흥민'이 이미 count를 차지하여 중복 할당 에러 발생 가능

# hello_names('손흥민', '이강인', '황희찬')
# -> '손흥민'이 count에 들어가고 '이강인', '황희찬'만 인사하게 됨