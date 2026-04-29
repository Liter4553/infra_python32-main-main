server_info = {
    "hostname":"WEB-SVR-01",
    "port": "80",
    "status": "Running",
    "ip_addr": "127.0.0.1",
    "os": "Ubuntu",
    "user_list": ["apple", "bear", "cat"]
}

print(server_info)

#print(server_info["hostname"])
#print(server_info["port"])
#print(server_info["status"])
#print(server_info["ip_addr"])
#print(server_info["os"])
#print(server_info["user_list"])


print(server_info.get("hostname"))
print(server_info.get("port"))
print(server_info.get("status"))
print(server_info.get("ip_addr"))
print(server_info.get("os"))
print(server_info.get("user_list"))

print(server_info.keys())
print(server_info.values())
print(server_info.items())
#딕셔너리 핵심 함수 : keys(), values(), items(), get()
#언제든지 변환해서 사용할 수 있음
