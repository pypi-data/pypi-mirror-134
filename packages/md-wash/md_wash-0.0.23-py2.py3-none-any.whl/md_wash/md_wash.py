#coding: utf-8
from .logx import setup_logging
import logging
import argparse
import re
import os
import argparse
from concurrent.futures import ThreadPoolExecutor
import threading
import uuid
import requests
from shutil import copyfile
from os.path  import join,basename,dirname
from pathlib import Path
import tempfile
import shutil
from distutils.dir_util import copy_tree

# don`t remove this line
setup_logging()

logger = logging.getLogger(__name__)

import sys

# 识别一行多张图片
def get_img_url(line):
    reg = "(\!\[.*\]\(\(.*?\))*\)"
    comp= re.search(reg,line)
    if comp:
        for c in  comp.groups(0):
            reg = "\!\[.*\]\((http.*?)\)"
            comp= re.search(reg,line)
            if comp:
                yield "url",comp.groups(0)[0]
            else: 
                reg = "\!\[.*\]\((.*?)\)"
                comp= re.search(reg,line)
                if comp:
                    yield "other",comp.groups(0)[0]

def download_file(url,local_filename,timeout=10):
    # auto make dir
    os.makedirs(os.path.dirname(local_filename), exist_ok=True)
    if os.path.exists(local_filename):
        return 

    try:
        with requests.get(url, stream=True,timeout=timeout) as r:
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): 
                    if chunk: # filter out keep-alive new chunks
                        f.write(chunk)
    except Exception as identifier:
        logger.info(f"{url}  请求失败")
        logger.exception(identifier)
        

def getfiles(dirPath):
    for (dirRoot, dirnames, filenames) in os.walk(dirPath):
        return set([os.path.abspath(join(dirRoot,f)) for f in filenames])

AllAssets =set()
NeedAssets =set()
def task(relPath,output,repos):
    global AllAssets;
    global NeedAssets;
    if relPath.split(".")[-1] not in ["md","markdown",'mdown']:
        return

    newfile=""

    inplace = output == '.'
    md_assets =set()

    #  修改当前文件夹
    if inplace:
        with open(relPath) as f:
            line=f.readline()
            while line:
                for t,imgurl in get_img_url(line):
                    if not imgurl.startswith('http'):
                        a = os.path.abspath(join(dirname(relPath),imgurl))
                        md_assets.add(a)
                line=f.readline()
        #  logger.info(f'relPath:{relPath}')
        #  print(md_assets)
        # 如果有引用的地址，则做清理
        if len(md_assets)>0:
            for asset in md_assets:
                NeedAssets.add(asset)
                assetDir = dirname(asset)
                nowFilesInAssets = getfiles(assetDir)
                if nowFilesInAssets:
                    AllAssets = AllAssets.union(nowFilesInAssets)

                #  nowFilesInAssets = getfiles(assetDir)
                if not os.path.isfile(asset):
                    missed = os.path.abspath(asset)
                    if repos:
                        for repo in repos:
                            missedName = basename(missed)
                            tryFindPathName = join(repo,missedName)
                            if os.path.exists(tryFindPathName):
                                os.makedirs(dirname(missed), exist_ok=True)                    
                                shutil.copyfile(tryFindPathName,os.path.abspath(missed))
                                print("copyed ==>",tryFindPathName,os.path.abspath(missed))
                                break
                            else:
                                pass

            #  print(md_assets)
            #  AllAssets = AllAssets.difference(md_assets)

    else:
        with open(relPath) as f:
            line=f.readline()
            while line:
                # handle assets
                for t,imgurl in get_img_url(line):
                    if t=="url":
                        pass
                    else:
                        # copy  file
                        src = os.path.join(dirname(relPath),imgurl)
                        local_filename =join(output,src)
                        os.makedirs(dirname(local_filename), exist_ok=True)                    
                        logger.info(f"----\n{src}\n{local_filename}")
                        if os.path.isfile(src):
                            copyfile(os.path.join(os.path.dirname(relPath),imgurl.strip()), local_filename)
                        else:
                            logger.error(f"not found: {src}")
                            pass
                        try:
                            if ifDeletedOriginFile:
                                logger.warn(f"delete {src}")
                                os.remove(src)
                        except:
                            pass

                # append new line to new markdown 
                newfile+=line
                line=f.readline()

             # save back to file
            fullOutputPath=join(output,relPath)
            os.makedirs(os.path.dirname(fullOutputPath), exist_ok=True)                    
            f = open(fullOutputPath, 'w')
            logger.info(f"----\n{relPath}\n{fullOutputPath}")
            f.write(newfile)
            f.close()


def moveMdDir(fromDir,toDir):
    pass
def moveMdFile(fromPath,toPath):
    pass

def main(args):
    inputsrc             = args.input
    outputDir            = args.outputDir
    # 是否修改当前文件夹
    isDirSrc             = os.path.isdir(inputsrc)
    repos                 = args.asset_folder

    if not os.path.exists(inputsrc):
        logger.exception(f'{inputsrc} not exist')
        return 

    # not dir just one file
    if not isDirSrc:
        task(inputsrc,outputDir,repos)
    else:
        inputDirPath = inputsrc

        for (dirRoot, dirnames, filenames) in os.walk(inputDirPath):
            for filename in filenames:
                inputsrc2 = os.path.relpath(join(dirRoot,filename))
                task(inputsrc2,outputDir,repos)

    # clean unused assets
    toDeletedAssets = AllAssets.difference(NeedAssets)
    if len(toDeletedAssets)==0:
        logger.info(f'nothing to wash')

    for r in toDeletedAssets:
        d = dirname(r)
        os.remove(r)
        logger.info(f'deleted file:{r}')
        if not getfiles(d):
            os.removedirs(d)
            logger.info(f'deleted Dir:{d}')


def entry_point():
    parser = createParse()
    mainArgs=parser.parse_args()
    main(mainArgs)


def createParse():
    parser = argparse.ArgumentParser( formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('input', type=str, help='指定你 md 的目录, 或者 md 文件')
    #  parser.add_argument('outputDir', type=str, help='指定你 md output 的目录')
    parser.add_argument('-o', '--outputDir', type=str, help='指定你 md output 的目录', required=False, default='.')
    parser.add_argument('-r', '--asset_folder', action='append', help='图片文件夹搜索地址，如果md 里图片路径找不到，则会通过名字在此地址查找, 可指定多个 -r', required=False,)
    return parser
