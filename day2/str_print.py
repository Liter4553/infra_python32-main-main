name = "최인규"
mbti = "ISTP"
blood_type = "A"

# 안녕하세요. 최인규입니다. 제 MBTI는 ISTP이고요. 혈액형은 A형입니다.
print("안녕하세요. " + name + "입니다. 제 MBTI는 " + mbti + "이고요, 혈액형은 " + blood_type + "형입니다.")
print("안녕하세요. %s입니다. 제 MBTI는 %s이고요, 혈액형은 %s형입니다." % (name, mbti, blood_type))
print("안녕하세요. {}입니다. 제 MBTI는 {}이고요, 혈액형은 {}형입니다.".format(name, mbti, blood_type))
print("안녕하세요. {2}입니다. 제 MBTI는 {1}이고요, 혈액형은 {0}형입니다.".format(blood_type, mbti, name))

# 진짜 최신방식
print(f"안녕하세요. {name[:-2] + "**"}입니다. 제 MBTI는 {mbti}이고요, 혈액형은 {blood_type}형입니다.")