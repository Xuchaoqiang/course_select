#! _*_coding:utf-8 _*_
#__author__:"Irving"

import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
from core import main
from conf import settings
from modules import db_handle

DB_DIR = settings.DB_DIR

if __name__ == '__main__':
    # 初始化数据库
    if not os.path.exists(DB_DIR + r'\Beijing.txt'):
        db_handle.initialization_db()
        print('\033[31;1m数据库初始化成功!\033[0m')
    # 程序入口
    main.run()
