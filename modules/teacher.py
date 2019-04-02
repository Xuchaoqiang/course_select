#! _*_coding:utf-8 _*_
#__author__:"Irving"

class Teacher:
    '''
    教师类，包含名字、班级、课程、学员
    '''
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.grades = {}
        self.students = {}

    def cat_info(self):
        '''
        查看讲师信息接口，给学校类调用
        :return:
        '''
        print('\033[31;1m--------- 姓名%s ----------\033[0m' % self.name)
        print('绑定的课程：', end='')
        for i in self.courses:
            print(i.name, end=',')
        print('')
        print('绑定的班级：', end='')
        for i in self.grades:
            print(i, end=',')
        print('')

    def cat_grade_student(self):
        '''
        查看讲师对象下面的班级信息
        :return:
        '''
        if len(self.students) < 1:
            print('\033[31;1m暂无学生信息，请先去创建。\033[0m')
        else:
            for i in self.students:
                print('姓名:{} 年龄:{} 性别:{} 成绩:{}'.format(self.students[i].name, self.students[i].age,
                                                       self.students[i].sex, self.students[i].record))

    def modify_student_record(self, school_obj):
        '''
        修改讲师对象下面的学生成绩
        :param school_obj:
        :return:
        '''
        if len(self.students) < 1:
            print('\033[31;1m暂无学员信息，请先去创建。\033[0m')
        else:
            for i in self.students:
                print('姓名:{}    成绩:{}'.format(self.students[i].name, self.students[i].record))
            student_name = input('请输入要修改成绩的学员:').strip()
            if student_name in self.students:
                modify_value = input('请输入新成绩：').strip()
                if modify_value.isdigit():
                    modify_value = int(modify_value)
                    self.students[student_name].record = modify_value
                    school_obj.save_school_db()     # 对象关联到学校对象， 修改完直接序列化学校对象
                    print('修改成功！')
                else:
                    print('invaild value!')
            else:
                print('学员不存在！')




