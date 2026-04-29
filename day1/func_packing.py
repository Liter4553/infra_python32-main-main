def setup_firewall(ip, port, action):
    print(f"{ip}:{port} 접속 후 {action}")

config = ["127.0.0.1", "80", "BLOCK"] #args에서의 * 기능은 여기 있는 큰따옴표로 패킹되어있는 데이터를 벗겨서 각각 자리에 넣어줌(언패킹), 패킹도 같이함

setup_firewall("127.0.0.1", "80", "BLOCK")

