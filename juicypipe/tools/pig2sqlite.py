#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
pigの出力ファイルからsqlite3のDBを作る

実行
  pig2sqlite.py hoge.tsv hoge/.pig_header
出力ファイル
  pipestore.sqlite3
"""
import pipe
import juicypipe
import sqlite3
import argparse
from pipe import Pipe


parser = argparse.ArgumentParser()
parser.add_argument("filename")
parser.add_argument("filename_header", help="tsv形式のカラム名ファイル .pig_header")
parser.add_argument("--tablename", default="pipestore")
parser.add_argument("--outfilename", default="pipestore.sqlite3")

def main():
    args = parser.parse_args()
    (juicypipe.string_load(args.filename, args.filename_header)
        | juicypipe.sqlite3_store(
            filename=args.outfilename,
            tablename=args.tablename
        )
    )

if __name__ == '__main__':
    main()
