#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/6 9:06 下午
# @Author  : lance.txl
# @Site    : 
# @File    : utils.py
# @Software: PyCharm

import os
import hashlib
import cv2
import random
import re

def ergodicDir(Dir, FileType=""):
    fileDict = {}
    for parent, dirnames, filenames in os.walk(Dir):
        for i in filenames:
            if FileType != "":
                if i.split(".", -1)[-1] == FileType:
                    fileDict[os.path.join(parent, i)] = os.path.join(parent, i)
            else:
                fileDict[os.path.join(parent, i)] = os.path.join(parent, i)
    return fileDict


def get_md5(s):
    m = hashlib.md5()
    m.update(s.encode("utf-8"))
    unique_id = m.hexdigest()
    return unique_id

def show_or_save_pic(pic,savename=None):
    if isinstance(pic,str):
        pic = cv2.imread(pic)
    name = "windowname_" + random.choice(list("abcdefg"))
    print(name)
    cv2.namedWindow(name,cv2.WINDOW_NORMAL)
    cv2.imshow(name,pic)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyWindow(name)
    elif k == ord("s"):
        if savename:
            cv2.imwrite(savename,pic)
        else:
            cv2.imwrite(name + ".png",pic)
        cv2.destroyWindow(name)

