import random

# 관리자 이름 묻기
manager_name = input('관리자 이름을 입력하세요: ')

# 서버 ID 생성 (random 모듈 import!!!)
server_num = random.randint(1, 50)
server_id = f"SVR-{server_num:02d}"

# CPU 사용률 생성 (random 모듈 import!!!)
cpu_usage = random.uniform(0.0, 100.0)
cpu_percent = f"{cpu_usage:.1f}%"

# 처리 로그 수
log_count = random.randint(1000, 1000000)

print(f"[점검 보고서] 담당자: {manager_name} / {server_id} {cpu_percent} / 누적 로그 수 : {log_count:,}")