#-*- coding: utf-8 -*
import itertools
import os
import bz2
import gzip
import json
import pipe
import glob

##################################################
## 読み込み関数群
##################################################
def load_schema(filename_header):
    """.pig_headerからスキーマを読み込む"""
    header = open(filename_header).readline().rstrip().split()
    header = [item.split("::")[-1] for item in header]
    return header

def open_with_expansion(filename):
    """拡張子に応じて圧縮済みファイルを開く"""
    root, ext = os.path.splitext(filename)
    if ext == '.bz2':
        f = bz2.BZ2File(filename)
    elif ext == '.gz':
        f = gzip.open(filename, 'r')
    else:
        f = open(filename)
    return f

def string_load(filename, filename_header):
    header = load_schema(filename_header)
    f = open_with_expansion(filename)
    try:
        for line in f:
            yield dict([(k, v) for k, v in zip(header, line.rstrip().split("\t"))])
    finally:
        f.close()

def directory_load(dirname,filename_header=None):
    """.pig_headerが存在しなかった場合、dirname内の.pig_headerを読む"""
    if filename_header is None:
        filename_header = dirname + '/.pig_header'
    files = sorted(glob.glob(dirname + '/part-*'))
    return itertools.chain(*[string_load(filename, filename_header) for filename in files])


def json_load(filename):
    """改行区切りのjsonファイルを読む"""
    f = open_with_expansion(filename)
    try:
        for line in f:
            yield json.loads(line)
    finally:
        f.close()

@pipe.Pipe
def json_dump(iterable, filename):
    """改行区切りのjsonとして出力"""
    f = open(filename, "w+")
    try:
        for line in iterable:
            f.write(json.dumps(line)+"\n")
    finally:
        f.close()
