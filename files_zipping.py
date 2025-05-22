""" 
# CREATING ARCHIVE FROM FILES 
from pathlib import Path 
import zipfile 

root_dir = Path("file_outputs") 

archive_dir = Path("archives")
archive_dir.mkdir(parents=True, exist_ok=True) 

archive_path = archive_dir / "archive.zip"
# archive_path = root_dir / Path("archive.zip") 

with zipfile.ZipFile(archive_path, 'w') as zf:
    for path in root_dir.rglob("*.txt"): 
        zf.write(path)
        path.unlink()  # this removes the folders carried on during zipping process 
""" 

# CREATING ARCHIVE FROM FILES 
from pathlib import Path 
import zipfile 

root_dir = Path("file_outputs/first") 
archive_path = root_dir / Path("archive.zip") 

with zipfile.ZipFile(archive_path, 'w') as zf:
    for path in root_dir.rgrob("*.txt"): 
        zf.write(path)
