#기본 정보 설정 (튜플) = 추가, 수정, 변경, 삭제 아예 안됨!!! 
db_config = ("127.0.0.1", "admin", 1234)

#수정 시도
#db_config[0] = "192.0.8.15"  에러남

#출력
print(db_config[0])

#요소가 하나 뿐인 튜플에는 콤마,를 찍어서 표시
single_tuple = (1,)
single_tuple[0] = "홍인규"


