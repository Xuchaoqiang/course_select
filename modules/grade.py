#! _*_coding:utf-8 _*_
#__author__:"Irving"

class Grade:
    '''
    班级类，包含名称，课程，讲师，学员
    '''
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.teachers = []
        self.students = {}

    def cat_info(self):
        '''
        查看班级信息接口，给学校类调用
        :return:
        '''
        print('\033[31;1m--------- %s 班级 ----------\033[0m' % self.name)
        print('该班级的课程信息：', end='')
        for course in self.courses:
            print(course.name, end=' ')
        print('')
        print('该班级的老师信息：', end='')
        for teacher in self.teachers:
            print(teacher.name, end=',')
        print('')
        print('该班级的学员信息：', end='')
        for student in self.students:
            print(student, end=',')
        print('')