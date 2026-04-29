import os
import random
from dotenv import load_dotenv

load_dotenv()
admin = os.getenv("ADMIN_NAME", "GUEST")

whitelist = ("192.168.1.10", "192.168.1.11")
server_assets = [
    {"name": "WEB-01", "ip":"192.168.1.10", "status":"Run"},
    {"name": "DB-01", "ip":"192.168.1.20", "status":"Stop"}
    
]

new_name = input("추가할 서버 이름: ")
new_ip = input("추가할 서버 IP: ")
cpu_usage = random.uniform(0, 100)
server_assets.append({"name": new_name, "ip": new_ip, "status":"Run", "CPU_usage": cpu_usage})

server_assets[0]["status"] = "Stop"

print(f"총 {len(server_assets)}대의 서버의 보안 점검을 수행합니다.")
print("-"*40)
print(f"[담당자: {admin}] {server_assets[0]['name']} 서버({server_assets[0]['status']}) 점검 수행")
print(f"-화이트 리스트 대상 여부: {server_assets[0]['ip'] in whitelist}")
print("-"*40)
print(f"[담당자: {admin}] {server_assets[1]['name']} 서버({server_assets[1]['status']}) 점검 수행")
print(f"-화이트 리스트 대상 여부: {server_assets[1]['ip'] in whitelist}")
print("-"*40)
print(f"[담당자: {admin}] {server_assets[2]['name']} 서버({server_assets[2]['status']}) 점검 수행")
print(f"-화이트 리스트 대상 여부: {server_assets[2]['ip'] in whitelist}/현재 부하: {server_assets[2]['CPU_usage']:.1f}%")
print("-"*40)