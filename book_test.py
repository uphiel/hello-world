#!/usr/bin/python3
#-*- coding:utf-8 -*-
import ftplib


def anonLogin(hostname):
    print("Hello world!")
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'me@your.com')
        print('\n[*] ' + str(hostname) + ' FTP AnonymousLogon Succeeded!')
        ftp.quit()
        return True
    except Exception:
        print('\n[-] ' + str(hostname) + ' FTP AnonymousLogon Failed!')
        return False

host = '192.168.95.179'
anonLogin(host)
