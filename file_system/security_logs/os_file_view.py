#import glob
#
#text_file_os = glob.glob("*.txt")
#print(text_file_os)

from pathlib import Path

py_file_pathlib = Path("day1").glob("*.py")

for f in py_file_pathlib:
    print(f"파일명: {f.name}, 파일크기: {f.stat().st_size}kb") #f.뒤에 많은 모듈을 붙일 수 있음, f.name, f.stat(),st_size, f.stat().st_birthtime 