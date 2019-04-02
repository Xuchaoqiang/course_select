#! _*_coding:utf-8 _*_
#__author__:"Irving"

class Course:
    '''
    课程类，包含名称、周期、价格、学校
    '''
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price

    def cat_info(self):
        print('\033[33;1m 课程名称：{0} 课程周期:{1}  课程价格：{1}\033[0m'.format(self.name, self.period,self.price))

