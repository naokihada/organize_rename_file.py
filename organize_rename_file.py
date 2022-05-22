from pathlib import Path
from datetime import datetime
import os
import sys
import shutil

def print_usage():
    print("Usage:")
    print("python organize_rename_file.py original_folder_path destination_folder_path")
    print("ex) python organize_rename_file.py C:/temp/org C:/temp/dst")

def organize_files(org_folder_path: Path, dst_folder_path: Path):
    for file in org_folder_path.glob("**/*"):  # subfolder supported
    # for file in org_folder_path.iterdir():  # no subfolder supported

        if file.is_file() and file.name != ".DS_Store":
            timestamp: float = os.path.getmtime(file)  # modefied time
            dt: datetime = datetime.fromtimestamp(timestamp)  # convert to datetime

            eight_digit: str = str(dt.year) + str(dt.month).zfill(2) + str(dt.day).zfill(2)

            new_file_name: str = file.name  # default
            if eight_digit not in file.name:  # add prefix if not contained (avoid duplicate)
            # if not file.name.startswith(eight_digit):  # add prefix if not startswith
                new_file_name = eight_digit + "-" + file.name

            new_folder_path: Path = dst_folder_path.joinpath(
                str(dt.year) + "/" + str(dt.month).zfill(2) + "/" + str(dt.day).zfill(2))  # YYYY/MM/DD
            # new_folder_path = org_folder_path.joinpath(str(dt.year)+"/"+str(dt.month).zfill(2)) # YYYY/MM

            if not new_folder_path.exists():  # check if exist
                os.makedirs(new_folder_path)  # create folder recursively

            new_file_path: Path = new_folder_path.joinpath(new_file_name)  # add file name to the path

            print(new_file_path)  # output
            # print(file.name + " => " + new_file_path)  # output

            shutil.copy2(file, new_file_path)  # copy file (duplicate)
            # file.replace(new_file_path)  # move file

# command line parameter
args = sys.argv

# # test only
# args = ["T:/test_org", "T:/test_dst"]

if len(args) < 2:
    print_usage()
else:
    print("Original path   : " + args[1])
    print("Destination path: " + args[2])

    org_folder_path: Path = Path(args[1])  # original folder
    dst_folder_path: Path = Path(args[2])  # destination folder

    if not org_folder_path.exists():
        print("Specified path not found")
    else:
        organize_files(org_folder_path, dst_folder_path)
