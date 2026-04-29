# str - split 함수
message="위험-사용자인증실패-2026-04-27"

msg_list = message.split("-")
risky_level = msg_list[0]
real_msg = msg_list[1]
date_list = msg_list[2:]

print(risky_level, real_msg, date_list)

names = "            최인규, 우유엘, 신지혜, 남보라, 민병연\n김명성, 김성현, 김수정, 서지우, 김태현\n한서현\n\n\n\n\n\n"
print(names.strip().replace(" ", "").replace("\n", ",").replace(",", "\n")) # method chaining