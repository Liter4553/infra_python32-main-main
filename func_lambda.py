#cpu_log = [75, 55, 96, 51, 41]
#
#warning_cpu = list(filter(lambda value: value >= 80, cpu_log))
#print(warning_cpu)
#
#lambda : 따로 정의하지 않는 간단한 익명 함수(내장함수)
#간단하게 사용할때만 사용하는 일회용 함수이므로, 코드가 복잡할땐 정석적인 방법으로 함수를 선언해야함 (def)





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

include_e = list(filter(lambda person: "e" in person["name"].lower(), people))
print(include_e)
