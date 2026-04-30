kor_score = int(input("국어점수를 입력하세요."))
eng_score = int(input("영어점수를 입력하세요."))
math_score = int(input("수학점수를 입력하세요."))

average = (kor_score + eng_score + math_score) / 3
print(f"당신의 합계 점수는 {average:.2f}입니다.")