from pathlib import Path
import shutil   

source = Path("day3/file_system/secirity_logs/log1500.txt")
dest = Path("day3/file_system/securitylogs/log1408.txt")

if source.exists():
    # shutil.move(str(source), str(dest))
    source.rename(dest)
