import csv
import os

# 데이터를 저장할 폴더가 없으면 자동으로 생성해주는 코드 (선택사항)
os.makedirs("day3/csv", exist_ok=True)

one_students = [
    {"name": "민병연", "city": "서울", "mbti": "INTJ"},
    {"name": "박건우", "city": "대구", "mbti": "ISTP"},
    {"name": "박민호", "city": "광주", "mbti": "ISTJ"},
    {"name": "박예은", "city": "인천", "mbti": "ESFJ"},
]

two_students = [
    {"name": "박진솔", "city": "경기", "mbti": "INTP"},
    {"name": "백세희", "city": "서울", "mbti": "ESTJ"},
    {"name": "백정민", "city": "부산", "mbti": "ISTP"},
    {"name": "양태규", "city": "광주 ", "mbti": "ENTP"},
]

three_students = [
    {"name": "서지우", "city": "서울"}, # mbti 없음 -> 빈칸으로 저장됨
    {"name": "송보연", "city": "경기"}, 
    {"name": "송석현", "city": "안양"}, 
    {"name": "신지혜", "city": "인천"},
]

column_names = ["name", "city", "mbti"]

# 경로를 슬래시(/)로 쓰면 윈도우/맥/리눅스 모두에서 잘 작동합니다.
with open("day3/csv/student_analysis_report.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=column_names)
    
    # 1. 헤더(name, city, mbti) 쓰기
    writer.writeheader()
    
    # 2. 데이터 순차적으로 쓰기
    writer.writerows(one_students)
    writer.writerows(two_students)
    writer.writerows(three_students)

print("작업이 완료되었습니다.")