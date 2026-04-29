inventory = [
    { "name" : "WEB1", "risk": 95 },
    { "name" : "DB2", "risk": 40 },
    { "name" : "DB3", "risk": 50 },
    { "name" : "WEB2", "risk": 10 },
    { "name" : "WEB3", "risk": 75 },
    { "name" : "DB4", "risk": 83 },
]

def filter_high_risk(server_list):
    """딕셔너리를 요소로 하는 리스트를 받아, risk가 높은(80초과) 서버의 name을 리스트로 반환"""
    
    # 리스트 컴프리헨션 수정: dict["risk"] 값이 80보다 큰 경우의 dict["name"]을 수집
    result = [server["name"] for server in server_list if server["risk"] > 80]
    
    # 필터링된 결과 리스트를 직접 반환
    return result

# 함수 호출 및 결과 출력
high_risk_servers = filter_high_risk(inventory)
print(high_risk_servers)