logined_id_list = [
    "wjdd1s",
    "leeyun0528-cyber",
    "d0hiru",
    "Bul1etBear",
    "Kimmyoungsung",
    "wjdd1s",
    "leeyun0528-cyber",
    "d0hiru",
    "Bul1etBear",
    "Kimmyoungsung",
    "wjdd1s",
    "Bul1etBear",
    "Kimmyoungsung",
    "wjdd1s",
    "leeyun0528-cyber",
    "d0hiru",
    "Bul1etBear",
]

#관리가 어려우니 세트로 생성
user_set1 = set(logined_id_list)

#세트는 내용의 변경은 불가능하지만 add()를 사용한 추가는 가능

#출력
print(user_set1)

user_set2 = {"1", "2", "3", "4", "5"}

print(user_set2)

print(user_set1.union(user_set2)) #union: 합집합
print(user_set1.difference(user_set2)) #difference: 차집합





burger_set = set() #비어있는 세트
burger_set.add("맘스터치")
print(type(burger_set))
print(burger_set)

