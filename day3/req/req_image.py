import requests


try:
    code_input = int(input("상태 코드를 입력하세요: "))

    if code_input < 200 or code_input > 599:
        raise ValueError("상태코드 아닙니다.")
    
    req_url = "https://http.cat/" + str(code_input)



    resp = requests.get(req_url)
    
    # 응답이 성공적이고 데이터가 이미지인 경우만 저장
    if resp.status_code == 200 and "image" in resp.headers.get("Content-Type"):
        with open(f"day3/{str(code_input)}.jpg", 'wb') as f:
            f.write(resp.content)
        print(f"성공: day3/{code_input}.jpg 파일이 저장되었습니다.")


except Exception as e:
    print(f"발생한 에러: {e}")