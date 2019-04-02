#!-*- coding:utf-8 -*-
#__author__:"irving"

import os
from modules.student import Student
from conf import settings
from modules import db_handle

DB_DIR = settings.DB_DIR

START_MENU = '''\033[36;1m(1) 学员视图
(2) 讲师视图
(3) 管理员视图
 q  退出程序\033[0m'''

MANAGER_MENU = '''\033[36;1m(1) create_grade
(2) create_teacher
(3) create_course
(4) cat_grade_info
(5) cat_teacher_info
(6) cat_course_info
(7) cat_student_info
 q  返回上一层 \033[0m'''

STUDENT_MENU = '''\033[36;1m(1) register
(2) payment
(3) select_grade
(4) input_record
 q  返回上一层 \033[0m'''

TEACHER_MENU = '''\033[36;1m(1) cat_grade_student
(2) modify_student_record
 q  返回上一层 \033[0m'''


def manager_view():
    '''
    管理员视图
    :return:
    '''
    print('\033[33;1m欢迎进入管理员视图！\033[0m')
    choice = input('\033[36;1m请输入要管理的学校（Beijing or Shanghai）：\033[0m ').strip()
    if os.path.exists(DB_DIR + r'\%s.txt' % choice):
        school_obj = db_handle.load_db(choice)
        print('\033[35;1m ---------欢迎来到%s老男孩学校--------- \033[0m' % choice)
        while True:
            print(MANAGER_MENU)
            choice1 = input('请输入相应操作：')
            # if hasattr(school_obj, choice1):      # 为了方便用户操作，就不用这种方式了
            #     getattr(school_obj, choice1)()
            if choice1 == '1':
                school_obj.create_grade()
            elif choice1 == '2':
                school_obj.create_teacher()
            elif choice1 == '3':
                school_obj.create_course()
            elif choice1 == '4':
                school_obj.cat_grade_info()
            elif choice1 == '5':
                school_obj.cat_teacher_info()
            elif choice1 == '6':
                school_obj.cat_course_info()
            elif choice1 == '7':
                school_obj.cat_student_info()
            elif choice1 == 'q':
                break
            else:
                print('\033[31;1m请输入正确指令！\033[0m')
    else:
        print('\033[33;1m该学校不存在！\033[0m')

def student_view():
    '''
    学员视图
    :return:
    '''
    print('\033[33;1m欢迎进入学员视图！\033[0m')
    choice = input('\033[36;1m请选择学校（Beijing or Shanghai）：\033[0m ').strip()
    if os.path.exists(DB_DIR + r'\%s.txt' % choice):
        school_obj = db_handle.load_db(choice)
        print('\033[35;1m ---------欢迎来到%s老男孩学校--------- \033[0m' % choice)
        while True:
            print(STUDENT_MENU)
            choice1 = input('请输入相应操作：')
            if choice1 == '1':
                name = input('name >>: ').strip()
                if name not in school_obj.students:
                    age = input('age >>:').strip()
                    sex = input('sex >>:').strip()
                    student_obj = Student(name, age, sex)
                    school_obj.students[name] = student_obj
                    school_obj.save_school_db()
                    print('\033[33;1m学员%s 注册成功！\033[0m' % name)
                else:
                    print('\033[33;1m不好意思，此学员已存在！\033[0m')
            elif choice1 == '2':
                name = input('请输入学员名字：').strip()
                if name in school_obj.students:
                    student_obj = school_obj.students[name]
                    student_obj.payment(school_obj)
                else:
                    print('学员未注册！')
            elif choice1 == '3':
                name = input('请输入学员名字：').strip()
                if name in school_obj.students:
                    student_obj = school_obj.students[name]
                    student_obj.select_grade(school_obj)
                else:
                    print('学员未注册！')
            elif choice1 == '4':
                name = input('请输入学员名字：').strip()
                if name in school_obj.students:
                    student_obj = school_obj.students[name]
                    student_obj.input_record(school_obj)
                else:
                    print('学员未注册！')
            elif choice1 == 'q':
                break

def teacher_view():
    '''
    讲师视图
    :return:
    '''
    print('\033[33;1m欢迎进入讲师视图！\033[0m')
    choice = input('\033[36;1m请选择学校（Beijing or Shanghai）：\033[0m ').strip()
    if os.path.exists(DB_DIR + r'\%s.txt' % choice):
        school_obj = db_handle.load_db(choice)
        print('\033[35;1m ---------欢迎来到%s老男孩学校--------- \033[0m' % choice)
        name = input('\033[32;1mEnter your name >>: \033[0m').strip()
        if name in school_obj.teachers:
            teacher_obj = school_obj.teachers[name]
            print('\033[31;1m该老师负责的班级：\033[0m')
            for i in teacher_obj.grades:
                print(i)
            choice = input('\033[32;1m请选择你要管理的班级：\033[0m').strip()
            if choice in teacher_obj.grades:
                while True:
                    print(TEACHER_MENU)
                    choice1 = input('\033[32;1m请输入要进行的操作：\033[0m').strip()
                    if choice1 == '1':
                        teacher_obj.cat_grade_student()
                    elif choice1 == '2':
                        teacher_obj.modify_student_record(school_obj)
                        school_obj.save_school_db()
                    elif choice1 == 'q':
                        break
                    else:
                        print('\033[33;1m输入错误！！\033[0m')
            else:
                print('\033[33;1m该班级不存在！\033[0m')
        else:
            print('\033[33;1m不好意思，讲师不存在！\033[0m')

    else:
        print('\033[33;1m该学校不存在！\033[0m')

def run():
    print('\033[0;31;40m欢迎使用选课系统\033[0m')
    while True:
        print(START_MENU)
        num = input('请输入数字选择视图 ：')
        if num == '1':
            student_view()
        elif num == '2':
            teacher_view()
        elif num == '3':
            manager_view()
        elif num == 'q':
            break
        else:
            print('\033[31;1m您的输入有误，请重新输入。\033[0m')