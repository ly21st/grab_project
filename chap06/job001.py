# -*- coding:utf-8 -*-

import os


path = r"E:\weixin\WeChat Files\wxid_hd6r03y9il5d21\Files"

def list_files(path):
    all_files = {}
    dir = os.listdir(path)
    for file in dir:
        # print(file)
        suffix = file.rpartition(".")[-1]
        if not suffix:
            continue
        file_list = all_files.get(suffix)
        if not file_list:
            file_list = []
        file_list.append(file)
        all_files.update({suffix: file_list})

    # for key, val in all_files.items():
    #     print("{}:{}".format(key, val))
    return all_files



# def copy_files(path, new_dir, all_files):
#     for key, val in all_files.items():
#         sub_dir = new_dir + "\\" + key
#         if not os.path.exists(sub_dir):
#             os.mkdir(sub_dir)
#         print("{}:{}".format(key, val))
#         for file in val:
#             src_full_path = path + "\\" + file
#             dst_full_path = sub_dir + "\\" + file
#             print("src_full_path:", src_full_path)
#             print("dst_full_path:", dst_full_path)
#             fobj_in = open(src_full_path, "r+", encoding = 'utf-8', errors='ignore')
#             fobj_out = open(dst_full_path, "w+", encoding = 'utf-8', errors='ignore')
#
#             while True:
#                 buf = fobj_in.read()
#                 if not buf:
#                     break
#                 fobj_out.write(buf)
#
#             fobj_in.close()
#             fobj_out.close()

def copy_files(path, new_dir, all_files):
    for key, val in all_files.items():
        sub_dir = new_dir + "\\" + key
        if not os.path.exists(sub_dir):
            os.mkdir(sub_dir)
        print("{}:{}".format(key, val))
        for file in val:
            src_full_path = path + "\\" + file
            dst_full_path = sub_dir + "\\" + file
            print("src_full_path:", src_full_path)
            print("dst_full_path:", dst_full_path)
            with open(src_full_path, "r+", encoding = 'utf-8', errors='ignore') as fobj_in, open(dst_full_path,"w+", encoding = 'utf-8', errors='ignore') as fobj_out:
                while True:
                    buf = fobj_in.read()
                    if not buf:
                        break
                    fobj_out.write(buf)


new_dir = r"G:\weixin_files"

all_files = list_files(path)
copy_files(path, new_dir, all_files)