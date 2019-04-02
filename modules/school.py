#! _*_coding:utf-8 _*_
#__author__:"Irving"

import pickle
from modules.course import Course
from modules.grade import Grade
from modules.teacher import Teacher
from conf import settings

DB_DIR = settings.DB_DIR

class School:
    '''
    学校类， 包含名称，课程，班级，学员，讲师
    '''
    def __init__(self, name):
        self.name = name
        self.courses = {}
        self.grades = {}
        self.students = {}
        self.teachers = {}

    def create_course(self):
        name = input('课程名称： ').strip()
        if name not in self.courses:
            period = input('课程周期： ').strip()
            price = input('课程价格： ').strip()
            new_course = Course(name, period, price)
            self.courses[name] = new_course
            self.save_school_db()
            print('\033[31;1m课程创建成功！\033[0m')
        else:
            print('\033[33;1m课程已存在！\033[0m')

    def create_grade(self):
        '''
        实现创建班级，主动绑定课程  班级的学生，老师被动绑定
        :return:
        '''
        name = input('班级名称：').strip()
        if name not in self.grades:      # 判断班级是否重名
            new_grade = Grade(name)
            self.cat_course_info()
            course = input('该班绑定的课程：').strip()
            if course in self.courses:
                new_grade.courses.append(self.courses[course])
                print('\033[31;1m班级创建成功！\033[0m')
                self.grades[name] = new_grade  # 班级绑定到学校
                self.save_school_db()
            else:
                print('\033[33;1m课程不存在！\033[0m')
        else:
            print('\033[33;1m班级已存在！\033[0m')

    def create_teacher(self):
        '''
        创建老师，老师这里只需要手动绑定下班级即可，所负责课程、学员直接绑定班级的课程，学员
        :return:
        '''
        name = input('老师名称：').strip()
        if name not in self.teachers:
            new_teacher = Teacher(name)
            self.cat_grade_info()
            grade = input('\033[33;1m请选择该老师绑定的班级：\033[0m').strip()
            if grade in self.grades:
                self.teachers[name] = new_teacher  # 把新建的老师绑定到学校
                new_teacher.grades[grade] = self.grades[grade]  # 老师绑定班级
                self.grades[grade].teachers.append(new_teacher)  # 班级绑定老师
                # 老师绑定班级后， 把班级的课程、学员绑定给老师
                new_teacher.courses.extend(self.grades[grade].courses)
                self.save_school_db()
                print('\033[33;1m老师%s创建成功\033[0m' % name)
            else:
                print('\033[31;1m班级不存在！\033[0m')
        else:
            print('\033[31;1m老师已存在！\033[0m')

    def cat_grade_info(self):
        '''
        查看班级信息
        :return:
        '''
        if len(self.grades) < 1:
            print('\033[31;1m暂无班级信息，请先去创建。\033[0m')
        else:
            for i in self.grades:
                self.grades[i].cat_info()

    def cat_teacher_info(self):
        '''
        查看老师信息
        :return:
        '''
        if len(self.teachers) < 1:
            print('\033[31;1m暂无教师信息，请先去创建。\033[0m')
        else:
            for i in self.teachers:
                self.teachers[i].cat_info()

    def cat_course_info(self):
        '''
        查看老师信息
        :return:
        '''
        for i in self.courses:
            self.courses[i].cat_info()

    def cat_student_info(self):
        '''
        查看学生信息
        :return:
        '''
        if len(self.students) < 1:
            print('\033[31;1m暂无学生信息，请先去创建。\033[0m')
        else:
            for i in self.students:
                self.students[i].cat_info()

    def save_school_db(self):
        with open(DB_DIR + r'\%s.txt' % self.name, 'wb') as f:
            pickle.dump(self, f)








