#!/usr/bin/python3
#-*- coding: UTF-8 -*-
import os
import os.path

ls = []

def getAppointFile(path, ls):
    fileList = os.listdir(path)
    try:
        for tmp in fileList:
            pathTmp = os.path.join(path, tmp)
            if True == os.path.isdir(pathTmp):
                getAppointFile(pathTmp, ls)
            elif pathTmp[pathTmp.rfind(".")+1:].upper() == "PY":
                ls.append(pathTmp)
    except PermissionError:
        pass

def main():

    while True:
        path = input('请输入路径:').strip()
        if os.path.isdir(path) == True:
            break

    getAppointFile(path,ls)
    # #print(len(ls))
    for tmp in ls:
        print(tmp, end=" ")
    print()
    print(ls)
    print("Totals: %d " % len(ls))

main()