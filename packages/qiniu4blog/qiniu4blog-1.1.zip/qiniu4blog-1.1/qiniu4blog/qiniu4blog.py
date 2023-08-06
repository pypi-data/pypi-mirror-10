#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, time, sys ,ConfigParser,platform,urllib
import qiniu
from mimetypes import MimeTypes
import sys
import pyperclip
from os.path import expanduser


homedir = expanduser("~")
config = ConfigParser.RawConfigParser()
config.read(homedir+'/qiniu.cfg')
mime = MimeTypes()



try:
    bucket = config.get('config', 'bucket')
    accessKey = config.get('config', 'accessKey')
    secretKey = config.get('config', 'secretKey')
    path_to_watch = config.get('config', 'path_to_watch')
    enable = config.get('custom_url','enable')
    if enable == 'false':
        print 'custom_url not set'
    else:
        addr = config.get('custom_url','addr')


except ConfigParser.NoSectionError, err:
    print 'Error Config File:', err

def setCodeingByOS():
    '''获取系统平台,设置编解码'''
    if 'cygwin' in platform.system().lower():
        CODE = 'GBK'
    elif os.name == 'nt' or platform.system() == 'Windows':
        CODE = 'GBK'
    elif os.name == 'mac' or platform.system() == 'Darwin':
        CODE = 'utf-8'
    elif os.name == 'posix' or platform.system() == 'Linux':
        CODE = 'utf-8'
    return  CODE

def set_clipboard(url_list):
	for url in url_list:
		pyperclip.copy(url)
	spam = pyperclip.paste()



def parseRet(retData, respInfo):
    '''处理上传结果'''
    if retData != None:
        print("Upload file success!")
        print("Hash: " + retData["hash"])
        print("Key: " + retData["key"])
        for k, v in retData.items():
            if k[:2] == "x:":
                print(k + ":" + v)
        for k, v in retData.items():
            if k[:2] == "x:" or k == "hash" or k == "key":
                continue
            else:
                print(k + ":" + str(v))
    else:
        print("Upload file failed!")
        print("Error: " + respInfo.text_body)


def upload_without_key(bucket, filePath, uploadname):
    '''上传文件'''
    auth = qiniu.Auth(accessKey, secretKey)
    upToken = auth.upload_token(bucket, key=None)
    key = uploadname
    retData, respInfo = qiniu.put_file(upToken, key, filePath, mime_type=mime.guess_type(filePath)[0])
    parseRet(retData, respInfo)

import os

def get_filepaths(directory):
    file_paths = []  # List which will store all of the full filepaths.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.
    return file_paths  # Self-explanatory.


def main():
    print "running ... ..."
    before =  get_filepaths(path_to_watch)
    while 1:
        time.sleep(1)
        after = get_filepaths(path_to_watch)
        added = [f for f in after if not f in before]
        removed = [f for f in before if not f in after]
        if added:
            print "Added Files: ", ", ".join(added)
            # print added
            url_list = []
            for i in added:
                if platform.system() == 'Windows':
                    fileName = "/".join("".join(i.rsplit(path_to_watch))[1:].split("\\"))
                else:
                    fileName = "".join(i.rsplit(path_to_watch))[1:]
                upload_without_key(bucket, i, fileName.decode(setCodeingByOS()))
                if enable == 'true':
                    url = addr + urllib.quote(fileName.decode(setCodeingByOS()).encode('utf-8'))
                else:
                    url = 'http://' + bucket + '.qiniudn.com/' + urllib.quote(fileName.decode(setCodeingByOS()).encode('utf-8'))
                url_list.append(url)

            with open('image_markdown.txt', 'a') as f:
                for url in url_list:
                    image = '![' + url + ']' + '(' + url + ')' + '\n'
                    f.write(image)
            print "image url [markdown] is save in image_markdwon.txt"

            set_clipboard(url_list)
        if removed:
            print "Removed Files: ", ", ".join(removed)
            print  removed
        before = after

if __name__ == "__main__":
	main()


