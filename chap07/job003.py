# -*- coding:utf-8 -*-

import os


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
            with open(src_full_path, "rb+") as fobj_in, open(dst_full_path,"wb+") as fobj_out:
                while True:
                    buf = fobj_in.read()
                    if not buf:
                        break
                    fobj_out.write(buf)


import time

def wrap_list_files(func):
    def wrap(path):
        start_time = time.time()
        res = func(path)
        end_time = time.time()
        print("cost time:{}s".format(end_time - start_time))
        return res
    return wrap


def wrap_copy_files(func):
    def wrap(path, new_dir, all_files):
        start_time = time.time()
        res = func(path, new_dir, all_files)
        end_time = time.time()
        print("cost time:{}s".format(end_time - start_time))
        return res
    return wrap




path = r"E:\weixin\WeChat Files\wxid_hd6r03y9il5d21\Files"
new_dir = r"G:\weixin_files"

all_files = wrap_list_files(list_files)(path)
wrap_copy_files(copy_files)(path, new_dir, all_files)
# all_files = list_files(path)
# copy_files(path, new_dir, all_files)