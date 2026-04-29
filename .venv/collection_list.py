#서버리스트
server_list = ["WEB-01", "DB-01", "APP-01"]

print(server_list[0])

print(server_list[1])

print(server_list[2])

print(server_list[2] == server_list[-1])

print(server_list[0])

print(server_list[0])
print(server_list[-1])

#요소 하나 추가 - 데이터 타입 상관 없음
server_list.append("APP-01")
server_list.append("APP-01")
server_list.append("APP-01")
server_list.append("APP-01")
server_list.append("APP-01")
server_list.remove("APP-01")

server_list.insert(1000, "첫번재 서버 넣기")

print(server_list)



print(f"현재 관리 중인 서버는 총 {len(server_list)}대 입니다.")