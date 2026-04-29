#number = int(input("숫자를 입력하세요: \t"))
#if number > 50:
#    print("입력한 숫자는 50보다  크군요.")
#elif number == 50:
#    print("입력한 숫자는 50이군요.")


kor_score = int(input("국어점수를 입력하세요."))
eng_score = int(input("영어점수를 입력하세요."))
math_score = int(input("수학점수를 입력하세요."))

score_list = [kor_score, eng_score, math_score]
average = sum(score_list) / len(score_list)

#만약에 평균 90점 이상이면 A, 80점 이상이면 B, 70점 이상이면 C, 60점 이상이면 D, 나머지는 F
if average >= 90:
    print("A")
elif average >= 80:
    print("B")
elif average >= 70:
    print("C")
elif average >= 60:
    print("D")
else :
    print("F") 