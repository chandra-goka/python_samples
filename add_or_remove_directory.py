import os

#List directories in a current working directory
print(os.listdir())
#Create Directory
os.mkdir("sample_dir")

#Create subdirectories
os.makedirs("sample_dirs/sample-child")

#Remove Directory
os.rmdir("sample_dir")

#Remove sub directories
os.removedirs("sample_dirs/sample-child")


