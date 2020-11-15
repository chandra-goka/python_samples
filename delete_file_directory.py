import os
import shutil

file= input("Enter file name to delete: ")

if os.path.isfile(file):
    os.remove(file)
else:
    print(f"Error: {file} file not found")


if os.path.isfile(file):
    os.unlink(file)
else:
    print(f"Error: {file} file not found")

if os.path.isdir(file):
    os.rmdir(file)
else:
    print(f"Error: {file} file not found")

if os.path.isdir(file):
    shutil.rmtree(file)
else:
    print(f"Error: {file} file not found")
