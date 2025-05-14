from pathlib import Path 

# path  = Path('file_outputs/second.txt')
# print(path.exists())
# print(type(path))

# if not path.exists(): 
#     with open(path, 'w') as file: 
#         content = "this text file is the second file to be written"
#         file.write(content)

# with open(path, 'a') as file: 
#     cont = " \nHere is the second line for this file \n "
#     file.write(cont) 

# print(path.name)
# print(path.stem) 

""" 
# HOW TO REMANE FILES AFTER CREATING AND READING THEM   
root_dir = Path('file_outputs/new-names')         
file_paths = root_dir.iterdir()
# print(Path.cwd())

for path in file_paths:  
    new_name = "new-" + path.name
    new_path = path.with_name(new_name) 
    print(new_path) 
    path.rename(new_path) 

    with open(new_path, 'a') as file: 
        cont = " \nThis content is added to the new file after renaming it \n"
        file.write(cont)
        print("content is written") 
""" 

#  RENAMING FILE BASED ON THE DIRECTORY NAME AND USING GLOB FUNCTION

# practical example  
"""
root_dir = Path('file_outputs')
file_path = root_dir.glob("**/*") 

for path in file_path: 
    if path.is_file(): 
        parent_folder = path.parts[1] 
        new_filename = parent_folder + "_" + path.name 
        print
        new_path = path.with_name(new_filename) 
        print(new_path) 
        path.rename(new_path) 
"""

""" 
root_dir = Path('file_outputs')
file_path = root_dir.glob("**/**/*") 

for item in file_path: 
    if item.is_file(): 
        p_folder = item.parts[1]
        p_folder2 = item.parts[2]
        new_filename = p_folder + '-' + p_folder2 + '-' + item.name
        print(new_filename) 
        new_path = item.with_name(new_filename) 
        item.rename(new_path)

        with open(new_path, 'a') as file: 
            cont = "\nThis is appended after the file is renamed \n" 
            file.write(cont) 
            print("content written") 
"""

# CHECKING DATE AND TIME FILES WERE CREATED 
from pathlib import Path 
from datetime import datetime
# path = Path("file_outputs/first/ap/one")
# stats = path.stat() 
# second_created = stats.st_ctime 
# print(second_created) 
# date_created = datetime.fromtimestamp(second_created)  
# date_created_str = date_created.strftime("%Y_%m_%d %H-%M-%S")
# print(f"The file was createed on: {date_created_str}") 

""" 
root_dir = Path('file_outputs')
root_path = root_dir.glob('**/**/**/*')
for file in root_path: 
    if file.is_file(): 
        stats = file.stat() 
        second_created = stats.st_ctime 
        print(second_created) 
        date_created = datetime.fromtimestamp(second_created)

        # can be simplifid to 
        # date_created_option = datetime.fromtimestamp(file.stat().st_ctime) 
        #  
        date_created_str = date_created.strftime("%Y_%m_%d-%H-%M-%S")
        print(f"The file {file.name} was createed on: {date_created_str}") 
        new_filename = date_created_str + "_" + file.name
        new_file_path = file.with_name(new_filename)  
        file.rename(new_file_path)  
        print(f"   The file has been renamed to: {date_created_str}")  
"""

# CONVERSION FROM TXT TO CSV 
root_dir = Path('file_outputs') 
filepath = root_dir.rglob("*") 

for file in filepath: 
    if file.is_file(): 
        new_filepath = file.with_suffix(".txt") 
        file.rename(new_filepath)

