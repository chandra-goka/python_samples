import zipfile
import os


def prepare_zip(dir_path):
    new_file = dir_path + '.zip'
    # creating zip file with write mode
    zip = zipfile.ZipFile(new_file, 'w', zipfile.ZIP_DEFLATED)
    # Walk through the files in a directory
    for dir_path, dir_names, files in os.walk(dir_path):
        f_path = dir_path.replace(dir_path, '')
        f_path = f_path and f_path + os.sep
        # Writing each file into the zip
        for file in files:
            zip.write(os.path.join(dir_path, file), f_path + file)
    zip.close()
    print("File Created successfully..")
    return new_file

def extract_zip(dir_path):
    with zipfile.ZipFile(dir_path+'data.zip', 'r') as zip_inst:
        zip_inst.extractall(dir_path)

if __name__ == '__main__':
    prepare_zip('C:\\Users\\Lenovo\\Documents\\Data')
    extract_zip('C:\\Users\\Lenovo\\Documents\\Data\\')