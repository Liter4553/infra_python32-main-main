import json
import os  # 폴더 생성을 위해 추가

students = [
    {"name": "안다솜", "city": "경기 ", "mbti": "ISTP", "sibling": "1", "pbl": "false"},
    {"name": "양태규", "city": "광주", "mbti": "ENTP", "sibling": None, "pbl": None},
    {"name": "엄민욱", "city": "파주", "mbti": "ENFJ", "sibling": "2", "pbl": "true"},
    {"name": "오승백", "city": "천안", "mbti": "ESFJ", "sibling": "2", "pbl": "True"},
    {"name": "우유엘", "city": "수원", "mbti": "INTP", "sibling": "2", "pbl": "False"},
]

# 1. 저장할 폴더 경로 설정
directory = "day3/file_system/security_logs"

# 2. 폴더가 없으면 생성 (exist_ok=True는 이미 폴더가 있어도 에러를 내지 말라는 뜻)
os.makedirs(directory, exist_ok=True)

# 3. 파일 저장 (파일명에 .json 확장자 추가 추천)
file_path = os.path.join(directory, "daily.json")

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(students, f, indent=4, ensure_ascii=False)

print(f"파일이 성공적으로 저장되었습니다: {file_path}")