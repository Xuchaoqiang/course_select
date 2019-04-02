#! _*_coding:utf-8 _*_
#__author__:"Irving"


class Student:
    '''
    学生类， 包含名字、班级
    '''
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.grades = []
        self.cost = 0
        self.record = 0

    def cat_info(self):
        '''
        查看学员信息接口，给学校类调用
        :return:
        '''
        print('姓名: %s   成绩: %s' % (self.name , self.record), end=' ')
        for i in self.grades:
            print('班级: %s' % i.name)

    def payment(self, school_obj):
        '''
        学员缴纳学费接口
        :param school_obj:
        :return:
        '''
        if self.cost > 0:
            print('\033[33;1m您的学费为: %s \033[0m' % self.cost)
            money = input('请输入金额>>：').strip()
            if money.isdigit():
                money = int(money)
                if money == self.cost:
                    self.cost = 0
                    print('\033[31;1m缴纳学费成功！\033[0m')
                    school_obj.save_school_db()
                else:
                    print('\033[31;1m 请正确输入金额！\033[0m')
        else:
            print('\033[31;1m您无需要交学费。\033[0m')

    def select_grade(self, school_obj):
        '''
        学员选择班级接口
        :param school_obj:
        :return:
        '''
        school_obj.cat_grade_info()
        grade = input('\033[33;1m请选择该学员绑定的班级：\033[0m').strip()
        if grade in school_obj.grades:
            self.grades.append(school_obj.grades[grade])    # 把班级绑定到学员里
            school_obj.grades[grade].students[self.name] = self     # 把该学员绑定到班级
            for i in school_obj.grades[grade].teachers:     # 把该学员绑定到 绑定班级 的老师
                i.students[self.name] = self
            school_obj.students[self.name] = self       # 把该学员绑定到相关学校
            grade_course = school_obj.grades[grade].courses     # 获取要绑定的班级的课程对象
            for i in grade_course:      #  获取要绑定的班级的课程对象,拿到该对象的price属性 计算学费
                self.cost += int(i.price)
            school_obj.save_school_db()
            print('\033[33;1m添加班级成功！\033[0m')
        else:
            print('\033[31;1m班级不存在！\033[0m')

    def input_record(self, school_obj):
        '''
        学员填写成绩接口
        :param school_obj:
        :return:
        '''
        record = input('\033[33;1m请输入你的成绩：\033[0m').strip()
        if record.isdigit():
            record = int(record)
            if record < 0:
                print('\033[31;1m成绩不能小于0！\033[0m')
            else:
                self.record = record
                print('\033[33;1m写入成绩成功！！\033[0m')
                self.cat_info()
                school_obj.save_school_db()

