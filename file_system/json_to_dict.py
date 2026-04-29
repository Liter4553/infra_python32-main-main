import json


#json형태를 갖고있지만 그냥 문자열
raw_json_str = '[{[{"name": "안다솜", "city": "경기", "mbti": "ISTP", "sibling": 1, "pbl": false}, {"name": "양태규", "city": "광주", "mbti": "ENTP", "sibling": 0, "pbl": null}, {"name": "엄민욱", "city": "파주", "mbti": "ENFJ", "sibling": 2, "pbl": true}, {"name": "오승백", "city": "천안", "mbti": "ESFJ", "sibling": 2, "pbl": true}, {"name": "우유엘", "city": "수원", "mbti": "INTP", "sibling": 2, "pbl": false}]}]'

#문자열을 가져와서 딕셔너리 형태로 변환

json_dict = json.loads(raw_json_str)
print(json_dict[1])
json_list = json.loads(raw_json_str)
for s in json_list:
    print(s["name"])

    #students.json 파일을 가져와서 딕셔너리로 변환

# 2. students.json 파일을 가져와서 dictionary로 변환
with open("day3/json/students.json", "r", encoding="utf-8") as f:
    student_list = json.load(f)
    for s in student_list:
        print(s["name"])