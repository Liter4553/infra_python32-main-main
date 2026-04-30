people = [
    {"name": "Alice", "age": 25, "city": "Seoul"},
    {"name": "Bob", "age": 30, "city": "Busan"},
    {"name": "Charlie", "age": 28, "city": "Incheon"},
    {"name": "David", "age": 35, "city": "Daegu"},
    {"name": "Eve", "age": 22, "city": "Daejeon"},
    {"name": "Frank", "age": 40, "city": "Gwangju"},
    {"name": "Grace", "age": 27, "city": "Suwon"},
    {"name": "Hannah", "age": 33, "city": "Ulsan"},
    {"name": "Ian", "age": 29, "city": "Jeju"},
    {"name": "Jane", "age": 31, "city": "Sejong"}
]
#나이순 정렬
print(sorted(people, key= lambda person: ['age'], reverse=True))

#filter나 map의 결과는 바로 출력하면 이상한 객체 주소 값만 나옴
#반드시 list()로 감싸서 내용물을 확인
#람다에서 쓰는 변수 이름도 문맥에 맞게 지어주면 좋지만, 짧은 코드에서만 사용하기 때문에 관습적으로 x를 많이 씀

