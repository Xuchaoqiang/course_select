#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving
import pickle
from modules.school import School
from modules.course import Course
from conf import settings

DB_DIR = settings.DB_DIR

def initialization_db():
    '''
    初始化数据库， 两个学校，3门课程
    :return:
    '''
    # 初始化学校
    s_school = School('Shanghai')
    b_school = School('Beijing')
    # 初始化课程
    l_course = Course('linux', '80days', '6000')
    p_course = Course('py', '90days', '9999')
    g_course = Course('go', '70days', '5000')
    # 课程关联学校
    s_school.courses['go'] = g_course
    b_school.courses['linux'] = l_course
    b_school.courses['py'] = p_course
    with open(DB_DIR + r'\%s.txt' % b_school.name, 'wb') as f:
        pickle.dump(b_school, f)
    with open(DB_DIR + r'\%s.txt' % s_school.name, 'wb') as f1:
        pickle.dump(s_school, f1)

def load_db(tmp):
    with open(DB_DIR + r'\%s.txt' % tmp, 'rb') as f:
        school_obj = pickle.load(f)
        return school_obj

