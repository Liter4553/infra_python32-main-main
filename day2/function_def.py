# 함수란 자주 사용하는 코드뭉치를 하나의 함수로 치환하여 사용하는것
# 긴 코드를 자주 사용하기에는 가독성이 떨어지니 간략화 해서 사용
#def로 함수를 지정하고 return으로 반환

def send_alert(server_name:str, status:int):
    """DocString: 함수 가이드 [서버 메세지 출력]"""
    result = ""
    result +=f"[경보] 대상 장비는 {server_name}"
    result +=f"[상태] 대상 장비는 {status}"
    result +="-"*20
    return result

send_alert("DB-01", "DB용량 초과")    