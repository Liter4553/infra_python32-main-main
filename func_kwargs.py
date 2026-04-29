def update_config(server_name, **kwargs):
    print(f"[{server_name}] 설정 변경 내역")
    # kwargs는 {'os': 'Linux', 'port': '22', ...} 형태의 딕셔너리가 됩니다.
    for k, v in kwargs.items():
        print(f"{k} ---- {v}")

# 수정된 호출 방식: 첫 번째 인자는 server_name에, 나머지는 kwargs로 들어갑니다.
update_config("내 소중한 서버", os="Linux", port="22", status="Running", pw="1234")



#lambda : 따로 정의하지 않는 간단한 익명 함수
#간단하게 사용할때만 사용하는 일회용 함수이므로, 코드가 복잡할땐 정석적인 방법으로 함수를 선언해야함 (def)

