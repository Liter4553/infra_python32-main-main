#import os
#
#if not os.path.exists("security_logs/daily"):
#    os.makedirs("security_logs/daily")
#    print(os.path("security_logs/daily"))

import  os

#디렉터리 존재 확인 - os.path.exists("경로")
if not os.path.exists("day3/file_system/security_logs/daily"):
    os.makedirs("day3/file_system/security_logs/daily")
#디렉터리 생성 - os.makedirs("경로") : 줄줄이 생성

#디렉터리 하위에 텍스트 파일 생성, test 글자 삽입
with open("day3/file_system/security_logs/daily/log.txt", "w") as f:
    f.write("test")


#파일명 추출
file_name = os.path.basename("day3/file_system/security_logs/daily/log.txt")
print(file_name)