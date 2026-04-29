fam_list = [ "박민호", "최인규", "정진성", "박보검", "수지", "카리나", "장원영", "츄", "영케이"]

favorite= {
    "food" : [{
        "name": "빵",
        "bestThing" : ["식빵", "카스테라", "버터떡"]
    }, "과자", "고기", "술"],
    "activity" : ["여행", "낮잠", "노래"],
    "animal" : ["고양이"]
}

db_config = ("127.0.0.1", "admin", 1234)
user_set = {"Bul1etBear", "Kimmyoungsung", "dumpling0531", "Lyxx-cloud", "yeon506"}

print("최인규" in fam_list) #true
print(1234 in db_config) #true
print("최인규" in user_set) #false
print("food" in favorite.keys()) #true
activity_list = favorite.get("activity", []) #favorite리스트 안에서 activity 리스트를 빼와서 새로운 리스트로 만듦
print("여행" in activity_list) #true
#not in 으로 바꾸면 false와 true가 바뀜


#컬렉션 타입 : max(), min() 최댓값, 최솟값 반환(숫자면 크기 비교, 문자면 알파벳 순서 비교)
#컬렉션 타입 : sum()
#컬렉션 타입 : sorted() 정렬된 타입 반환 (원본 데이터를 훼손하지 않기 위함)
#컬렉션 타입 : 

# 세트 생성 {11,2,33,3,3,3,3}