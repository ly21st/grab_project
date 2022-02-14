# -*- coding: utf-8

import os


def get_all_python_lib_files(path, sep):
    file_list = []
    files = os.listdir(path)
    for file in files:
        file_full_path = path + sep + file
        if os.path.isfile(file_full_path) and file_full_path.endswith(".py"):
            file_list.append(file_full_path)
        elif os.path.isdir(file_full_path):
            file_list.extend(get_all_python_lib_files(file_full_path))

    return file_list


path = r"E:\ProgramData\Anaconda3\envs\python37\lib"
file_list = get_all_python_lib_files(path, "\\")

print(file_list)
print(len(file_list))


