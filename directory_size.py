import os
import sys

if __name__ == '__main__':
    try:
        directory = input("Enter the directory which you want to get size : ")
    except IndexError:
        sys.exit("Invalid directory")

    dir_size = 0
    readable_sizes = {'B': 1,
                 'KB': float(1) / 1024,
                 'MB': float(1) / (1024 * 1024),
                 'GB': float(1) / (1024 * 1024 * 1024)
                      }
    for (path, dirs, files) in os.walk(directory):
        for file in files:
            filename = os.path.join(path, file)
            dir_size += os.path.getsize(filename)
    readable_sizes_list = [str(round(readable_sizes[key] * dir_size, 2)) + " " + key for key in readable_sizes]

    if dir_size == 0:
        print("File Empty")
    else:
        for units in sorted(readable_sizes_list)[::-1]:
            print("Folder Size: " + units)